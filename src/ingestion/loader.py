from pathlib import Path

def load_documents(folder_path):
    folder = Path(folder_path)
    files = folder.glob("*.txt")
    texts = []

    for file in files:
        with open(file, encoding='utf-8') as doc:
            text = doc.read()
            texts.append({"filename": file, "text":text})
    return texts

if __name__ == "__main__":
    documents = load_documents("data/raw")
    print(documents[0]["filename"])
