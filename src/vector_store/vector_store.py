import json
import faiss


class VectorStore:
    def __init__(self, dimension):
        self.index = faiss.IndexFlatIP(dimension)
        self.index_path = "data/vector_store/faiss_index.bin"
        self.metadata_path = "data/vector_store/chunk_metadata.json"
        self.metadata = []

    def add(self, embeddings, metadata):
        self.index.add(embeddings)
        self.metadata = metadata

    def save(self):
        # Save FAISS index
        faiss.write_index(self.index, self.index_path)

        # Save metadata
        with open(self.metadata_path, "w", encoding="utf-8") as f:
            json.dump(self.metadata, f, ensure_ascii=False, indent=4)

    def load(self):
        # Load FAISS index
        self.index = faiss.read_index(self.index_path)

        # Load metadata
        with open(self.metadata_path, "r", encoding="utf-8") as f:
            self.metadata = json.load(f)

    def search(self, query_embedding, k=5):
        distances, indices = self.index.search(query_embedding, k)
        return distances, indices
