import fitz
from pathlib import Path

PDF_PATH = Path("documents/station_facilities.pdf")

doc = fitz.open(PDF_PATH)

print(f"Document : {PDF_PATH.name}")
print(f"Total Pages : {len(doc)}")

for page_index in range(len(doc)):
    page = doc.load_page(page_index)
    text = page.get_text()

    print("\n" + "=" * 50)
    print(f"PAGE {page_index + 1}")
    print("=" * 50)
    print(text[:400])