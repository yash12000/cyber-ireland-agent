from langchain.tools import tool
from app.retriever import get_retriever

retriever = get_retriever()


@tool
def retrieve_documents(query: str):
    """
    Retrieve relevant document chunks from the vector database.
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
def calculate_cagr(input_str: str):
    """
    Calculate CAGR.

    Input format:
    start,end,years

    Example:
    7351,17000,8
    """

    try:
        start, end, years = map(float, input_str.split(","))

        cagr = (end / start) ** (1 / years) - 1

        return f"CAGR: {round(cagr * 100, 2)}%"

    except Exception as e:
        return f"Error calculating CAGR: {str(e)}"