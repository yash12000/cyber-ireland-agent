from app.retriever import get_retriever

retriever = get_retriever()

query = "How many cyber security jobs are there in Ireland?"

docs = retriever.get_relevant_documents(query)

for i, doc in enumerate(docs):
    print("\n--- Result", i+1, "---")
    print(doc.page_content[:300])
    print("Page:", doc.metadata)