from app.retriever import get_retriever

retriever = get_retriever()

query = "cyber security employment Ireland"

docs = retriever.invoke(query)

seen = set()

for doc in docs:

    text = doc.page_content

    if text not in seen:

        seen.add(text)

        print(text[:200])
        print("Page:", doc.metadata)
        print("-"*50)