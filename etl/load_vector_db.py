from langchain.vectorstores import Chroma
from langchain.embeddings import HuggingFaceEmbeddings


def create_vector_db(chunks):

    texts = [c["content"] for c in chunks]
    metadata = [{"page": c["page"]} for c in chunks]

    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    vectordb = Chroma.from_texts(
        texts=texts,
        embedding=embeddings,
        metadatas=metadata,
        persist_directory="db"
    )

    vectordb.persist()

    return vectordb