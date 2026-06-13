import os

from dotenv import load_dotenv

def load_env():
    env_path = r'/home/satish/.env'
    load_dotenv(dotenv_path=env_path)


def get_open_api_key(): 
    load_env()

    api_key = os.getenv('OPEN_AI_API_KEY')
    return api_key

def get_gemini_api_key():
    load_env()

    api_key = os.getenv('GEMINI_API_KEY')
    return api_key