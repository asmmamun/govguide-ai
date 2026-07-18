from src.retrieval.retriever import Retriever
from src.embedding.embedder import Embedder
from src.vector_store.vector_store import VectorStore
from src.prompting.prompt_builder import build_prompt

embedder = Embedder()

vector_store = VectorStore(dimension=384)
vector_store.load()

retriever = Retriever(embedder, vector_store)

query = "আপিল করার সময়সীমা কত?"

results = retriever.retrieve(query, k=3)

context_parts = [result["text"] for result in results]
context = "\n\n".join(context_parts)
prompt = build_prompt(context, query)
print(prompt)

