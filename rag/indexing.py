import os

from pathlib import Path
from dotenv import load_dotenv
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_qdrant import QdrantVectorStore

env_path = r'/home/satish/.env'
load_dotenv(dotenv_path=env_path)

api_key = os.getenv('OPEN_AI_API_KEY')

pdf_path = Path(__file__).parent.parent/"AyushmanBharat.pdf"
print(pdf_path)

pdf_loader = PyPDFLoader(file_path=str(pdf_path))
documents = pdf_loader.load()

print(f"Number of documents: {len(documents)}")
print(f"Document content: {documents[0].page_content[:100]}...")

# Split the documents into smaller chunks

text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
chunks = text_splitter.split_documents(documents = documents)

print(f"Number of chunks: {len(chunks)}")


# We need vector embeddings

embedding_model = OpenAIEmbeddings(model="text-embedding-3-large", api_key=api_key)

vector_store = QdrantVectorStore.from_documents(documents=chunks,
                                                 embedding=embedding_model, 
                                                 url="http://localhost:6333",
                                                 collection_name="ayushman_bharat_rag")
print("Documents have been embedded and stored in Qdrant vector database.")