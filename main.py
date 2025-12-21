# backend/main.py

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

# ---------------------------
# CORS SETTINGS
# ---------------------------
origins = [
    "http://localhost:3000",  # your frontend during development
    "https://your-frontend-domain.com",  # replace with deployed frontend domain
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # can use ["*"] for testing only
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ---------------------------
# DATA MODEL
# ---------------------------
class MindMateRequest(BaseModel):
    message: str

class MindMateResponse(BaseModel):
    reply: str

# ---------------------------
# API ENDPOINT
# ---------------------------
@app.post("/mindmate", response_model=MindMateResponse)
async def mindmate_endpoint(request: MindMateRequest):
    user_message = request.message
    # Your processing logic here, e.g., AI/BERT response
    response_text = f"You said: {user_message}"  # placeholder logic
    return MindMateResponse(reply=response_text)

# ---------------------------
# OPTIONAL ROOT ENDPOINT
# ---------------------------
@app.get("/")
async def root():
    return {"message": "MindMate API is running"}
