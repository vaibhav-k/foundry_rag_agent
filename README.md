# Foundry RAG Agent

A modular Retrieval-Augmented Generation (RAG) system built using:

- Azure AI Foundry
- Azure AI Search
- Azure OpenAI (via Foundry)
- Python SDK (azure-ai-projects)

---

## 🚀 Features

- Azure AI Search-powered RAG
- Streaming responses
- Citation support
- Modular architecture
- Auto agent creation & cleanup
- Multi-turn chat support

---

## 🏗️ Architecture
main.py

├── client.py → Azure Foundry client

├── search_connection.py → connection resolver

├── agent_service.py → agent lifecycle

├── chat_service.py → streaming chat

└── config.py → configuration


---

## ⚙️ Setup

### 1. Clone repo

```
git clone https://github.com/vaibhav-k/foundry_rag_agent.git

cd foundry_rag_agent
```

---

### 2. Create virtual environment

```
python -m venv venv
venv\Scripts\activate # Windows
```

---

### 3. Install dependencies

```
pip install -r requirements.txt
```

---

### 4. Configure environment

Create `.env` file:

```
PROJECT_ENDPOINT=your_endpoint

SEARCH_CONNECTION_NAME=your_connection

SEARCH_INDEX_NAME=your_index
```

---

### 5. Login to Azure


az login


---

### 6. Run the app


python main.py


---

## 💬 Usage

- Type a question
- Get grounded answers from Azure AI Search
- Citations included automatically
- Type `exit` to quit

---

## 🔐 Security Notes

- Do NOT commit `.env`
- Do NOT commit Azure subscription IDs
- Use Azure CLI or Managed Identity for authentication
- Keep secrets in environment variables

---

## 🧹 Cleanup behavior

Each run:
- creates a temporary agent
- deletes it after session ends

---

## 📦 Requirements

- Python 3.10+
- Azure CLI logged in
- Access to Azure AI Foundry project
- Azure AI Search connection configured
