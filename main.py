from src.ingestion.loader import load_documents
from src.preprocessing.preprocessor import preprocess_documents
from src.preprocessing.preprocessor import inspect_documents
from src.chunking.chunker import chunk_documents, inspect_chunks

def main():
    documents = load_documents("data/raw")

    inspect_documents(documents)

    preprocessed_documents = preprocess_documents(documents)

    inspect_documents(preprocessed_documents)

    chunks = chunk_documents(preprocessed_documents)

    inspect_chunks(chunks)

if __name__ == "__main__":
    print("Main is running")
    main()
