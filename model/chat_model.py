from pydantic import BaseModel
from typing import Optional

class ChatMessage(BaseModel):
    user_id: str
    text: str

class ChatResponse(BaseModel):
    ai_reply: str
    audio_base64: Optional[str] = None
