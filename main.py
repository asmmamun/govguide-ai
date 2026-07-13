from src.ingestion.loader import load_documents
from src.preprocessing.preprocessor import preprocess_documents
from src.preprocessing.preprocessor import inspect_documents
print("Main is running")

documents = load_documents("data/raw")
inspect_documents(documents)
preprocessed_docs = preprocess_documents(documents)
inspect_documents(preprocessed_docs)
