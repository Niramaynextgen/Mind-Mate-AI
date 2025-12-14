import os
import json
from google.oauth2 import service_account
from google.cloud import firestore
from datetime import datetime

# Load Firebase values from .env
FIREBASE_PROJECT_ID = os.getenv("FIREBASE_PROJECT_ID")
FIREBASE_CLIENT_EMAIL = os.getenv("FIREBASE_CLIENT_EMAIL")
FIREBASE_PRIVATE_KEY = os.getenv("FIREBASE_PRIVATE_KEY")

# Fix private key formatting (required)
FIREBASE_PRIVATE_KEY = FIREBASE_PRIVATE_KEY.replace("\\n", "\n")

# Create service account dictionary
service_account_info = {
    "type": "service_account",
    "project_id": FIREBASE_PROJECT_ID,
    "private_key_id": "dummy_key_id",
    "private_key": FIREBASE_PRIVATE_KEY,
    "client_email": FIREBASE_CLIENT_EMAIL,
    "client_id": "dummy_client_id",
    "auth_uri": "https://accounts.google.com/o/oauth2/auth",
    "token_uri": "https://oauth2.googleapis.com/token",
    "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
    "client_x509_cert_url": ""
}

credentials = service_account.Credentials.from_service_account_info(service_account_info)
db = firestore.Client(credentials=credentials, project=FIREBASE_PROJECT_ID)

def save_chat(user_id: str, user_msg: str, ai_reply: str, audio_base64: str = ""):
    try:
        doc_ref = (
            db.collection("users")
            .document(user_id)
            .collection("chats")
            .document()
        )
        doc_ref.set({
            "user_message": user_msg,
            "ai_reply": ai_reply,
            "audio_base64": audio_base64,
            "timestamp": datetime.utcnow()
        })
    except Exception as e:
        print(f"Firestore save error: {e}")
