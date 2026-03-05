from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings


def create_vector_db(chunks):

    embedding = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    texts = [c["content"] for c in chunks]

    metadata = [{"page": c["page"]} for c in chunks]

    vectordb = Chroma.from_texts(
        texts=texts,
        embedding=embedding,
        metadatas=metadata,
        persist_directory="db"
    )

    vectordb.persist()

    return vectordb