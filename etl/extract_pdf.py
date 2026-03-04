import pdfplumber

PDF_PATH = "data/raw/cyber_security_report.pdf"

def extract_text():

    pages = []

    with pdfplumber.open(PDF_PATH) as pdf:
        for i, page in enumerate(pdf.pages):

            text = page.extract_text()

            pages.append({
                "page": i + 1,
                "text": text
            })

    return pages


if __name__ == "__main__":

    pages = extract_text()

    print("Total Pages:", len(pages))
    print(pages[0]["text"][:500])