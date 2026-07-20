class Retriever:
    def __init__(self, embedder, vector_store):
        self.embedder = embedder
        self.vector_store = vector_store

    def retrieve(self, query: str, k: int = 3) -> list:
        query_embedding = self.embedder.encode(query)
        query_embedding = query_embedding.reshape(1, -1)
        distances, indices = self.vector_store.search(query_embedding, k)
        result = []
        for chunk_idx, distance in zip(indices[0], distances[0]):
            result.append({'filename' : self.vector_store.metadata[chunk_idx]['filename'],
                'chunk_number' : self.vector_store.metadata[chunk_idx]['chunk_number'],
                'score' : distance,
                'text' : self.vector_store.metadata[chunk_idx]['text']
               })
        return result
