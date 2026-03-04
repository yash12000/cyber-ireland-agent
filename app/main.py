from fastapi import FastAPI
from app.agent import create_agent

app = FastAPI()

agent = create_agent()


@app.get("/")
def health():

    return {"status": "Cyber Ireland Agent Backend Running"}


@app.post("/query")
def query_agent(question: str):

    response = agent.run(question)

    return {
        "query": question,
        "answer": response
    }