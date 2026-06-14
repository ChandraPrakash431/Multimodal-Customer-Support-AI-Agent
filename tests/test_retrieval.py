from app.documents.embedding_service import (EmbeddingService)

from app.documents.chroma_service import (ChromaService)


embedding_service = (EmbeddingService())

chroma = ChromaService()


question = ("How does Go handle concurrency?")

query_embedding = (
    embedding_service.create_embedding(
        question
    )
)

results = chroma.search(embedding=query_embedding, top_k=3)

print("\nRESULTS:\n")

for document in results["documents"][0]:

    print("=" * 80)

    print(document[:500])

    print()
