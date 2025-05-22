```python
# utils/llm.py

import os
import requests
from dotenv import load_dotenv

# Load API key and strip whitespace/newlines and any leading '='
load_dotenv()
API_KEY = os.getenv("GEMINI_API_KEY", "").strip().lstrip('=')

BASE_URL = (
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
        r = requests.post(BASE_URL, json=payload, timeout=10)
        r.raise_for_status()
        return r.json()["candidates"][0].get("content", "").strip()
    except Exception as e:
        return f"LLM Error: {str(e)}"
```
