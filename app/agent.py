from langchain_openai import ChatOpenAI
from langchain.agents import AgentExecutor, create_tool_calling_agent
from langchain.prompts import ChatPromptTemplate

from app.tools import retrieve_documents, calculate_cagr


def create_agent():

    llm = ChatOpenAI(
        model="gpt-4o-mini",
        temperature=0
    )

    tools = [
        retrieve_documents,
        calculate_cagr
    ]

    prompt = ChatPromptTemplate.from_messages(
        [
            ("system",
             "You are an AI assistant that answers questions using retrieved documents. "
             "Always provide citations including page numbers."),
            ("human", "{input}"),
            ("placeholder", "{agent_scratchpad}")
        ]
    )

    agent = create_tool_calling_agent(
        llm,
        tools,
        prompt
    )

    agent_executor = AgentExecutor(
        agent=agent,
        tools=tools,
        verbose=True
    )

    return agent_executor