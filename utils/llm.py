# utils/llm.py

import os
import google.generativeai as genai
from dotenv import load_dotenv

# 1) Load & clean API key
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY", "").strip()
genai.configure(api_key=api_key)

# 2) Pick a model you have access to (e.g., "gemini-2.0-flash" or "gemini-pro")
MODEL = "gemini-2.0-flash"

def generate_response(prompt: str) -> str:
    try:
        # Use the chat API under the hood
        response = genai.chat.completions.create(
            model=MODEL,
            messages=[{"author": "user", "content": prompt}]
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"LLM Error: {e}"
