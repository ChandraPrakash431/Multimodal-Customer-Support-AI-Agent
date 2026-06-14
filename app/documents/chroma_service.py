import chromadb


class ChromaService:

    def __init__(self):

        self.client = chromadb.PersistentClient(
            path="./chroma_db"
        )

        self.collection = (
            self.client.get_or_create_collection(
                name="documents"
            )
        )

    def add_chunk(self, chunk_id: str, text: str, embedding: list[float]):

        self.collection.add(ids=[chunk_id], documents=[text], embeddings=[embedding])

    def search(self, embedding: list[float], top_k: int = 3):

        return self.collection.query(query_embeddings=[embedding], n_results=top_k)