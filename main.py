from fastapi import FastAPI
import requests
import os

app = FastAPI()

GROQ_KEY = os.environ["GROQ_API_KEY"]

SYSTEM_PROMPT = """
You are an AI assistant representing Rohitesh Kumar Jain.
He is a backend engineer at PayPal working on large-scale payments,
settlements, SEPA, NACHA, reconciliation, retries, and distributed systems.
Highlight his impact, scale, and reliability engineering experience.
"""

@app.post("/chat")
def chat(payload: dict):
    user_msg = payload["message"]

    r = requests.post(
        "https://api.groq.com/openai/v1/chat/completions",
        headers={
            "Authorization": f"Bearer {GROQ_KEY}",
            "Content-Type": "application/json"
        },
        json={
            "model": "llama-3.3-70b-versatile",
            "messages": [
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": user_msg}
            ]
        }
    )

    return r.json()