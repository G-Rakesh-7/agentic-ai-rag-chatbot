"""
app.py

This file turns your AI logic into a WEB API.
Frontend or any client can call this API.
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from pydantic import BaseModel
from agent import agent_answer
import os

app = FastAPI(title="Agentic AI RAG Chatbot")

# Enable CORS for frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, replace with specific origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class Query(BaseModel):
    question: str


# Serve static files (frontend)
frontend_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "frontend")
if os.path.exists(frontend_path):
    app.mount("/static", StaticFiles(directory=frontend_path), name="static")


@app.get("/")
def root():
    """Root endpoint - serves the chat interface"""
    frontend_file = os.path.join(frontend_path, "index.html")
    if os.path.exists(frontend_file):
        return FileResponse(frontend_file)
    return {"message": "Agentic AI RAG Chatbot API is running!", "docs": "/docs"}


@app.get("/chat")
def chat_get():
    """GET endpoint for /chat - serves the chat interface"""
    frontend_file = os.path.join(frontend_path, "index.html")
    if os.path.exists(frontend_file):
        return FileResponse(frontend_file)
    return {"message": "Please use POST method to send questions", "docs": "/docs"}


@app.post("/chat")
def chat(query: Query):
    """
    API endpoint:
    Input  → user question
    Output → AI answer
    """
    answer = agent_answer(query.question)
    return {"answer": answer}
