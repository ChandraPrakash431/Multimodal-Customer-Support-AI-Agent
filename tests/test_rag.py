from app.documents.rag_service import (RAGService)


rag = RAGService()

answer = rag.answer_question("How does Go handle concurrency?")

print("\nANSWER:\n")

print(answer)
