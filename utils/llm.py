# utils/llm.py

import os
from google import genai
from dotenv import load_dotenv

# Load API key
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

# Initialize the GenAI client
client = genai.Client(api_key=api_key)

def generate_response(prompt: str) -> str:
    try:
        # Generate content with a Gemini model
        response = client.models.generate_content(
            model="gemini-2.0-flash",    # or "gemini-pro" if enabled for your project
            contents=[prompt]
        )
        return response.text
    except Exception as e:
        return f"LLM Error: {str(e)}"
