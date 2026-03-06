from langchain.tools import tool
from app.retriever import get_retriever

retriever = get_retriever()


@tool
def retrieve_documents(query: str):
    """
    Retrieve relevant document chunks from the Cyber Ireland report
    and return their content with page numbers.
    """

    docs = retriever.get_relevant_documents(query)

    results = []

    for doc in docs:
        results.append(
            {
                "text": doc.page_content,
                "page": doc.metadata.get("page"),
            }
        )

    return results


@tool
def calculate_cagr(input_str: str):
    """
    Calculate Compound Annual Growth Rate (CAGR).

    Input format:
    "start,end,years"

    Example:
    "7351,17000,8"
    """

    start, end, years = input_str.split(",")

    start = float(start)
    end = float(end)
    years = int(years)

    cagr = (end / start) ** (1 / years) - 1

    return round(cagr * 100, 2)