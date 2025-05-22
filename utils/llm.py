# utils/llm.py

import os
from google import genai
from dotenv import load_dotenv

# Load & clean API key
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY", "").strip()
client = genai.Client(api_key=api_key)

# Choose a Gemini model you have access to:
MODEL = "gemini-2.0-flash"

def generate_response(prompt: str) -> str:
    try:
        # Use the generate_content endpoint
        response = client.models.generate_content(
            model=MODEL,
            contents=[prompt]
        )
        return response.text.strip()
    except Exception as e:
        return f"LLM Error: {e}"
