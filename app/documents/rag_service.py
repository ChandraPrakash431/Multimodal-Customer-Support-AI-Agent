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

        metadatas = (results["metadatas"][0])

        context_parts = []

        for doc, meta in zip(documents, metadatas):

            source = meta.get("source", "Unknown")

            context_parts.append(f"""
            SOURCE: {source}

            CONTENT:{doc}
            """)

        context = "\n\n".join(context_parts)

        prompt = f"""
        You are a customer support AI.

        Answer ONLY using the supplied context.

        If the answer exists in the context,
        mention the source document.

        Context:

        {context}

        Question:

        {question}
        """
        print(results["metadatas"])
        return ask_gemini_with_context(prompt)
