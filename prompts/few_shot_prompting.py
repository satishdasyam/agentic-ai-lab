import os
from dotenv import load_dotenv
from openai import OpenAI

# In Few shot prompting model is given few examples before asking the actual question.

env_path = r'/home/satish/.env'
load_dotenv(dotenv_path=env_path)

api_key = os.getenv('GEMINI_API_KEY')

SYSTEM_PROMPT = """ You are specialised in only maths. Any prompt related to other topics should be responded with 'I am sorry, I can only assist with math-related queries.'

Rule: Strictly follow output format in json

{}

Examples:
Q: What is 2 + 2?
A: {output: "2 + 2 is equal to 4."}

Q: what is 2 * 4?
A: {output: "2 * 4 is equal to 8."}

"""

client = OpenAI(api_key=api_key,
                base_url="https://generativelanguage.googleapis.com/v1beta/openai/",)
response = client.chat.completions.create(
    model="gemini-3.5-flash",
    messages=[
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": "What is 4+4"}
    ]
)

print(response.choices[0].message.content)