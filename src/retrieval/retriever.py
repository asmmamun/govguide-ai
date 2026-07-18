class Retriever:
    def __init__(self, embedder, vector_store):
        self.embedder = embedder
        self.vector_store = vector_store

    def retrieve(self, query, k):
        query_embedding = self.embedder.encode(query)
        query_embedding = query_embedding.reshape(1, -1)
        distances, indices = self.vector_store.search(query_embedding, k)
        result = []
        for index, distance in zip(indices[0], distances[0]):
            result.append({'filename' : self.vector_store.metadata[index]['filename'],
                'chunk_number' : self.vector_store.metadata[index]['chunk_number'],
                'score' : distance,
                'text' : self.vector_store.metadata[index]['text']
               })
        return result
