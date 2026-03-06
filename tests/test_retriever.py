from app.retriever import get_retriever


def test_retrieval():

    retriever = get_retriever()

    docs = retriever.get_relevant_documents(
        "How many cyber security jobs are in Ireland?"
    )

    for doc in docs:
        print(doc.page_content[:200])
        print("Page:", doc.metadata)


if __name__ == "__main__":
    test_retrieval()