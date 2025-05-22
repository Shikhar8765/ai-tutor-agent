import os
import requests
from dotenv import load_dotenv

# Load API key and strip whitespace/newlines and any leading '='
load_dotenv()
API_KEY = os.getenv("GEMINI_API_KEY", "").strip().lstrip('=')

# REST endpoints with key in URL
CHAT_URL = (
    "https://generativelanguage.googleapis.com/v1beta2/"
    "models/chat-bison-001:generateMessage"
    f"?key={API_KEY}"
)
TEXT_URL = (
    "https://generativelanguage.googleapis.com/v1beta2/"
    "models/text-bison-001:generateText"
    f"?key={API_KEY}"
)

def generate_response(prompt: str) -> str:
    # 1) Try chat endpoint
    try:
        payload = {
            "prompt": {
                "messages": [
                    {"author": "user", "content": prompt}
                ]
            }
        }
        resp = requests.post(CHAT_URL, json=payload, timeout=10)
        resp.raise_for_status()
        return resp.json()["candidates"][0]["content"].strip()
    except requests.HTTPError as err:
        if resp.status_code != 404:
            return f"LLM Error (chat): {err}"
        # else fall back to text
    except Exception:
        # network or other error; fall back to text
        pass

    # 2) Try text endpoint
    try:
        payload = {
            "prompt": {
                "text": prompt
            }
        }
        resp = requests.post(TEXT_URL, json=payload, timeout=10)
        resp.raise_for_status()
        return resp.json()["candidates"][0].get("output", "").strip()
    except Exception as e:
        return f"LLM Error (text): {e}"
