import os
from dotenv import load_dotenv
from openai import OpenAI

env_path = r'/home/satish/.env'
load_dotenv(dotenv_path=env_path)

api_key = os.getenv('OPEN_AI_API_KEY')

client = OpenAI(api_key=api_key)
response = client.chat.completions.create(
    model="gpt-5-nano",
    messages=[
        #{"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Hello! How can you assist me today?"}
    ]
)

print(response.choices[0].message)