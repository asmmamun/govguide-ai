from src.llm.llm import generate

def main():
    prompt = "দণ্ড কত প্রকার ও কী কী?"
    answer = generate(prompt)
    print(answer)

if __name__ == "__main__":
    main()
