from fastapi import FastAPI
from pydantic import BaseModel
from app.agent import create_agent

app = FastAPI()

agent = create_agent()


class QueryRequest(BaseModel):
    question: str


@app.get("/")
def health():
    return {"status": "Cyber Ireland Agent Running"}


@app.post("/query")
def query_agent(request: QueryRequest):

    response = agent.invoke(
        {"input": request.question}
    )

    return {
        "query": request.question,
        "answer": response["output"]
    }