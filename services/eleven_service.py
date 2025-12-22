import requests
import os
import base64
from dotenv import load_dotenv

load_dotenv()

ELEVEN_API_KEY = os.getenv("ELEVEN_API_KEY")  
VOICE_ID = os.getenv("VOICE_ID", "VOICE_ID")

def text_to_speech(text: str)-> str:
    url = f"https://api.elevenlabs.io/v1/text-to-speech/{VOICE_ID}"

    headers = {
        "Accept": "audio/mpeg",
        "xi-api-key": ELEVEN_API_KEY,
        "Content-Type": "application/json"
    }

    data = {
        "text": text,
        "model_id":"eleven_monolingual_v2",
        "voice_settings":{
            "stability":0.7,"similarity_boost":0.8
        }
    }

    try:
        response = requests.post(url, json=data,headers=headers)
        response.raise_for_status()
        audio_bytes = response.content
        return base64.b64encode(audio_bytes).decode('utf-8')
    except Exception as e:
        print(f"TTS Error: {e}")
        return ""
