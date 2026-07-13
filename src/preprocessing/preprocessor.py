import random
import re

def inspect_documents(documents):
    for document in documents:
        filename = document['filename']
        character_count = len(document['text'])
        lines = document['text'].splitlines()
        line_count = len(lines)
        
        if len(lines) >= 10:
            start = random.randint(0, len(lines)-10)
            sample = lines[start : start + 10]
        else:
            sample = lines
        
        print("=" * 120)
        print(f"File: {filename}")
        print(f"Characters: {character_count}")
        print(f"Lines: {line_count}\n")

        print("\nFirst 10 lines:")
        print("\n".join(lines[:10]))

        print("\nLast 10 lines:")
        print("\n".join(lines[-10:]))

        print("\nRandom 10 consecutive lines:")
        print("\n".join(sample))
        print("=" * 120)


def normalize_whitespace(text):
    lines = text.splitlines()

    cleaned_lines = []
    for line in lines:
        line = line.strip()
        cleaned_lines.append(line)
    return "\n".join(cleaned_lines)


def preprocess_documents(documents):
    processed_documents = []
    for document in documents:
        new_doc = {
                   "filename": document["filename"],
                   "text": normalize_whitespace(document["text"])
                  }
        processed_documents.append(new_doc)
    return processed_documents
