from app.documents.pdf_reader import PDFReader


reader = PDFReader()

text = reader.extract_text("sample.pdf")

print(text[:2000])
