# 🤖 Agentic AI RAG Chatbot

Developed by **G Rakesh** — AI/ML Engineer (Fresher)

A modern, intelligent chatbot that combines **Retrieval-Augmented Generation (RAG)** with **Agentic AI** capabilities. This chatbot can autonomously decide when to retrieve information from a knowledge base and when to answer directly, providing accurate and context-aware responses.

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![FastAPI](https://img.shields.io/badge/FastAPI-0.104+-green.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

## ✨ Features

- **🤖 Agentic Behavior**: Intelligent decision-making to determine when to retrieve information vs. answer directly
- **📚 RAG Pipeline**: Retrieval-Augmented Generation for accurate, context-aware responses
- **⚡ Fast Search**: FAISS vector database for efficient similarity search
- **💬 Modern UI**: Beautiful, responsive chat interface with message bubbles
- **🔍 Semantic Search**: Uses sentence transformers for intelligent document retrieval
- **🎯 Knowledge Base**: Answers questions based on your custom knowledge base
- **🚀 Fast API**: RESTful API built with FastAPI
- **📱 Responsive Design**: Works seamlessly on desktop and mobile devices

## 🏗️ Architecture

This project demonstrates a production-ready RAG chatbot with the following components:

```
┌─────────────┐
│   Frontend  │  ← Modern chat interface
└──────┬──────┘
       │ HTTP POST
       ▼
┌─────────────┐
│  FastAPI    │  ← Web API server
│   (app.py)  │
└──────┬──────┘
       │
       ▼
┌─────────────┐
│   Agent     │  ← Decision logic (DIRECT vs RETRIEVE)
│  (agent.py) │
└──────┬──────┘
       │
       ├───► DIRECT: Simple greeting response
       │
       └───► RETRIEVE: RAG Pipeline
              │
              ▼
         ┌─────────────┐
         │     RAG     │  ← Retrieve + Generate
         │   (rag.py)  │
         └──────┬──────┘
                │
                ▼
         ┌─────────────┐
         │ FAISS Store │  ← Vector similarity search
         │(vector_store│
         └─────────────┘
```

## 🛠️ Tech Stack

### Backend
- **FastAPI**: Modern, fast web framework for building APIs
- **LangChain**: Framework for LLM applications
- **FAISS**: Vector similarity search library
- **Hugging Face Transformers**: FLAN-T5 model for text generation
- **Sentence Transformers**: For creating embeddings

### Frontend
- **HTML5/CSS3**: Modern, responsive design
- **Vanilla JavaScript**: No framework dependencies
- **Fetch API**: For API communication

## 📋 Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- Git (optional, for cloning)

## 🚀 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/G-Rakesh-7/agentic-ai-rag-chatbot.git
cd agentic-ai-rag-chatbot
```

### 2. Install Dependencies

```bash
cd backend
pip install -r requirements.txt
```

**Note**: First-time installation may take 5-10 minutes as it downloads:
- Language models (FLAN-T5)
- Embedding models (sentence-transformers)
- Other dependencies

### 3. Prepare Your Knowledge Base

Edit `data/docs.txt` with your own content. The current file contains information about:
- Artificial Intelligence (AI)
- Retrieval-Augmented Generation (RAG)
- FAISS
- LangChain
- Agentic AI Systems

## 🎮 Usage

### Starting the Server

```bash
cd backend
python -m uvicorn app:app --reload --host 0.0.0.0 --port 8000
```

The server will start on `http://localhost:8000`

### Accessing the Chatbot

1. **Web Interface**: Open your browser and navigate to:
   - `http://localhost:8000/chat` or
   - `http://localhost:8000/`

2. **API Documentation**: Visit `http://localhost:8000/docs` for interactive API documentation

### Using the Chatbot

1. Type your question in the input field
2. Press **Enter** or click the **Send** button
3. The bot will respond based on its knowledge base

### Example Questions

- **Simple Greetings**: "hi", "hello", "who are you"
- **About AI**: "What is AI?", "Explain Artificial Intelligence"
- **About RAG**: "What is RAG?", "How does RAG work?"
- **About FAISS**: "What is FAISS?", "Tell me about FAISS"
- **About LangChain**: "What is LangChain?", "Explain LangChain"
- **About Agentic AI**: "What is Agentic AI?", "How do Agentic AI systems work?"

## 📁 Project Structure

```
agentic-ai-rag-chatbot/
├── backend/
│   ├── app.py              # FastAPI application & routes
│   ├── agent.py            # Agentic decision logic
│   ├── rag.py              # RAG pipeline (retrieve + generate)
│   ├── vector_store.py     # FAISS vector database setup
│   └── requirements.txt    # Python dependencies
├── data/
│   └── docs.txt            # Knowledge base documents
├── frontend/
│   ├── index.html          # Chat interface
│   ├── script.js           # Frontend JavaScript
│   └── style.css           # Styling
└── README.md               # This file
```

## 🔌 API Endpoints

### POST `/chat`

Send a question to the chatbot.

**Request:**
```json
{
  "question": "What is RAG?"
}
```

**Response:**
```json
{
  "answer": "RAG is a technique that combines information retrieval..."
}
```

### GET `/chat` or `/`

Returns the chat interface HTML page.

### GET `/docs`

Interactive API documentation (Swagger UI).

## 🧠 How It Works

### 1. Agentic Decision Making

The agent analyzes each question and decides:
- **DIRECT**: For simple greetings (hi, hello, who are you)
- **RETRIEVE**: For questions requiring knowledge base lookup

### 2. RAG Pipeline (When Retrieval is Needed)

1. **Retrieve**: Searches FAISS vector database for relevant document chunks
2. **Generate**: Builds a prompt with retrieved context + question
3. **Answer**: LLM generates response based on retrieved information

### 3. Vector Store

- Documents are split into chunks (200 characters, 20 overlap)
- Chunks are converted to embeddings using sentence-transformers
- Stored in FAISS for fast similarity search

## 🎨 Features in Detail

### Modern Chat Interface
- Message bubbles for user and bot
- Typing indicator while processing
- Smooth animations
- Responsive design
- Error handling with user-friendly messages

### Agentic Behavior
- Transparent decision-making process
- Rule-based logic (easy to debug and modify)
- Extensible for more complex decision trees

### RAG System
- Reduces hallucinations by grounding in documents
- Fast retrieval with FAISS
- Context-aware responses
- Handles questions outside knowledge base gracefully

## 🔧 Configuration

### Adjusting Chunk Size

Edit `backend/vector_store.py`:
```python
splitter = RecursiveCharacterTextSplitter(
    chunk_size=200,      # Adjust chunk size
    chunk_overlap=20     # Adjust overlap
)
```

### Changing Retrieval Count

Edit `backend/rag.py`:
```python
def retrieve_context(question, k=2):  # Change k value
```

### Modifying Knowledge Base

Simply edit `data/docs.txt` with your content. The vector store will rebuild on server restart.

## 🐛 Troubleshooting

### Server Won't Start
- Ensure Python 3.8+ is installed
- Check if port 8000 is available
- Verify all dependencies are installed

### No Answers from Bot
- Check server logs for errors
- Ensure vector store loaded successfully
- Verify knowledge base file exists at `data/docs.txt`

### Models Not Downloading
- Check internet connection
- Models download automatically on first run
- May take 5-10 minutes depending on connection

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

- **LangChain** for the excellent framework
- **Hugging Face** for pre-trained models
- **Facebook AI Research** for FAISS
- **FastAPI** for the amazing web framework

## 📧 Contact

For questions or support, please open an issue on GitHub.

---

⭐ If you find this project helpful, please give it a star!

## 📚 What I Learned
- Built an end-to-end RAG pipeline from scratch using LangChain and FAISS  
- Understood vector embeddings and semantic retrieval in production-style systems  
- Gained hands-on experience designing Agentic AI decision-making logic  

# agentic-ai-rag-chatbot
