# SupportAI Assistant 🤖

A professional, full-stack RAG (Retrieval-Augmented Generation) customer support system built to deliver context-aware, accurate responses from a custom knowledge base.

## 🚀 Features
* **Intelligent Retrieval**: Powered by LangChain and Google Gemini, ensuring answers are grounded in your specific documentation.
* **Vector-Based Search**: Uses ChromaDB to perform semantic searches, providing highly relevant support answers.
* **Full-Stack Connectivity**: Seamless integration between a responsive React frontend and a robust FastAPI backend.
* **Modern Architecture**: Designed for performance and maintainability in an engineering context.

## 🛠️ Tech Stack
* **Frontend**: React, JavaScript (ES6+), CSS3
* **Backend**: FastAPI, Python 3.13+
* **AI/LLM**: LangChain, Google Generative AI (Gemini 3.5 Flash)
* **Vector Database**: ChromaDB
* **Development Tools**: VS Code, Git

## ⚙️ Setup Instructions

### 1. Clone the Repository
```bash
git clone [https://github.com/yourusername/rag-customer-support.git](https://github.com/yourusername/rag-customer-support.git)
cd rag-customer-support

## backend setup : Navigate to the backend directory and set up your environment:

cd backend
# Create and activate virtual environment
python -m venv venv
.\venv\Scripts\activate  # Windows
source venv/bin/activate  # macOS/Linux

# Install dependencies
pip install -r requirements.txt

# Run the API server
uvicorn main:app --reload

## frontend setup : In a new terminal window, navigate to the frontend directory:

cd ../frontend
# Install required packages
npm install

# Launch the application
npm start

## Usage

1.Ensure your knowledge_base.txt is updated in the backend/ folder.

2.Open http://localhost:3000 in your web browser.

3.Enter your query (e.g., "What is your refund policy?") and click Ask to receive an AI-generated response based on your custom data.


## Project Structure

/backend: Contains the FastAPI server (main.py), the RAG logic, and document loading scripts.

/frontend: Contains the React application for the user interface.

.gitignore: Ensures sensitive files and large dependency folders are excluded from GitHub.

## Project Notes

This project was developed to explore Retrieval-Augmented Generation (RAG) pipelines in real-world support scenarios. It demonstrates the integration of semantic search with large language models to reduce hallucinations and provide trustworthy information.

Built with professional design and technical rigor.

