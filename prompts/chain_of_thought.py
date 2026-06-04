import os
from dotenv import load_dotenv
from openai import OpenAI

# In Few shot prompting model is given few examples before asking the actual question.

env_path = r'/home/satish/.env'
load_dotenv(dotenv_path=env_path)

api_key = os.getenv('GEMINI_API_KEY')

SYSTEM_PROMPT = """ 
You are an expert in solving user queries using chain of thought prompting.
You will break down the problem into smaller steps and solve it step by step.
You will have INPUT and that you PLAN and planning can be done in multiple steps and once you are done with plan you can give the final answer in OUTPUT.

Examples:

INPUT: What is 2 + 2*4/2-1?
PLAN: To solve this problem, we can break it down into the following steps:
PLAN: To solve this we use BODMAS rule.
PLAN: First we solve the multiplication and division from left to right.
PLAN: Doing multiplication 2*4 = 8
PLAN: Next dividing 8/2 = 4
PLAN: Now we solve the addition and subtraction from left to right.
PLAN: 2 + 4 = 6
PLAN: 6 - 1 = 5
OUTPUT: The answer is 5.

"""

input_text = input(">  ") # "What is 2 + (2*4)/2*5-1?"

client = OpenAI(api_key=api_key,
                base_url="https://generativelanguage.googleapis.com/v1beta/openai/",)
response = client.chat.completions.create(
    model="gemini-3.5-flash",
    messages=[
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": input_text}
    ]
)

print(response.choices[0].message.content)