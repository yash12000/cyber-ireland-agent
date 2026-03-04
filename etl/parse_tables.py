import camelot
from pathlib import Path

PDF_PATH = Path("data/raw/cyber_security_report.pdf")


def extract_tables():

    tables = camelot.read_pdf(
        str(PDF_PATH),
        pages="all",
        flavor="stream"
    )

    extracted_tables = []

    for i, table in enumerate(tables):

        extracted_tables.append({
            "page": table.page,
            "data": table.df.to_dict()
        })

    return extracted_tables


if __name__ == "__main__":

    tables = extract_tables()

    print("Tables extracted:", len(tables))