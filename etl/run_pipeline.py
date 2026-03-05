from etl.extract_pdf import extract_text
from etl.chunking import chunk_documents
from etl.load_vector_db import create_vector_db


def run_pipeline():

    print("Starting ETL pipeline...")

    pages = extract_text()

    print(f"Extracted {len(pages)} pages")

    chunks = chunk_documents(pages)

    print(f"Created {len(chunks)} chunks")

    create_vector_db(chunks)

    print("Vector database created successfully!")


if __name__ == "__main__":
    run_pipeline()