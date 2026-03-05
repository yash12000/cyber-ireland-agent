from etl.extract_pdf import extract_text
from etl.chunking import chunk_documents
from etl.load_vector_db import create_vector_db


def run_pipeline():

    print("Starting ETL pipeline...")

    print("Extracting PDF text...")
    pages = extract_text()

    print(f"Pages extracted: {len(pages)}")

    print("Chunking documents...")
    chunks = chunk_documents(pages)

    print(f"Chunks created: {len(chunks)}")

    print("Creating vector database...")
    create_vector_db(chunks)

    print("Vector DB successfully built!")


if __name__ == "__main__":
    run_pipeline()