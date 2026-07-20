from src.embedding.embedder import Embedder
from src.vector_store.vector_store import VectorStore
from src.retrieval.retriever import Retriever
from src.prompting.prompt_builder import build_prompt
from src.llm.llm import generate

def main():
    query = input("Write your question please: ")
    embedder = Embedder()
    vector_store = VectorStore(dimension=384)
    vector_store.load()
    retriever = Retriever(embedder, vector_store)
    results = retriever.retrieve(query, k=3)
    texts = []
    for result in results:
        text = result["text"]
        texts.append(text)
    context = "\n\n-------------------\n\n".join(texts)

    prompt = (build_prompt(context, query))
    
    response = generate(prompt)
    print(response)

if __name__ == "__main__":
    main()
