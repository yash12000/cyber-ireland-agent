from fastapi import FastAPI
from app.agent import create_agent

app = FastAPI()

agent = create_agent()


@app.get("/")
def root():
    return {"message": "Cyber Ireland Agent Running"}


@app.post("/query")
def query_agent(question: str):

    try:
        response = agent.run(question)

        return {
            "query": question,
            "answer": response
        }

    except Exception as e:

        return {
            "error": str(e)
        }