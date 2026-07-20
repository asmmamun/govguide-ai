from textwrap import dedent
"""
Prompt builder for the Bangla Government RAG system.

This module is responsible only for constructing prompts.
It does not perform retrieval or call the LLM.
"""
PROMPT_TEMPLATE = dedent("""You are an assistant for answering questions about Bangladesh government rules.

    Context:
    {context}

    Question:
    {question}

Instructions:
- Use ONLY the provided context to answer the question.
- Do not use your own knowledge or make assumptions.
- If the answer is not found in the provided context, reply:
   "প্রদত্ত নথিতে এই তথ্য পাওয়া যায় নি।"
- Respond entirely in Bangla.
- If available, mention the relevant rule (বিধি) number.

Answer:
""")

def build_prompt(context, question):
    """
    Build a prompt for the LLM using the retrieved context and user question.

    Args:
        context: Retrieved document context.
        question: User's question.

    Returns:
        A formatted prompt string ready to send to the LLM.
    """
    return PROMPT_TEMPLATE.format(context=context, question=question,)
