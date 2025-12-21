import base64
from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from  model.chat_model import ChatMessage, ChatResponse  
from services.gemini_service import generate_ai_reply
from services.eleven_service import text_to_speech
from services.firestore_service import save_chat

app = FastAPI(title="MindMate")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000",
        "https://mind-mate-ai-production-51a0.up.railway.app"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/mindmate",response_model=ChatResponse)
async def mindmate_chat(request:ChatMessage):
    if not request.text.strip():
        raise HTTPException(status_code=400, detail="Message cannot be empty")
    
    ai_reply = generate_ai_reply(request.text)

    audio_bytes = text_to_speech(ai_reply)

    audio_base64 = base64.b64encode(audio_bytes).decode("utf-8")

    save_chat(request.user_id, request.text, ai_reply)

    return ChatResponse(ai_reply=ai_reply, audio_base64=audio_base64)


# @app.get("/")
# async def root():
#     return {"message":"MindMate Backend is running 💙"}
# if __name__ == "__main__":
#     uvicorn.run("main:app",host="0.0.0.0",port=8000,reload=True)
    
@app.post("/mindmate")
async def mindmate_chat(request: ChatMessage):
    return {
        "ai_reply": "Backend working perfectly",
        "audio_base64": ""
    }
