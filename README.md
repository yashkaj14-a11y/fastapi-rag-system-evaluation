# ⚡ Production-Grade RAG System with Evaluation Harness

An enterprise-ready Retrieval-Augmented Generation (RAG) system built with **FastAPI**, **Streamlit**, and **Groq LLM**. Features dynamic API key handling to ensure total credential security and zero-hardcoding risks.

## 🚀 Key Features

* **Dynamic Credentials Management:** Accepts user-provided API keys at runtime via a password-masked UI, eliminating key leaks.
* **Evaluation Harness:** Benchmark and measure RAG response accuracy and retrieval precision.
* **Interactive Dashboard:** Modern Streamlit frontend built for low-latency query handling and seamless interaction.
* **Modular Backend Architecture:** Easily extendable to integrate vector databases (ChromaDB, FAISS, Pinecone) and custom embeddings.

## 🛠️ Tech Stack

* **Language:** Python 3.10+
* **Frontend:** Streamlit
* **API / LLM Integration:** Groq API
* **Environment Security:** `python-dotenv` & `.gitignore` standards

## 📥 Local Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/your-username/fastapi-rag-system-evaluation.git](https://github.com/your-username/fastapi-rag-system-evaluation.git)
   cd fastapi-rag-system-evaluation
