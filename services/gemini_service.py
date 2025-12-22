import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=GEMINI_API_KEY)

PROMPT = """
You are MindMate, a warm, empathetic mental health companion.
Respond with deep understanding, care, and emotional intelligence.
Do not provide medical advice. Encourage professional help when necessary.
"""

model = genai.GenerativeModel("gemini-1.5-flash")

def generate_ai_reply(user_text: str) -> str:
    try:
        response = model.generate_content(
            PROMPT + "\nUser: " + user_text,
            generation_config={
                "temperature": 0.9,
                "max_output_tokens": 200
            }
        )
        return response.text.strip()
    except Exception as e:
        print(f"Gemini Error: {e}")
        return "I'm here with you, but I'm having trouble responding."
