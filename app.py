from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
from pydantic import BaseModel
from typing import Optional, List
import uvicorn

from main import QueryAnalyzer

query_analyzer = None

class QueryRequest(BaseModel):
    query:str
    top_k: Optional[int] = 5

@asynccontextmanager
async def lifespan(app: FastAPI):
    global query_analyzer
    print("Starting ES Querybot application...")
    query_analyzer = QueryAnalyzer()
    
    yield
    
    print("Application shutdown")

app = FastAPI(title="ES Querybot", lifespan=lifespan)

@app.get("/health")
async def health_check():
    if query_analyzer is None:
        raise HTTPException(status_code=503, detail="Analyzer not initialized")
    return {"status": "healthy", "analyzer_ready": True}


# @app.post("/query")
# def process_nl_query(request: QueryRequest):
#     global query_analyzer
    
#     if query_analyzer is None:
#         raise HTTPException(status_code=503, detail="query_analyzer not initialized")
    
#     try:
#         results = query_analyzer.process_query(request.query,top_k=request.top_k)
        
#         return results

#     except Exception as e:
#         raise HTTPException(status_code=500, detail=str(e))

@app.post("/query")
def process_nl_query(request: QueryRequest):
    global query_analyzer
    
    if query_analyzer is None:
        raise HTTPException(status_code=503, detail="query_analyzer not initialized")
    
    try:
        relevant_indices = query_analyzer.fetch_relevant_indices()
        session_history:List[str] = []
        related_fields = query_analyzer.process_nl_query(request.query,request.top_k)
        
        dsl_query = query_analyzer.generate_dsl_query(
            previous_queries=session_history,
            indices_list=relevant_indices,
            related_fields=related_fields,
            user_input=request.query,
        )
        
        return dsl_query

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


