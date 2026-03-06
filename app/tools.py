from langchain.tools import tool
from app.retriever import get_retriever

retriever = get_retriever()


@tool
def retrieve_documents(query: str) -> str:
    """
    Retrieve relevant document chunks from the Cyber Ireland report.
    """

    docs = retriever.invoke(query)

    output = []

    for doc in docs:
        page = doc.metadata.get("page", "unknown")
        output.append(f"Page {page}: {doc.page_content}")

    return "\n\n".join(output)


@tool
def calculate_cagr(start: float, end: float, years: int) -> float:
    """
    Calculate compound annual growth rate (CAGR)
    """

    cagr = (end / start) ** (1 / years) - 1
    return round(cagr * 100, 2)