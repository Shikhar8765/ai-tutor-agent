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
    errors = []

    # 1) Try chat endpoint
    try:
        resp = genai.chat.completions.create(
            model="chat-bison-001",
            messages=[{"author": "user", "content": prompt}]
        )
        return resp.choices[0].message.content.strip()
    except Exception as e:
        errors.append(f"chat: {str(e)}")

    # 2) Fallback to text completion
    try:
        resp = genai.generate_text(
            model="text-bison-001",
            prompt=prompt,
            temperature=0.2,
            max_output_tokens=512
        )
        return getattr(resp, "text", getattr(resp, "content", str(resp)))
    except Exception as e:
        errors.append(f"text: {str(e)}")

    # 3) Final fallback
    return f"LLM Error: {' | '.join(errors)}"
