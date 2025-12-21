from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import base64
import io
from gtts import gTTS

app = FastAPI()

class MindMateRequest(BaseModel):
    user_id: str
    text: str

class MindMateResponse(BaseModel):
    reply: str
    audio_base64: str

@app.post("/mindmate", response_model=MindMateResponse)
async def mindmate(req: MindMateRequest):
    try:
        # 1️⃣ AI / chatbot reply (dummy for now)
        reply_text = f"Hello {req.user_id}, you said: {req.text}"

        # 2️⃣ TEXT → SPEECH (IMPORTANT FIX)
        tts = gTTS(text=reply_text, lang="en")

        audio_buffer = io.BytesIO()
        tts.write_to_fp(audio_buffer)   # ✅ writes BYTES
        audio_buffer.seek(0)

        audio_bytes = audio_buffer.read()  # ✅ bytes
        audio_base64 = base64.b64encode(audio_bytes).decode("utf-8")

        return {
            "reply": reply_text,
            "audio_base64": audio_base64
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"TTS error: {str(e)}")

@app.get("/")
def root():
    return {"status": "MindMate API running"}
