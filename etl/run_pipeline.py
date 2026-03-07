from etl.extract_pdf import extract_text
from etl.chunking import chunk_documents
from etl.load_vector_db import create_vector_db


def run_pipeline():

    print("Extracting PDF text...")

    pages = extract_text()

    print(f"Extracted {len(pages)} pages")

    print("Chunking documents...")

    chunks = chunk_documents(pages)

    print(f"Created {len(chunks)} chunks")

    print("Creating vector database...")

    create_vector_db(chunks)

    print("Vector database created successfully!")


if __name__ == "__main__":
    run_pipeline()