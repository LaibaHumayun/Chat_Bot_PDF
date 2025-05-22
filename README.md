# PDF Chatbot

A Retrieval-Augmented Generation (RAG) chatbot application that allows users to upload PDF documents and chat with them using natural language.

## 📋 Table of Contents

- [Overview](#overview)
- [Architecture](#architecture)
- [Features](#features)
- [Setup Instructions](#setup-instructions)
  - [Prerequisites](#prerequisites)
  - [Local Development](#local-development)
  - [Docker Deployment](#docker-deployment)
  - [Environment Variables](#environment-variables)
- [API Documentation](#api-documentation)
- [Usage Guide](#usage-guide)
- [Project Structure](#project-structure)
- [Technologies Used](#technologies-used)
- [Future Improvements](#future-improvements)

## 🔍 Overview

The PDF Chatbot is an application that uses state-of-the-art language models and document processing to enable natural language conversations with the content of PDF documents. The system extracts text from uploaded PDFs, splits it into manageable chunks, creates vector embeddings, and uses a retrieval-augmented generation (RAG) approach to answer user queries based on the document content.

## 🏗️ Architecture

```
┌─────────────┐     ┌───────────────┐     ┌─────────────────────┐
│ Web Frontend│────▶│ FastAPI       │────▶│ PDF Processing      │
│ (HTML/JS)   │     │ Backend       │     │ (PyPDF2)            │
└─────────────┘     └───────────────┘     └─────────────────────┘
                            │                        │
                            ▼                        ▼
                    ┌───────────────┐     ┌─────────────────────┐
                    │ Vector Store  │     │ Text Chunking       │
                    │ (FAISS)       │◀───▶│ (LangChain)         │
                    └───────────────┘     └─────────────────────┘
                            │                        ▲
                            ▼                        │
                    ┌───────────────┐     ┌─────────────────────┐
                    │ RAG System    │────▶│ OpenAI API          │
                    │ (LangChain)   │     │ (GPT-3.5/4)         │
                    └───────────────┘     └─────────────────────┘
```

The application follows a RAG-based architecture:
1. **Document Upload & Processing**: PDFs are uploaded, processed, and text is extracted
2. **Text Chunking & Embedding**: Document text is split into chunks and converted to vector embeddings
3. **Vector Storage**: Embeddings are stored in a FAISS vector database for efficient similarity search
4. **Query Processing**: User questions are processed to find the most relevant document sections
5. **Response Generation**: Relevant context is sent to an LLM with the user's question to generate accurate answers

## ✨ Features

- **PDF Document Upload**: Drag-and-drop interface for easy PDF uploads
- **Conversation Interface**: Clean, chat-like UI for interacting with document content
- **Source Citations**: Responses include citations to the source material within the document
- **Context Awareness**: The system maintains conversation history to provide more relevant answers
- **Document Management**: Users can view, chat with, and delete uploaded documents

## 🚀 Setup Instructions

### Prerequisites

- Python 3.10 or higher
- An OpenAI API key for embeddings and completions

### Local Development

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/pdf-chatbot.git
   cd pdf-chatbot
   ```

2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Create a `.env` file in the project root:
   ```
   OPENAI_API_KEY=your_openai_api_key
   LLM_MODEL=gpt-3.5-turbo  # or gpt-4 if you have access
   ```

5. Run the application:
   ```bash
   uvicorn main:app --reload
   ```

6. Open `http://localhost:8000` in your browser

### Docker Deployment

1. Build the Docker image:
   ```bash
   docker build -t pdf-chatbot .
   ```

2. Run the container:
   ```bash
   docker run -p 8000:8000 -e OPENAI_API_KEY=your_openai_api_key pdf-chatbot
   ```

3. Access the application at `http://localhost:8000`

### Environment Variables

| Variable | Description | Default |
|----------|-------------|---------|
| `OPENAI_API_KEY` | Your OpenAI API key | None (Required) |
| `LLM_MODEL` | The OpenAI model to use | gpt-3.5-turbo |

## 📚 API Documentation

### Document API

- **POST** `/api/documents/upload`
  - Upload a PDF document
  - Body: multipart/form-data with 'file' field containing PDF
  - Response: `{"document_id": "uuid", "filename": "name.pdf", "status": "processing"}`

- **GET** `/api/documents/list`
  - List all uploaded documents
  - Response: `{"documents": [{"document_id": "uuid", "filename": "name.pdf", "status": "processed"}]}`

- **DELETE** `/api/documents/{document_id}`
  - Delete a specific document
  - Response: `{"status": "success", "message": "Document deleted"}`

### Chat API

- **POST** `/api/chat/message`
  - Send a message to the chatbot
  - Body: `{"message": "your question", "document_id": "uuid", "conversation_id": "optional-uuid"}`
  - Response: `{"response": "answer text", "sources": [...], "conversation_id": "uuid"}`

- **GET** `/api/chat/history/{conversation_id}`
  - Get chat history for a conversation
  - Response: `[{"role": "user", "content": "message", "timestamp": "ISO date"}, ...]`

## 📱 Usage Guide

### Uploading Documents

1. Navigate to the main page
2. Drag and drop a PDF file onto the upload area, or click to browse
3. Click "Upload Document" and wait for processing to complete

### Chatting with Documents

1. From the main page, find your document in the list
2. Click "Chat with this document"
3. In the chat interface, type your question about the document content
4. View the AI's response and the source citations in the sidebar

## 📂 Project Structure

```
/app
  /api             # FastAPI routes
  /models          # Pydantic data models
  /services        # Business logic services
  /static          # Frontend assets
    /css           # Stylesheets
    /js            # JavaScript files
  /templates       # HTML templates
/uploads           # Storage for uploaded PDFs
/vector_store      # FAISS vector database files
main.py            # Application entry point
requirements.txt   # Python dependencies
Dockerfile         # Container configuration
```

## 🛠️ Technologies Used

- **Backend**: FastAPI, Python 3.10+
- **PDF Processing**: PyPDF2
- **NLP & LLM**: LangChain, OpenAI API
- **Vector Storage**: FAISS
- **Frontend**: HTML, CSS, JavaScript, Bootstrap
- **Containerization**: Docker

## 🔮 Future Improvements

- Add user authentication and document access control
- Support additional document formats (DOCX, TXT, etc.)
- Implement batched processing for large documents
- Add custom training capabilities for domain-specific knowledge
- Improve error handling and recovery mechanisms
- Add document preview functionality
- Enable document content search separate from chat
- Support offline LLMs for self-hosted deployment 