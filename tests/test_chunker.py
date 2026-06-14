from app.documents.pdf_reader import PDFReader
from app.documents.chunker import TextChunker


reader = PDFReader()

chunker = TextChunker()


text = reader.extract_text("sample.pdf")

chunks = chunker.chunk_text(text)

print(f"Total Chunks: {len(chunks)}")

print("\nFIRST CHUNK:\n")

print(chunks[0])

for i, chunk in enumerate(chunks):

    print(
        f"\nChunk {i + 1}"
    )

    print("-" * 50)

    print(chunk[:200])
