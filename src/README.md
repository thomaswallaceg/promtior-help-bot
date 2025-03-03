# Promtior Helpbot

This project implements a Retrieval-Augmented Generation (RAG) chatbot. It utilizes the following models:

- **LLM**: Llama3 hosted on **Groq**
- **Embeddings**: Cohere-hosted model

## Features

- Retrieval-Augmented Generation (RAG) architecture.
- LangChain for LLM orchestration.
- LangServe for API hosting.
- Streamlit-based frontend.
- Hosted on Railway (https://promtior-help-bot-production.up.railway.app/)

## Setup

### 1. Clone the Repository

```bash
git clone https://github.com/thomaswallaceg/promtior-help-bot.git
cd promtior-help-bot/src
```

### 2. Install Dependencies Using Poetry

```bash
poetry install
```

### 3. Configure API Keys

Create a `.env` file in the project root and add:

```
GROQ_API_KEY=your_groq_api_key
COHERE_API_KEY=your_cohere_api_key
```

### 4. Start the LangServe Backend

```bash
poetry run langchain serve --port 8080
```

### 5. Start the Streamlit Frontend

```bash
poetry run streamlit run app/ui.py --server.port 8081 --server.address 0.0.0.0
```

---

**Author:** [Thomas Wallace]
