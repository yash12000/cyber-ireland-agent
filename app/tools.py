from langchain.tools import tool
from app.retriever import get_retriever

retriever = get_retriever()


@tool
def retrieve_documents(query: str):
    """
    Retrieve relevant document chunks from the report
    """

    docs = retriever.get_relevant_documents(query)

    results = []

    for doc in docs:
        results.append({
            "text": doc.page_content,
            "page": doc.metadata.get("page")
        })

    return results


@tool
def calculate_cagr(start: float, end: float, years: int):
    """
    Calculate compound annual growth rate
    """

    cagr = (end / start) ** (1 / years) - 1

    return round(cagr * 100, 2)