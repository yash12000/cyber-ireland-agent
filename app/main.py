from fastapi import FastAPI
from app.agent import create_agent

app = FastAPI()

agent = create_agent()


@app.get("/")
def home():

    return {"message": "Cyber Ireland Agent Running"}


@app.post("/query")
def query(question: str):

    response = agent.run(question)

    return {
        "query": question,
        "answer": response
    }