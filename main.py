from __future__ import annotations

import json
import re
import numpy as np 
import os
import faiss
import pickle 
from opensearchpy import OpenSearch
from llama_cpp import Llama 
from pathlib import Path
from typing import List, Tuple, Dict, Any , Optional
from dataclasses import field, dataclass

import urllib3
urllib3.disable_warnings()

EMBED_MODEL = "model/bge-small-en-v1.5.Q5_K_M.gguf"
# EMBED_MODEL = "model/all-MiniLM-L6-v2-Q5_K_M.gguf"
# LLM_MODEL = "model/Qwen3.5-9B-Q4_K_M.gguf"
LLM_MODEL = "model/Qwen2.5-7B-Instruct-Q6_K_L.gguf"
MAPPING_JSON_PATH = "raw_mapping.json"
INDEX_PATH = "embeddings/faiss_index.bin"
DATA_PATH = "embeddings/field_data.pkl"
EMBED_DIMENSION = 384 # for all-MiniLM-L6 & bge-small-en-v1.5

from field_enrichment_mapping import FIELD_ENRICHMENT
    
class QueryAnalyzer:
    def __init__(
        self,
        llm_model_path=LLM_MODEL,
        embed_model_path=EMBED_MODEL,
        embedding_dim=EMBED_DIMENSION,
        mapping_json_path=MAPPING_JSON_PATH,
        index_path=INDEX_PATH,
        data_path=DATA_PATH):
    
        print("Initializing QueryAnalyzer...")
        
        self.ALLOWED_READ_MOETHODS = {"GET","POST"}
        
        self.BLOCKED_ENDPOINT_KEYWORDS = [
            "_delete","_update","_bulk","_index","_create","_reindex"
        ]
        
        self.INDEX_PATTERN = [re.compile(
            r"^(logvehere-(probe-ma|probe-tm|alerts)-\d{8})$"
        )]
        
        
        # PATTERNS = [
        #     r"^logvehere-alerts-\d{8}$",
        #     # r"^logvehere-probe-\d{8}$",
        #     r"^logvehere-probe-ma-\d{8}$",
        #     r"^logvehere-probe-tm-\d{8}$",
        # ]

        # self.compiled_patterns = [re.compile(P) for P in PATTERNS]

        # check correct parameter values
        # self.llm = Llama(
        #     model_path=llm_model_path,
        #     embedding=True,
        #     n_ctx=8192, # 512
        #     n_batch=384,
        #     n_ubatch=384, # same as n_ctx
        #     pooling_type=1,
        #     n_threads=4,
        #     verbose=False,
        #     logits_all=True
        # )
        
        self.llm = Llama(
            model_path=llm_model_path,
            embedding=False,
            n_ctx=8192,
            n_threads=8,
            verbose=False
        )
        
        self.embedding_model = Llama(
            model_path=embed_model_path,
            embedding=True,
            n_ctx=384, # 512
            n_batch=384,
            n_ubatch=384, # same as n_ctx
            pooling_type=1,
            n_threads=4,
            verbose=False,
            logits_all=True
        )
        
        self.db_client = OpenSearch(
            hosts=[{"host": "10.1.3.110", "port": 9200}],
            http_auth=("admin", "admin"),
            use_ssl=True,
            verify_certs=False
        )   
        
        self.embedding_dim = embedding_dim
        self.index: Optional[faiss.IndexFlatIP] = None
        self.docs: List[dict] = []
        
        if os.path.exists(index_path) and os.path.exists(data_path):
            self.load_index(index_path,data_path)
        else:
            self.build_index(mapping_json_path,index_path,data_path)


    def _enrich_field(self,raw_field:str,dtype:str,description:str) ->dict:
        parts = raw_field.split(".")
        is_nested = len(parts) > 1
        parent_path = ".".join(parts[:-1]) if is_nested else None
        enrichment = FIELD_ENRICHMENT.get(raw_field, {})
        return {
            "raw_field": raw_field,
            "dtype": dtype,
            "description": description,
            "path_terms": parts,
            "is_nested": is_nested,
            "parent_path": parent_path,
            "synonyms": enrichment.get("synonyms", []),
            "context_phrases": enrichment.get("context_phrases", [])
        }
        

    def _to_embedding_text(self, doc: dict) -> str:
        parts = [f"Field '{doc['raw_field']}' (Type:{doc['dtype']}): {doc['description']}."]
        if doc["is_nested"]:
            parts.append(
                f"Nested Field:'{doc['path_terms'][-1]}' lives inside '{doc['parent_path']}'"
            )
        if doc["path_terms"]:
            parts.append(f"Path components: {', '.join(doc['path_terms'])}")
        if doc["synonyms"]:
            parts.append(f"Synonyms: {', '.join(doc['synonyms'])}")
        if doc["context_phrases"]:
            parts.append(f"Usage examples: {' '.join(doc['context_phrases'])}")
        return " ".join(parts)


    def embed(self, texts:List[str])->np.ndarray:
        vectors = []
        for text in texts:
            response = self.embedding_model.create_embedding(text)
            vector = np.array(response["data"][0]["embedding"],dtype=np.float32)
            vectors.append(vector)
        matrix = np.vstack(vectors)
        norms = np.linalg.norm(matrix, axis=1, keepdims=True)
        return matrix / np.maximum(norms,1e-10)
    
    
    def build_index(
        self,
        mapping_json_path=MAPPING_JSON_PATH,
        index_path=INDEX_PATH,
        data_path=DATA_PATH
    ):
        if os.path.exists(index_path) and os.path.exists(data_path):
            print(f"Index and Data files already exist in Embeddings directory. Skipping build.")
            return
        
        print("Building Index")
        
        with open(mapping_json_path, 'r',encoding='utf-8') as f:
            raw_fields = json.load(f)
        
        self.docs = [self._enrich_field(f["field"],f["type"],f["description"]) for f in raw_fields]     
        print(f"Embedding {len(self.docs)} fields...")
        embeddings = self.embed([self._to_embedding_text(doc) for doc in self.docs]) 
        
        self.index = faiss.IndexFlatIP(self.embedding_dim)
        self.index.add(embeddings)
        
        Path(index_path).parent.mkdir(parents=True, exist_ok=True)
        faiss.write_index(self.index, index_path)
        Path(data_path).parent.mkdir(parents=True, exist_ok=True)
        with open(data_path, "wb") as f:
            pickle.dump(self.docs, f)

        print(f"Indexing Done. {len(self.docs)} fields indexed.")
    
    
    def load_index(self, index_path=INDEX_PATH, data_path=DATA_PATH):
        self.index = faiss.read_index(index_path)
        with open(data_path, "rb") as f:
            self.docs = pickle.load(f)
        print(f"Loading Index. Loaded {len(self.docs)} fields.") 
    
    
    def process_nl_query(self, nl_input:str, top_k:int=5):
        if self.index is None:
            raise RuntimeError("Index not loaded. Call build_index() or load_index().")
        
        q_vec = self.embed([nl_input])
        scores, indices = self.index.search(q_vec,top_k)
        similarity_search_results = []
        
        for rank, (idx, score) in enumerate(zip(indices[0], scores[0]), start=1):
            if idx == -1:     
                continue
            doc = self.docs[idx]
            similarity_search_results.append({
                "rank": rank,
                "score": float(score),
                "raw_field": doc["raw_field"], 
                "type": doc["dtype"],
                "description": doc["description"],
                "is_nested": doc["is_nested"],
                "parent_path": doc["parent_path"],
                "synonyms": doc["synonyms"],
            })
        
        related_fields = [res['raw_field'] for res in similarity_search_results] 
        
        return related_fields
    
    
    def fetch_relevant_indices(self):
        all_indices = self.db_client.cat.indices(format="json")
        # print(f"No.of Indices: {len(all_indices)}")    
        filtered_indices = [
            idx["index"] for idx in all_indices 
            if any(p.match(idx["index"]) for p in self.INDEX_PATTERN)
        ]
        return filtered_indices
    
    
    def _build_prompt(
        self,
        previous_queries:List, 
        indices_list:List,
        related_fields:List,
        user_input:str
        )->str:
        
        # prompt_template = """You are an Elasticsearch Database Administrator for this organization. Your job is to create READ-only Elasticsearch queries from the user's natural language input.

        # You MUST return the complete request including:
        # - HTTP Method (always GET)
        # - Endpoint in the format: /<index_name>/_search
        # - JSON body (DSL query)

        # You do NOT have permission to execute write requests on the Elasticsearch database. 
        
        # **Session Context:**
        # - Previous queries in this session: {previous_queries}
        
        # **Available Indices:**
        # {indices_list}
        
        
        # **Brief Description of Each Index:**
        # 1. logvehere-alerts-* : This index stores all the network security alerts that we receive from our DNN model, highlighting suspicious activity in incoming data.
        # 2. logvehere-probe-tm-* : Stores all data related to filters set under "Capture Filter" section in our Product. Capture Filters allows us to target some specific features of the incoming data which we want to specifically analyze.
        # 3. logvehere-probe-ma-* : Stores the rest of incoming data that doesn't get filtered out by "Capture Filter".
        
        # **Related Schema Fields:**
        # {related_fields}
        
        # **Instructions:**
        # 1. Based on the user's input, use some or all of the related fields and the given indices to create a READ-only query.
        # 2. The query should return a list of results matching the user's request.
        # 3. Ensure the query syntax is valid Elasticsearch DSL.
        # 4. ALWAYS include:
        #    - HTTP Method: GET
        #    - Endpoint: /<appropriate_index_name>/_search
        #    - JSON body
        # 5. If multiple indices are relevant, choose the most appropriate one or use a wildcard index.
        # 6. If the user's request seems to require a WRITE operation, politely explain that you can only generate READ queries.
        # 7. Consider the session context (previous queries) to understand the conversation flow if needed.
        
        # **Output Format (STRICT):**
        # GET /<index_name>/_search
        # {{
        #   "query": {{
        #     ...
        #   }}
        # }}
        
        # **User Input:**
        # {user_input}
        
        # **Generated Query:**
        # """
        prompt_template = """You are an Elasticsearch Database Administrator for this organization. Your job is to create READ-only Elasticsearch queries from the user's natural language input.

        You MUST return the complete request including:
        - HTTP Method (always GET)
        - Endpoint in the format: /<index_name>/_search
        - JSON body (DSL query)

        You do NOT have permission to execute write requests on the Elasticsearch database.
        
        ---
        **Session Context:**
        - Previous queries in this session: {previous_queries}
        ---

        **Available Indices:**
        {indices_list}

        ---
        **Index Selection Rules (VERY IMPORTANT):**

        1. logvehere-alerts-*  
        - Use ONLY for security alerts, anomalies, or suspicious activity detected by models.  
        - DO NOT use for raw or general data queries.

        2. logvehere-probe-tm-*  
        - Contains filtered/targeted data based on Capture Filters.  
        - Use when the query refers to specifically monitored or filtered attributes.

        3. logvehere-probe-ma-*  
        - Contains ALL general/raw incoming data.  
        - Default index for queries involving emails, IPs, payload fields, or general logs.

        **Multi-Index Rule:**
        - If the query is general (e.g., emails, IPs, payload fields), use BOTH:
        logvehere-probe-ma-*,logvehere-probe-tm-*
        - NEVER use logvehere-alerts-* unless the query explicitly refers to alerts, threats, or anomalies.

        ---
        **Related Schema Fields:**
        {related_fields}
        
        ---
        **Instructions:**
        1. Based on the user's input, use relevant fields and indices to create a READ-only query.
        2. Ensure the query syntax is valid Elasticsearch DSL.
        3. ALWAYS include:
        - HTTP Method: GET
        - Endpoint: /<index_name>/_search
        - JSON body
        4. Carefully choose the correct index:
        - General data queries → logvehere-probe-ma-*,logvehere-probe-tm-*
        - Alerts/anomalies only → logvehere-alerts-*
        5. If multiple indices are required, include them as comma-separated values.
        6. If the user's request requires a WRITE operation, politely refuse.
        7. Consider session context if needed.
        
        ---
        **CRITICAL OUTPUT RULES:**
        1. Output ONLY the final query.
        2. Do NOT include explanations, reasoning, or comments.
        3. Do NOT describe your choice of index.
        4. Do NOT wrap the output in markdown or code blocks.
        5. The response MUST start with: GET 
        6. The response MUST end immediately after the final closing curly brace
        7. Any text after the closing curly brace is strictly forbidden.

        ---
        **Output Format (STRICT):**
        GET /<index_name>/_search
        {{
          "query": {{
            ...
          }}
        }}

        ---
        **User Input:**
        {user_input}

        ---
        Output:"""

        formated_template = prompt_template.format(
            previous_queries=json.dumps(previous_queries, indent=2),
            indices_list="\n".join(f"  - {i}" for i in indices_list),
            related_fields="\n".join(f"  - {f}" for f in related_fields),
            user_input=user_input,
        )
        # print("="*60)
        # print(formated_template)
        # print("="*60)
        return formated_template
        
    
    def generate_dsl_query(
        self,
        previous_queries:List, 
        indices_list:List,
        related_fields:List,
        user_input:List,
        max_tokens:int=512,
        temperature:float=0.1 
    )->str:
        
        prompt = self._build_prompt(previous_queries,indices_list,related_fields,user_input)
        print("Generating DSL query from LLM...")
        
        response = self.llm(
            prompt, 
            max_tokens=max_tokens,
            temperature=temperature,
            top_p=0.9,
            repeat_penalty=1.2,
            # stop=["```\n", "```"],
            stop=["\n\n","} GET"],
            echo=False
        )
        
        generated_text = response["choices"][0]["text"].strip()
        # print(type(generated_text))
        # json_text = json.loads(generated_text)
        # print(type(json_text))
        return generated_text
        # return json_text
        # return response

    def extract_single_query(self,generated_query:str):
        first_request = generated_query.find("GET")
        if first_request == -1:
            return generated_query.strip()
        
        brace_count = 0
        end_idx = None 
        
        for i, ch in enumerate(generated_query[first_request:]):
            if ch == '{':
                brace_count += 1
            elif ch == "}":
                brace_count -= 1
                if brace_count == 0:
                    end_idx = first_request + i + 1
                    break
                
        return generated_query[first_request:end_idx].strip() if end_idx else generated_query.strip()
    
    
    
    
if __name__ == "__main__":
    query_analyzer = QueryAnalyzer()
    
    relevant_indices = query_analyzer.fetch_relevant_indices()
    # print("Fetched Indices:",relevant_indices)
    
    session_history:List[str] = []
    
    # print("Fetched Indices:",query_analyzer.fetch_relevant_indices())
    queries = [
        "List all mails coming from abc@gmail.com",
    ]
    
    
    
    for q in queries:
        print(f"\nQuery: '{q}'")
        print("-" * 60)
 
        # Step 1: retrieve relevant schema fields via semantic search
        related_fields = query_analyzer.process_nl_query(q, top_k=5)
        print("Related fields:", related_fields)
 
        # Step 2: generate the DSL query using the LLM
        generated_query = query_analyzer.generate_dsl_query(
            previous_queries=session_history,
            indices_list=relevant_indices,
            related_fields=related_fields,
            user_input=q,
        )
        
        print("Generated DSL Query:\n", generated_query)
        # print("="*50)
        # cleaned_query = query_analyzer.extract_single_query(generated_query)
        # print("Single Query:\n", cleaned_query)
 
        # Keep a session history of past natural-language queries
        session_history.append(q)
    