from app.retriever import get_retriever

def test_retriever():

    retriever = get_retriever()

    docs = retriever.invoke("cyber security jobs Ireland")

    for doc in docs:

        print(doc.page_content[:200])
        print("Page:", doc.metadata)
        print("-"*50)


if __name__ == "__main__":
    test_retriever()