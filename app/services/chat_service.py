from sqlalchemy.orm import Session

from app.database.repository import (ConversationRepository)

from app.documents.embedding_service import (EmbeddingService)

from app.documents.chroma_service import (ChromaService)

from app.gemini_client import (ask_gemini_with_context)


class ChatService:

    def __init__(self):

        self.embedding_service = (EmbeddingService())

        self.chroma_service = (ChromaService())

        self.repository = (ConversationRepository())

    def process_message(self, db: Session, session_id: str, message: str) -> str:

        history = self.repository.get_by_session(db=db, session_id=session_id, limit=10)

        conversation_context = ""

        for item in history:

            conversation_context += (
                f"User: {item.user_message}\n"
                f"Assistant: {item.ai_response}\n"
            )
        
        query_embedding = (self.embedding_service.create_embedding(message))

        results = (self.chroma_service.search(embedding=query_embedding, top_k=3))

        document_context = ""

        documents = (results["documents"][0])

        metadata = (results["metadatas"][0])

        for doc, meta in zip(documents, metadata):

            source = meta.get(
                "source",
                "Unknown"
            )

            document_context += (
                f"\nSOURCE: {source}\n"
                f"{doc}\n"
            )

        prompt = f"""
        You are a customer support AI assistant.

        Use both the conversation history
        and the retrieved documents.

        Conversation History:

        {conversation_context}

        Knowledge Base:

        {document_context}

        Current User Question:

        {message}

        If information comes from a document,
        mention the source document.
        """
        answer = ask_gemini_with_context(prompt)

        self.repository.create(db=db, session_id=session_id, user_message=message, ai_response=answer)

        print("\n=== DOCUMENT SOURCES ===")
        print(metadata)

        print("\n=== DOCUMENT COUNT ===")
        print(len(documents))

        return answer
