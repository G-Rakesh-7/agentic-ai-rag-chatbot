"""
vector_store.py

This file is responsible for:
1. Loading documents (knowledge base)
2. Splitting them into chunks
3. Converting chunks into embeddings
4. Storing them in FAISS for fast similarity search
"""

from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS


def load_vector_store():
    """
    This function builds the FAISS vector database.
    It is called ONCE when the backend starts.
    """

    # STEP 1: Load documents
    # WHY: RAG answers should come ONLY from known data
    loader = TextLoader("../data/docs.txt")
    documents = loader.load()

    # STEP 2: Chunk documents
    # WHY: Smaller chunks improve retrieval accuracy
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=200,      # small enough for LLM context
        chunk_overlap=20     # prevents context loss
    )
    chunks = splitter.split_documents(documents)

    # STEP 3: Create embeddings
    # WHY: FAISS works on vectors, not raw text
    embedding_model = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    # STEP 4: Store embeddings in FAISS
    vector_store = FAISS.from_documents(chunks, embedding_model)

    return vector_store
