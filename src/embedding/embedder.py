from sentence_transformers import SentenceTransformer


class Embedder:
    def __init__(self):
        self.model = SentenceTransformer(
            "intfloat/multilingual-e5-base"
        )

    def encode(self, texts):
        return self.model.encode(
            texts,
            normalize_embeddings=True
        )
