from app.documents.embedding_service import (EmbeddingService)

from app.documents.chroma_service import (ChromaService)

from app.gemini_client import (ask_gemini_with_context)


class RAGService:

    def __init__(self):

        self.embedding_service = (EmbeddingService())

        self.chroma_service = (ChromaService())

    def answer_question(self, question: str) -> str:

        query_embedding = (self.embedding_service.create_embedding(question))

        results = (self.chroma_service.search(embedding=query_embedding, top_k=3))

        documents = (results["documents"][0])

        context = "\n\n".join(documents)

        prompt = f"""
        You are a customer support assistant.

        Use ONLY the provided context.

        Context:

        {context}

        Question:

        {question}
        """

        return ask_gemini_with_context(prompt)
