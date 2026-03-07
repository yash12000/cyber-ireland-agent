from app.retriever import get_retriever

retriever = get_retriever()

query = "How many cybersecurity jobs are reported in the sector?"

docs = retriever.invoke(query)

print("\nTop Retrieved Documents:\n")

for i, doc in enumerate(docs):

    print(f"\nResult {i+1}")
    print("Page:", doc.metadata.get("page"))
    print("Text:", doc.page_content[:400])