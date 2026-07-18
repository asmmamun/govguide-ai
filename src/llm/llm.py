import ollama

def generate(prompt: str, model: str = "qwen3:8b") -> str:
    """
    Generate a response from the given prompt using the specified LLM.

    Args:
        prompt: The prompt to send to the language model.
        model: The Ollama model to use for generation.

    Returns:
        The generated response as a string.
    """
    try:
        # Generate the response
        response = ollama.chat(
          model=model,
          messages=[
            {
                'role': 'user',
                'content': prompt,
            },
        ],
    )

        # Extract and return the text response
        answer = response['message']['content']
        return answer

    except Exception:
        raise
