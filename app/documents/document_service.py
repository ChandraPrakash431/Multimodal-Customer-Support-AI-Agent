import os

from app.documents.pdf_reader import (PDFReader)

from app.documents.chunker import (TextChunker)

from app.documents.embedding_service import (EmbeddingService)

from app.documents.chroma_service import (ChromaService)


class DocumentService:

    def __init__(self):

        self.reader = PDFReader()

        self.chunker = TextChunker()

        self.embedding_service = (EmbeddingService())

        self.chroma_service = (ChromaService())

    def ingest_pdf(self, pdf_path: str):

        text = self.reader.extract_text(pdf_path)

        chunks = self.chunker.chunk_text(text)

        filename = os.path.basename(pdf_path)

        for index, chunk in enumerate(chunks):

            embedding = (self.embedding_service.create_embedding(chunk))

            chunk_id = (f"{filename}_{index}")

            self.chroma_service.add_chunk(chunk_id=chunk_id, text=chunk, embedding=embedding)

        return len(chunks)
