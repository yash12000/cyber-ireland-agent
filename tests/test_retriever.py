from app.retriever import get_retriever

retriever = get_retriever()

docs = retriever.get_relevant_documents("How many jobs are reported?")

print(docs[0].page_content)