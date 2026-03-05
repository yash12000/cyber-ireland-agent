from langchain.vectorstores import Chroma
from langchain.embeddings import HuggingFaceEmbeddings


def get_retriever():

    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    vectordb = Chroma(
        persist_directory="db",
        embedding_function=embeddings
    )

    retriever = vectordb.as_retriever(
        search_kwargs={"k": 5}
    )

    return retriever