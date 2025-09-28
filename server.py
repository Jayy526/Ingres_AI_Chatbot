from fastapi import FastAPI
from pydantic import BaseModel
from tools import run_rag_pipeline


app = FastAPI()


class Query(BaseModel):
    question: str


@app.post("/ask")
async def ask_bot(query: Query):
    response = run_rag_pipeline(query.question)
    return {"answer": response}