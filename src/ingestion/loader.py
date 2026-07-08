from pathlib import Path

def load_documents():
    folder = Path("data/raw")
    files = folder.glob("*.txt")
    texts = []

    for file in files:
        with open(file, encoding='utf-8') as doc:
            text = doc.read()
            texts.append({"filename": file, "text":text})
    return texts

documents = load_documents()
print(documents[0]["filename"])
