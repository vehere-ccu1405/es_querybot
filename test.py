import json
import numpy as np 
import os
import faiss
import pickle 
from llama_cpp import Llama 
from pathlib import Path
from typing import List, Tuple, Dict, Any 

EMBED_MODEL = "model/all-MiniLM-L6-v2-Q5_K_M.gguf"
LLM_MODEL = "model/all-MiniLM-L6-v2-Q5_K_M.gguf"
MAPPING_JSON_PATH = "mapping.json"
INDEX_PATH = "embeddings/faiss_index.bin"
DATA_PATH = "embeddings/field_data.pkl"
EMBED_DIMENSION = 384



def field_to_text(field:Dict[str, Any])->str:
    raw_field = field.get("field","")
    dtype = field.get("type","")
    desc = field.get("description","")
    
    tokens = raw_field.replace("."," ").replace("_"," ").split()
    leaf = tokens[-1] if tokens else raw_field
    path_readable = " ".join(tokens)
    
    # simple synonym map for very common leaves
    SYNONYMS: Dict[str, str] = {
        "timestamp": "time date when created occurred",
        "email":     "email address mail contact",
        "email_ids": "email address mail contact list",
        "location":  "place geo country city region address coordinates",
        "person":    "person individual name human",
        "urls":      "url link website http",
        "subjects":  "subject topic category",
        "languages": "language locale lang spoken",
        "organization": "org company firm institution",
        "activities": "activity action event behaviour",
        "text":      "content body message raw text",
        "misc":      "miscellaneous other extra",
        "assign_to": "assigned assignee owner user responsible",
        "casename":  "case name title label",
        "comment":   "comment note remark annotation",
        "condition": "condition rule filter criteria",
    }
    synonyms = SYNONYMS.get(leaf, "")
    print(
        f"Field: {raw_field}\n"
        f"Path tokens: {path_readable}\n"
        f"Leaf name: {leaf}\n"
        f"Data type: {dtype}\n"
        f"Description: {desc}\n"
        f"Related terms: {synonyms}"
    )
    print("\n\n")
    return (
        f"Field: {raw_field}\n"
        f"Path tokens: {path_readable}\n"
        f"Leaf name: {leaf}\n"
        f"Data type: {dtype}\n"
        f"Description: {desc}\n"
        f"Related terms: {synonyms}"
    ).strip()


