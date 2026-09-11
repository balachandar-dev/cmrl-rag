import fitz
from pathlib import Path
from chunker import split_text

PDF_PATH = Path("documents/station_facilities.pdf")

doc = fitz.open(PDF_PATH)
all_chunks = []

for page_index in range(len(doc)):
    page = doc.load_page(page_index)
    text = page.get_text()

    chunks = split_text(text)

    for chunk in chunks:
        all_chunks.append({
            "page": page_index + 1,
            "text": chunk
        })

    print(f"Total chunks: {len(all_chunks)}")

    for chunk in all_chunks[:3]:
        print("-" * 40)
        print(f"Page: {chunk['page']}")
        print(chunk["text"])