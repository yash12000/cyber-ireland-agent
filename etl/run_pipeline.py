from etl.extract_pdf import extract_text
from etl.parse_tables import extract_tables
from etl.chunking import chunk_documents
from etl.load_vector_db import create_vector_db


def run_pipeline():

    print("Step 1: Extracting text from PDF")
    pages = extract_text()

    print("Step 2: Extracting tables")
    tables = extract_tables()

    print("Step 3: Chunking documents")
    chunks = chunk_documents(pages)

    print("Step 4: Creating vector database")
    create_vector_db(chunks)

    print("Pipeline completed successfully")


if __name__ == "__main__":
    run_pipeline()