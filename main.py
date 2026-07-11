from src.ingestion.loader import load_documents
from src.preprocessing.preprocessor import preprocess_documents
print("Main is running")

documents = load_documents("data/raw")
preprocessed_docs = preprocess_documents(documents)

