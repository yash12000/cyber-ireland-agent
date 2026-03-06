from langchain.agents import initialize_agent
from langchain.chat_models import ChatOpenAI
from dotenv import load_dotenv
import os

from app.tools import retrieve_documents, calculate_cagr

load_dotenv()


def create_agent():

    llm = ChatOpenAI(
        model="gpt-4o",
        temperature=0,
        openai_api_key=os.getenv("OPENAI_API_KEY")
    )

    tools = [
        retrieve_documents,
        calculate_cagr
    ]

    agent = initialize_agent(
        tools,
        llm,
        agent="zero-shot-react-description",
        verbose=True
    )

    return agent