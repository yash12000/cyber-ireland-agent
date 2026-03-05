from langchain.tools import tool
from app.retriever import get_retriever

retriever = get_retriever()


@tool
def retrieve_documents(query: str):
    """
    Retrieve relevant document chunks from the Cyber Ireland report.
    Returns the text and page numbers where information is found.
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
    Calculate Compound Annual Growth Rate (CAGR).
    Used for forecasting employment growth calculations.
    """

    cagr = (end / start) ** (1 / years) - 1

    return round(cagr * 100, 2)