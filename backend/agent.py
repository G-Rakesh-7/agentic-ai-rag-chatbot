"""
agent.py

This file adds AGENTIC behavior.
The agent decides:
- Should I retrieve information?
- Or answer directly?
"""

from rag import rag_answer


def agent_decision(question):
    """
    Simple rule-based decision logic.
    WHY rule-based?
    - Transparent
    - Easy to debug
    - Interview-friendly
    """
    simple_queries = ["hi", "hello", "who are you"]

    q = question.lower()
    if any(x in q for x in simple_queries):
        return "DIRECT"

    return "RETRIEVE"


def agent_answer(question):
    """
    Controller function.
    This is the 'brain' of the system.
    """
    decision = agent_decision(question)

    if decision == "DIRECT":
        return "Hello! I am an AI assistant powered by Agentic RAG."
    else:
        return rag_answer(question)
