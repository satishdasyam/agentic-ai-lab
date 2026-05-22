import os
from dotenv import load_dotenv
from openai import OpenAI

env_path = r'/home/satish/.env'
load_dotenv(dotenv_path=env_path)

api_key = os.getenv('GEMINI_API_KEY')

client = OpenAI(api_key=api_key,
                base_url="https://generativelanguage.googleapis.com/v1beta/openai/",)
response = client.chat.completions.create(
    model="gemini-3.5-flash",
    messages=[
        {"role": "system", "content": "You are specialised in only maths. Any prompt related to other topics should be responded with 'I am sorry, I can only assist with math-related queries.'"},
        {"role": "user", "content": "Whats the weather today?"}
    ]
)

print(response.choices[0].message.content)