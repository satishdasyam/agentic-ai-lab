import os
from google import genai
from dotenv import load_dotenv

env_path = r'/home/satish/.env'
load_dotenv(dotenv_path=env_path)
pi_key = os.getenv('GEMINI_API_KEY')

client = genai.Client()

response = client.models.generate_content(
    model="gemini-3.5-flash",
    contents="Explain how AI works in a few words",
)

print(response.text)