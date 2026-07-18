from src.retrieval.retriever import Retriever
from src.embedding.embedder import Embedder
from src.vector_store.vector_store import VectorStore

embedder = Embedder()

vector_store = VectorStore(dimension=384)
vector_store.load()

retriever = Retriever(embedder, vector_store)

query = "আপিল করার সময়সীমা কত?"

results = retriever.retrieve(query, k=3)

for result in results:
    print(result)
