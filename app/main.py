from fastapi import FastAPI
from pydantic import BaseModel
from app.agent import create_agent

app = FastAPI()

agent = create_agent()


class QueryRequest(BaseModel):
    question: str


class QueryResponse(BaseModel):
    query: str
    answer: str


@app.get("/")
def health():
    return {"status": "Cyber Ireland Agent Running"}


@app.post("/query", response_model=QueryResponse)
def query_agent(request: QueryRequest):

    response = agent.run(request.question)

    return {
        "query": request.question,
        "answer": response
    }