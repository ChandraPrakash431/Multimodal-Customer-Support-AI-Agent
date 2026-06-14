from app.documents.pdf_reader import PDFReader
from app.documents.chunker import TextChunker
from app.documents.embedding_service import (EmbeddingService)
from app.documents.chroma_service import (ChromaService)


reader = PDFReader()

chunker = TextChunker()

embedding_service = (EmbeddingService())

chroma = ChromaService()


text = reader.extract_text("sample.pdf")

chunks = chunker.chunk_text(text)


for i, chunk in enumerate(chunks):

    embedding = (embedding_service.create_embedding(chunk))

    chroma.add_chunk(chunk_id=f"chunk_{i}", text=chunk, embedding=embedding)

    print(f"Stored chunk {i}")
