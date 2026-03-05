from app.retriever import get_retriever


retriever = get_retriever()

query = "How many cyber security jobs are in Ireland?"

docs = retriever.invoke(query)

print("Retrieved documents:\n")

for doc in docs:
    print("Page:", doc.metadata["page"])
    print(doc.page_content[:300])
    print("------")