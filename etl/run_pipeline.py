from extract_pdf import extract_text
from chunking import chunk_documents
from load_vector_db import create_vector_db


def run_pipeline():

    print("Extracting PDF...")

    pages = extract_text()

    print("Chunking text...")

    chunks = chunk_documents(pages)

    print("Creating vector database...")

    create_vector_db(chunks)

    print("Vector DB created successfully!")


if __name__ == "__main__":
    run_pipeline()