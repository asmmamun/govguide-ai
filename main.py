from src.ingestion.loader import load_documents
from src.preprocessing.preprocessor import preprocess_documents
from src.preprocessing.preprocessor import inspect_documents
from src.chunking.chunker import chunk_documents, inspect_chunks
from src.embedding.embedder import Embedder
from src.vector_store.vector_store import VectorStore

def main():
    documents = load_documents("data/raw")

    inspect_documents(documents)

    preprocessed_documents = preprocess_documents(documents)

    inspect_documents(preprocessed_documents)

    chunks = chunk_documents(preprocessed_documents)

    inspect_chunks(chunks)

    embedder = Embedder()
    texts = [chunk["text"] for chunk in chunks]
    embeddings = embedder.encode(texts)
    print(embeddings.shape)

    metadata = []
    for chunk in chunks:
        metadata.append({
            "filename": str(chunk["filename"]),
            "chunk_number": chunk["chunk_number"],
            "text": chunk["text"]
        })

    vector_store = VectorStore(768)
    vector_store.add(embeddings, metadata)
    vector_store.save()
    vector_store.load()
    print(vector_store.index.ntotal)
    
    #vector = vector_store.index.reconstruct(0)
    #print(vector.shape)
    #print(vector[:10])   # First 10 values

if __name__ == "__main__":
    print("Main is running")
    main()
