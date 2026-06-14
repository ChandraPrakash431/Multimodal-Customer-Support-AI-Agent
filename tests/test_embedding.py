from app.documents.embedding_service import (EmbeddingService)


service = EmbeddingService()

vector = service.create_embedding("What is Go?")

print(f"Vector Dimensions: {len(vector)}")

print(vector[:10])
