# utils/llm.py

import os
from google import genai
from dotenv import load_dotenv

# Load & configure API key
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY", "").strip()
genai.configure(api_key=api_key)

MODEL = "gemini-pro"  # or "gemini-1.5-pro" if you have access

def generate_response(prompt: str) -> str:
    try:
        model = genai.GenerativeModel(model_name=MODEL)
        response = model.generate_content(prompt)
        return response.text.strip()
    except Exception as e:
        return f"LLM Error: {e}"
