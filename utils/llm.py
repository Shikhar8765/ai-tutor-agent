# utils/llm.py

import os
import requests
from dotenv import load_dotenv

# Load and clean the API key
load_dotenv()
API_KEY = os.getenv("GEMINI_API_KEY", "").strip()

# Append the key as a query param
BASE_URL = (
    "https://generativelanguage.googleapis.com/"
    "v1beta2/models/chat-bison-001:generateMessage"
    f"?key={API_KEY}"
)

def generate_response(prompt: str) -> str:
    try:
        payload = {
            "prompt": {
                "messages": [
                    {"author": "user", "content": prompt}
                ]
            }
        }
        r = requests.post(BASE_URL, json=payload, timeout=10)
        r.raise_for_status()
        return r.json()["candidates"][0]["content"].strip()
    except Exception as e:
        return f"LLM Error: {str(e)}"
