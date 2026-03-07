from app.retriever import get_retriever

retriever = get_retriever()

query = "How many cyber security professionals are employed?"

docs = retriever.get_relevant_documents(query)

for doc in docs:
    print("\nPAGE:", doc.metadata["page"])
    print(doc.page_content[:500])