class FieldExtraction:
    def __init__(self,embed_model_path:str, embedding_dim:int):
        self.embed_model_path = embed_model_path
        self.embedding_dim = embedding_dim
        self.fields_data = []
        self.embeddings = None
        self.index = None
        self.embedding_model = None
        self.llm = None
    
    def load_models(self):
        print(f"loading embedding model from {self.embed_model_path}...")
        self.embedding_model = Llama(
            model_path = self.embed_model_path,
            embedding = True, 
            logits_all=True,
            verbose = False, 
            n_ctx = 384 #limited by quantized model
        )
        print("embedding model loaded...")
        
        
    
    def load_json_fields(self, json_path:str):
        print(f"loading schema fields from json {json_path}...")
        with open(json_path, 'r',encoding='utf-8') as f:
            self.fields_data = json.load(f)
        print(f"Loaded {len(self.fields_data)} fields")
    
    def create_json_text(self, field:Dict[str,Any]) ->str:
        """create a text representation of a json object"""
        return f"Field: {field['field']}\nType: {field['type']}\nDescription: {field['description']}"
    
    def get_embedding(self, text: str) -> np.ndarray:
       
        if not self.embedding_model:
            raise ValueError("Model not loaded. Call load_model() first.")
        
        # Get embedding from llama.cpp
        embeddings = self.embedding_model.create_embedding(text)
        
        token_vecs = np.array(
            [entry["embedding"] for entry in embeddings["data"]], dtype=np.float32
        )
        vec = token_vecs.mean(axis=0)           # mean pooling
        vec /= np.linalg.norm(vec) + 1e-10      # L2 normalisation
        return vec
    
    def get_embeddings_batch(self, texts: List[str], batch_size: int = 64) -> np.ndarray:
        
        vecs = []
        for i, text in enumerate(texts):
            vecs.append(self.get_embedding(text))
            if (i + 1) % batch_size == 0:
                print(f"Embedded {i + 1}/{len(texts)} fields...")
        return np.array(vecs, dtype=np.float32)
    
    def create_embeddings(self, batch_size: int = 64):
        if not self.fields_data:
            raise ValueError("No fields loaded. Call load_json_fields() first.")
 
        texts = [field_to_text(f) for f in self.fields_data]
        print(f"Creating embeddings for {len(texts)} fields …")
        self.embeddings = self.get_embeddings_batch(texts, batch_size=batch_size)
        print(f"Embeddings shape: {self.embeddings.shape}")
        
    def build_faiss_index(self):
        if self.embeddings is None:
            raise ValueError("No embeddings. Call create_embeddings() first.")
 
        print("Building FAISS index …")
        n = len(self.embeddings)
 
        # For ≤ 10 k vectors a flat inner-product index is both fast and exact.
        # For larger corpora swap in IndexIVFFlat or HNSW.
        self.index = faiss.IndexFlatIP(self.embedding_dim)
 
        # Vectors are already L2-normalised by sentence-transformers
        # (normalize_embeddings=True), so inner-product == cosine similarity.
        self.index.add(self.embeddings)
        print(f"FAISS index contains {self.index.ntotal} vectors.")
        
        
    def save_index(self, index_path: str = INDEX_PATH, data_path: str = DATA_PATH):
        os.makedirs(os.path.dirname(index_path), exist_ok=True)
        faiss.write_index(self.index, index_path)
        with open(data_path, "wb") as f:
            pickle.dump({"fields_data": self.fields_data, "embeddings": self.embeddings}, f)
        print(f"Saved index → {index_path}, data → {data_path}")
 
    def load_index(self, index_path: str = INDEX_PATH, data_path: str = DATA_PATH):
        self.index = faiss.read_index(index_path)
        with open(data_path, "rb") as f:
            saved = pickle.load(f)
        self.fields_data = saved["fields_data"]
        self.embeddings  = saved["embeddings"]
        print(f"Loaded index ({self.index.ntotal} vectors) and {len(self.fields_data)} fields.")
    
    def search(self, query: str, top_k: int = 5) -> List[Tuple[Dict, float]]:
        """
        Semantic search over fields.
 
        Returns list of (field_dict, cosine_similarity) sorted descending.
        """
        if self.index is None or not self.fields_data:
            raise ValueError("Index not ready. Build or load it first.")
 
        q_vec = self.get_embedding(query).reshape(1, -1)
        # already normalised → inner product == cosine similarity
        scores, indices = self.index.search(q_vec, min(top_k, len(self.fields_data)))
 
        results = []
        for score, idx in zip(scores[0], indices[0]):
            if 0 <= idx < len(self.fields_data):
                results.append((self.fields_data[idx], float(score)))
        return results
 
    def search_with_threshold(
        self, query: str, top_k: int = 5, min_score: float = 0.3
    ) -> List[Tuple[Dict, float]]:
        """Like search() but filters out low-confidence matches."""
        return [(f, s) for f, s in self.search(query, top_k) if s >= min_score]
 
 
# ── CLI / demo ────────────────────────────────────────────────────────────────
 
def _print_results(results: List[Tuple[Dict, float]], query: str):
    print(f"\nQuery: '{query}'")
    print("─" * 60)
    if not results:
        print("  (no results above threshold)")
        return
    for i, (field, score) in enumerate(results, 1):
        print(f"  {i}. [{score:.4f}]  {field['field']}  ({field['type']})")
        print(f"       {field.get('description', '')}")
 
 
def main():
    extractor = FieldExtraction(embed_model_path=EMBED_MODEL,embedding_dim=EMBED_DIMENSION)
 
    if os.path.exists(INDEX_PATH) and os.path.exists(DATA_PATH):
        print("Loading existing index …")
        extractor.load_models()
        extractor.load_index(INDEX_PATH, DATA_PATH)
    else:
        print("Building new index …")
        extractor.load_models()
        extractor.load_json_fields(MAPPING_JSON_PATH)
        extractor.create_embeddings()
        extractor.build_faiss_index()
        extractor.save_index(INDEX_PATH, DATA_PATH)
 
    test_queries = [
        "fetch all data related to kritin@gmail.com",
        "what data is coming from India",
        "when was this record created",
        "who is assigned to this case",
        "detected language of message",
        "GPS coordinates of device",
        "filter by case name",
        "raw message body text",
    ]
 
    for q in test_queries:
        results = extractor.search_with_threshold(q, top_k=3, min_score=0.25)
        _print_results(results, q)
 
 
if __name__ == "__main__":
    main()