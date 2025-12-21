import base64
from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

from model.chat_model import ChatMessage, ChatResponse  
from services.gemini_service import generate_ai_reply
from services.eleven_service import text_to_speech
from services.firestore_service import save_chat

app = FastAPI(title="MindMate")

# CORS configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",
        "https://ai-mindmate.netlify.app"
    ],  
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/mindmate", response_model=ChatResponse)
async def mindmate_chat(request: ChatMessage):
    # Check if user sent empty message
    if not request.text.strip():
        raise HTTPException(status_code=400, detail="Message cannot be empty")

    # 1️⃣ Gemini AI call with error handling
    try:
        ai_reply = generate_ai_reply(request.text)
    except Exception as e:
        ai_reply = "AI service is temporarily unavailable. Please try later."

    # 2️⃣ ElevenLabs TTS call with error handling
    audio_bytes = None
    if ai_reply.strip():
        try:
            audio_bytes = text_to_speech(ai_reply)
        except Exception as e:
            audio_bytes = None

    # 3️⃣ Safe Base64 encoding
    audio_base64 = "" if audio_bytes is None else base64.b64encode(audio_bytes).decode("utf-8")

    # 4️⃣ Save chat to Firestore
    try:
        save_chat(request.user_id, request.text, ai_reply)
    except Exception as e:
        # optional: log error, do not break response
        pass

    return ChatResponse(ai_reply=ai_reply, audio_base64=audio_base64)

@app.get("/")
async def root():
    return {"message": "MindMate API is running 💙"}

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
