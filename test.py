from __future__ import annotations

import json
import numpy as np 
import os
import faiss
import pickle 
from llama_cpp import Llama 
from pathlib import Path
from typing import List, Tuple, Dict, Any , Optional
from dataclasses import field, dataclass

EMBED_MODEL = "model/bge-small-en-v1.5.Q5_K_M.gguf"
# EMBED_MODEL = "model/all-MiniLM-L6-v2-Q5_K_M.gguf"
LLM_MODEL = "model/Qwen3.5-9B-Q4_K_M.gguf"
MAPPING_JSON_PATH = "raw_mapping.json"
INDEX_PATH = "embeddings/faiss_index.bin"
DATA_PATH = "embeddings/field_data.pkl"
EMBED_DIMENSION = 384 # for all-MiniLM-L6

from field_enrichment_mapping import FIELD_ENRICHMENT

@dataclass
class FieldEmbeddingExtraction:
    raw_field:str
    dtype:str
    description:str
    path_terms:list = field(default_factory=list)
    is_nested:bool = False
    parent_path:Optional[str] = None
    synonyms:list = field(default_factory=list)
    context_phrases:list = field(default_factory=list)
    
    
    def to_embedding_text(self)->str:
        parts = [f"Field '{self.raw_field}' (Type:{self.dtype}): {self.description}."]
        if self.is_nested:
            parts.append(
                f"Nested Field:'{self.path_terms[-1]}' lives inside '{self.parent_path}'"
            )
        if self.path_terms:
            parts.append(f"Path components: {', '.join(self.path_terms)}")
        if self.synonyms:
            parts.append(f"Synonyms: {', '.join(self.synonyms)}")
        if self.context_phrases:
            parts.append(f"Usage examples: {' '.join(self.context_phrases)}")
        
        return " ".join(parts)
    
    
def _enrich_fields(raw_field:str,dtype:str,description:str)->FieldEmbeddingExtraction:
    parts = raw_field.split(".")
    is_nested = len(parts)>1
    parent_path = ".".join(parts[:-1]) if is_nested else None
    enrichment = FIELD_ENRICHMENT.get(raw_field, {})
    return FieldEmbeddingExtraction(
        raw_field=raw_field,
        dtype=dtype,
        description=description,
        path_terms=parts,
        is_nested=is_nested,
        parent_path=parent_path,
        synonyms=enrichment.get("synonyms",[]),
        context_phrases=enrichment.get("context_phrases",[])
    )
    
    
class QueryAnalyzer:
    def __init__(self,embed_model_path=EMBED_MODEL,embedding_dim=EMBED_DIMENSION,index_path=INDEX_PATH,data_path=DATA_PATH):
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
        self.embedding_dim = embedding_dim
        self.index: Optional[faiss.IndexFlatIP] = None
        self.docs: List[FieldEmbeddingExtraction] = []
        
        if os.path.exists(index_path) and os.path.exists(data_path):
            self.load_index(index_path,data_path)
        else:
            self.build_index(mapping_json_path,index_path,data_path)


    def embed(self, texts:List[str])->np.ndarray:
        vectors = []
        for text in texts:
            response = self.embedding_model.create_embedding(text)
            vector = np.array(response["data"][0]["embedding"],dtype=np.float32)
            vectors.append(vector)
        matrix = np.vstack(vectors)
        norms = np.linalg.norm(matrix, axis=1, keepdims=True)
        return matrix / np.maximum(norms,1e-10)
    
    
    def build_index(self,mapping_json_path=MAPPING_JSON_PATH,index_path=INDEX_PATH,data_path=DATA_PATH):
        
        if os.path.exists(index_path) and os.path.exists(data_path):
            print(f"Index and Data files already exist in Embeddings directory. Skipping build.")
            return
        
        print("Building Index")
        
        with open(mapping_json_path, 'r',encoding='utf-8') as f:
            raw_fields = json.load(f)
        
        self.docs = [_enrich_fields(f["field"],f["type"],f["description"]) for f in raw_fields]
                
        print(f"Embedding {len(self.docs)} fields...")
        
        embeddings = self.embed([doc.to_embedding_text() for doc in self.docs]) 
        
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
                "raw_field": doc.raw_field,
                "type": doc.dtype,
                "description": doc.description,
                "is_nested": doc.is_nested,
                "parent_path": doc.parent_path,
                "synonyms": doc.synonyms,
            })
        
        related_fields = [res['raw_field'] for res in similarity_search_results] 
        
        return related_fields
    
    def generate_dsl_query()
    
    
if __name__ == "__main__":
    query_analyzer = QueryAnalyzer()
   
    queries = [
        "list all mails coming from abc@gmail.com",
    ]
    
    for q in queries:
        print(f"\nQuery: '{q}'")
        print("-" * 60)
        result = query_analyzer.process_query(q,top_k=5)
        print(result)
    
    
    
=============================

def _build_prompt(
        self,
        previous_queries:List, 
        indices_list:List,
        related_fields:List,
        user_input:str
    )->str: THIS WORKS THE BEST
        # prompt_template = """You are an Elasticsearch Database Administrator for this organization. Your job is to create READ-only DSL queries from the user's natural language input.You do NOT have permission to execute write requests on the Elasticsearch database.
        
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
        # 1. Based on the user's input, use some or all of the related fields and the given indices to create a READ-only DSL query.
        # 2. The query should return a list of results matching the user's request.
        # 3. Ensure the query syntax is valid Elasticsearch DSL.
        # 4. If the user's request seems to require a WRITE operation, politely explain that you can only generate READ queries.
        # 5. Consider the session context (previous queries) to understand the conversation flow if needed.
        
        # **User Input:**
        # {user_input}
        
        # **Generated DSL Query:**
        # ```json
        # """
        
        prompt_template = """You are an Elasticsearch Database Administrator for this organization. Your job is to create READ-only DSL queries from the user's natural language input. You do NOT have permission to execute write requests on the Elasticsearch database.

        **Session Context:**
        - Previous queries in this session: {previous_queries}

        **Available Indices:**
        {indices_list}

        **Brief Description of Each Index:**
        1. logvehere-alerts-* : This index stores all the network security alerts that we receive from our DNN model, highlighting suspicious activity in incoming data.
        2. logvehere-probe-tm-* : Stores all data related to filters set under "Capture Filter" section in our Product.
        3. logvehere-probe-ma-* : Stores the rest of incoming data that doesn't get filtered out by "Capture Filter".

        **Related Schema Fields:**
        {related_fields}

        **Instructions:**
        1. Based on the user's input, use some or all of the related fields and the given indices to create a READ-only DSL query.
        2. The query should return a list of results matching the user's request.
        3. Ensure the query syntax is valid Elasticsearch DSL.
        4. If the user's request seems to require a WRITE operation, politely explain that you can only generate READ queries.
        5. Consider the session context (previous queries) to understand the conversation flow if needed.
        6. Always select the most relevant index (or indices) based on the query intent.

        7. Choose the appropriate HTTP method:
        - Use GET for standard search queries.
        - Use POST if:
        a) the query is very large or complex,
        b) the operation involves `_msearch`,
        c) the operation involves `scroll` or deep pagination.

        8. Always include the Elasticsearch endpoint in the format:
        <METHOD> /<index_name>/_search

        9. The response MUST include both:
        - The HTTP method + endpoint
        - The JSON DSL query body

        10. Output strictly in the following format:

        <METHOD> /<index_name>/_search
        ```json
        {
        "query": { ... }
        }
        User Input:
        {user_input}

        Generated DSL Query:
        """

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
    
