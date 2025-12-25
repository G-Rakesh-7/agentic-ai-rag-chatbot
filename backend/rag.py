"""
rag.py

This file handles:
1. Retrieving relevant chunks from FAISS
2. Building a grounded prompt
3. Generating an answer using an LLM
"""

from transformers import pipeline
from vector_store import load_vector_store

# Load vector store ONCE (important for performance)
vector_store = load_vector_store()

# Load LLM
# WHY FLAN-T5?
# - Instruction-tuned
# - Lightweight
# - Good for RAG-style QA
llm = pipeline(
    "text2text-generation",
    model="google/flan-t5-base",
    max_new_tokens=150
)


def retrieve_context(question, k=2):
    """
    Retrieves top-k relevant chunks from FAISS.
    """
    docs = vector_store.similarity_search(question, k=k)
    return "\n\n".join([doc.page_content for doc in docs])


def build_prompt(context, question):
    """
    Builds a grounded prompt.
    WHY:
    - Prevent hallucinations
    - Force LLM to answer only from retrieved data
    """
    return f"""
You are an AI assistant.
Answer the question using ONLY the context below.
If the answer is not in the context, say "I don't know".

Context:
{context}

Question:
{question}

Answer:
"""


def rag_answer(question):
    """
    Full RAG pipeline:
    Question → Retrieve → Prompt → LLM → Answer
    """
    context = retrieve_context(question)
    prompt = build_prompt(context, question)
    response = llm(prompt)

    return response[0]["generated_text"]
