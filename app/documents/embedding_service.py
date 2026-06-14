from app.gemini_client import (generate_embedding)


class EmbeddingService:

    def create_embedding(self, text: str) -> list[float]:

        return generate_embedding(text)
