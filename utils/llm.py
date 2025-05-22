# utils/llm.py

import os
import requests
from dotenv import load_dotenv

# Load & clean API key
load_dotenv()
API_KEY = os.getenv("GEMINI_API_KEY", "").strip().lstrip('=')

# Chat endpoint URL
CHAT_URL = (
    "https://generativelanguage.googleapis.com/v1beta2/"
    "models/chat-bison-001:generateMessage"
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
        resp = requests.post(CHAT_URL, json=payload, timeout=15)
        resp.raise_for_status()
        return resp.json()["candidates"][0]["content"].strip()
    except Exception as e:
        return f"LLM Error: {e}"
