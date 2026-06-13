
from common_code import get_open_api_key
from langchain_openai import OpenAIEmbeddings
from langchain_qdrant import QdrantVectorStore

from openai import OpenAI


embedding_model = OpenAIEmbeddings(model="text-embedding-3-large", api_key=get_open_api_key())
vector_db = QdrantVectorStore.from_existing_collection(url="http://localhost:6333",
                                  collection_name="ayushman_bharat_rag",
                                  embedding=embedding_model,
                        )
def process_query(user_query:str):
    print("Searching Chunks", user_query)
    
    search_results = vector_db.similarity_search(query=user_query)

    context = "\n\n\n".join(
    f"page_number: {result.metadata['page_label']}\n page_content: {result.page_content}\n file_location:{result.metadata['source']}"
    for result in search_results
    )

    #print(f"Context: {context}")

    SYSTEM_PROMPT = """You are a helpful assistant. Answer the user query from the context you  got from the pdf file along with page_number and page_content and file_location. 

    You should also give page number asking him to navigate to that page to know more.

    If you don't know the answer, say you don't know.

    Context:${context}"""


    client = OpenAI(api_key=get_open_api_key())
    response = client.chat.completions.create(
        model="gpt-5-mini",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": user_query}
        ]
    )
    print(f"🤖: {response.choices[0].message.content}")
    return response.choices[0].message.content