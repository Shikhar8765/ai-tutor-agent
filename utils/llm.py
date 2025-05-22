# utils/llm.py

import os
import google.generativeai as genai
from dotenv import load_dotenv

# Load API key from .env
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

# Configure the Gemini API key
genai.configure(api_key=api_key)

def generate_response(prompt: str) -> str:
    try:
        response = genai.chat.completions.create(
            model="chat-bison-001",
            messages=[{"author": "user", "content": prompt}]
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"LLM Error: {str(e)}"
