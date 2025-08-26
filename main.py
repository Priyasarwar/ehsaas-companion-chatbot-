import pandas as pd
import os
import requests
from fastapi import FastAPI
from pydantic import BaseModel
from datetime import datetime


# --- FastAPI app ---
app = FastAPI()

# --- Ollama setup ---
OLLAMA_API_URL = "http://127.0.0.1:11434/api/generate"
OLLAMA_MODEL = "gemma3n:e2b"

SYSTEM_PROMPT = (
    "You are an empathetic chatbot. Reply in 2-3 short, kind sentences. "
    "Be warm, supportive, and natural. "
    "Always vary your wording, tone, and style in each reply so the conversation feels fresh. "
    "Do not reuse the same sentence structure, phrasing, or closing line in multiple replies. "
    "Sometimes ask a gentle question, sometimes give reassurance, sometimes share a positive thought. "
    "Keep it empathetic, but avoid sounding formulaic or repetitive."
)

class UserInput(BaseModel):
    message: str

@app.post("/chat")
async def chat(input: UserInput):
    # Send prompt to Ollama
    payload = {
        "model": OLLAMA_MODEL,
        "prompt": f"{SYSTEM_PROMPT}\nUser: {input.message}\nChatbot:",
        "stream": False  # important so we get a full JSON response
    }

    try:
        r = requests.post(OLLAMA_API_URL, json=payload)
        r.raise_for_status()
        response_text = r.json()["response"]
    except Exception as e:
        response_text = f" Error contacting model: {str(e)}"

    # Store conversation in CSV
    store_conversation(input.message, response_text)

    return {"response": response_text}


def store_conversation(user_input, bot_response):
    os.makedirs("data", exist_ok=True)
    file_path = "data/conversation_history.csv"

    chat_id = datetime.now().strftime("%Y%m%d%H%M%S")

    df = pd.DataFrame([
        [datetime.now().strftime("%Y-%m-%d %H:%M"), "User", user_input, chat_id],
        [datetime.now().strftime("%Y-%m-%d %H:%M"), "Bot", bot_response, chat_id]
    ], columns=["Timestamp", "Role", "Message", "ChatID"])

    df.to_csv(file_path, mode="a", header=not os.path.exists(file_path), index=False)
