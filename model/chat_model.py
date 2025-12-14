from pydantic import BaseModel
from typing import Optional

class ChatMessage(BaseModel):
    user_id:str
    text:str

class ChatResponse(BaseModel):
    reply:str
    audio_base64: str
    