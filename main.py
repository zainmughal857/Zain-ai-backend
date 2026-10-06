import os
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from openai import OpenAI

app = FastAPI(title="ZAIN AI Media Manager Backend")

origins = os.getenv(
    "ALLOWED_ORIGINS",
    "https://zainmughal857.github.io"
).split(",")

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")
OPENAI_MODEL = os.getenv("OPENAI_MODEL", "gpt-5-mini")

client = OpenAI(api_key=OPENAI_API_KEY) if OPENAI_API_KEY else None


class ChatRequest(BaseModel):
    message: str


class ContentRequest(BaseModel):
    topic: str
    platform: str = "Facebook"
    tone: str = "professional"


@app.get("/")
def home():
    return {
        "status": "online",
        "service": "ZAIN AI Media Manager Backend"
    }


@app.get("/health")
def health():
    return {"status": "healthy"}


@app.post("/api/ai/chat")
def ai_chat(request: ChatRequest):
    if not client:
        raise HTTPException(
            status_code=500,
            detail="OPENAI_API_KEY is not configured"
        )

    try:
        response = client.responses.create(
            model=OPENAI_MODEL,
            input=request.message
        )

        return {
            "success": True,
            "reply": response.output_text
        }

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )


@app.post("/api/ai/content")
def create_content(request: ContentRequest):
    if not client:
        raise HTTPException(
            status_code=500,
            detail="OPENAI_API_KEY is not configured"
        )

    prompt = f"""
Create professional social media content.

Topic: {request.topic}
Platform: {request.platform}
Tone: {request.tone}

Give:
1. Catchy title
2. Main post/caption
3. Short description
4. Relevant hashtags
5. Call to action
"""

    try:
        response = client.responses.create(
            model=OPENAI_MODEL,
            input=prompt
        )

        return {
            "success": True,
            "content": response.output_text
        }

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )
