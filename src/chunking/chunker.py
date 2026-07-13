from langchain_text_splitters import RecursiveCharacterTextSplitter

def chunk_documents(documents):
    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=100)

    all_chunks = []
    for doc in documents:
        filename = doc["filename"]
        text = doc["text"]
        text_chunks = splitter.split_text(text)
        for chunk_number, chunk_text in enumerate(text_chunks, start=1):
            indiv_chunk = {"filename": filename, 
                           "chunk_number": chunk_number,
                           "text": chunk_text}
            all_chunks.append(indiv_chunk)
    return all_chunks


def inspect_chunks(chunks, filename=None):
    if not chunks:
        print("No chunks to inspect.")
        return

    if filename is None:
        filename = chunks[0]["filename"]
    document_chunks = [chunk for chunk in chunks if chunk['filename'] == filename]
    total_chunks = len(document_chunks)

    print("=" * 120)
    print(f"File: {filename}")
    print(f"Total chunks: {total_chunks}")
    print("=" * 120)
    print()

    for chunk in document_chunks:
        print(f"\nChunk {chunk['chunk_number']}")
        print(f"Characters: {len(chunk['text'])}")
        print(f"\n{chunk['text']}")
        print("=" * 120)
