# utils/llm.py

import os
import requests
from dotenv import load_dotenv

# Load API key and strip whitespace/newlines
load_dotenv()
API_KEY = os.getenv("GEMINI_API_KEY", "").strip()

BASE_URL = "https://generativelanguage.googleapis.com/v1beta2/models/chat-bison-001:generateMessage"

def generate_response(prompt: str) -> str:
    try:
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {API_KEY}"
        }
        payload = {
            "prompt": {
                "messages": [
                    {"author": "user", "content": prompt}
                ]
            }
        }
        r = requests.post(BASE_URL, headers=headers, json=payload, timeout=10)
        r.raise_for_status()
        candidate = r.json()["candidates"][0]
        return candidate.get("content", "").strip()
    except Exception as e:
        return f"LLM Error: {str(e)}"
