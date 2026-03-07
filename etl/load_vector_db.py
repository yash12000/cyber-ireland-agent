from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings


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

    return vectordb