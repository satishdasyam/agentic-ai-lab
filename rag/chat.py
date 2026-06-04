# Retreival Augmented Generation (RAG) Chatbot Implementation

import os

from dotenv import load_dotenv
from langchain_openai import OpenAIEmbeddings
from langchain_qdrant import QdrantVectorStore

from openai import OpenAI

env_path = r'/home/satish/.env'
load_dotenv(dotenv_path=env_path)

api_key = os.getenv('OPEN_AI_API_KEY')

user_query = input("Ask something: ")


embedding_model = OpenAIEmbeddings(model="text-embedding-3-large", api_key=api_key)
vector_db = QdrantVectorStore.from_existing_collection(url="http://localhost:6333",
                                  collection_name="ayushman_bharat_rag",
                                  embedding=embedding_model,
                        )

#Relevant chunks from the vector database based on the user query
search_results = vector_db.similarity_search(query=user_query)

#print(f"Search results: {search_results}")

# Using a list comprehension inside .join()
context = "\n\n\n".join(
    f"page_number: {result.metadata['page_label']}\n page_content: {result.page_content}\n file_location:{result.metadata['source']}"
    for result in search_results
)

#print(f"Context: {context}")

SYSTEM_PROMPT = """You are a helpful assistant. Answer the user query from the context you  got from the pdf file along with page_number and page_content and file_location. 

You should also give page number asking him to navigate to that page to know more.

If you don't know the answer, say you don't know.

Context:${context}"""


client = OpenAI(api_key=api_key)
response = client.chat.completions.create(
    model="gpt-5-mini",
    messages=[
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": user_query}
    ]
)

print(f"Response: {response.choices[0].message.content}")