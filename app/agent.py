from langchain.agents import initialize_agent
from langchain.chat_models import ChatOpenAI
from app.tools import retrieve_documents, calculate_cagr


def create_agent():

    llm = ChatOpenAI(
        model="gpt-4o",
        temperature=0
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