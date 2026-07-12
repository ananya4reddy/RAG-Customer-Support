import os
import logging
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from langchain_community.document_loaders import TextLoader
from langchain_community.vectorstores import Chroma
from langchain_google_genai import ChatGoogleGenerativeAI, GoogleGenerativeAIEmbeddings
from langchain_core.prompts import ChatPromptTemplate
from langchain_classic.chains import create_retrieval_chain
from langchain_classic.chains.combine_documents import create_stuff_documents_chain

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)



app = FastAPI(title="Gemini RAG Support API")

# Professional CORS configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize RAG Pipeline
try:
    logger.info("Loading documents...")
    loader = TextLoader("knowledge_base.txt")
    docs = loader.load()
    
    # Using the latest supported embedding model
    embeddings = GoogleGenerativeAIEmbeddings(model="gemini-embedding-2-preview")
    vectorstore = Chroma.from_documents(docs, embeddings)
    
    # Using the stable Gemini 1.5 Flash
    llm = ChatGoogleGenerativeAI(model="gemini-3.5-flash")
    
    prompt = ChatPromptTemplate.from_template("""
    Answer the question based only on the following context:
    {context}
    
    Question: {input}
    """)
    
    combine_docs_chain = create_stuff_documents_chain(llm, prompt)
    retrieval_chain = create_retrieval_chain(vectorstore.as_retriever(), combine_docs_chain)
    logger.info("Gemini RAG pipeline initialized successfully!")
except Exception as e:
    logger.error(f"Initialization error: {e}")

@app.get("/ask")
async def ask_question(query: str):
    try:
        response = retrieval_chain.invoke({"input": query})
        return {"answer": response["answer"]}
    except Exception as e:
        logger.error(f"Query error: {e}")
        raise HTTPException(status_code=500, detail="Internal AI Processing Error")
    
    