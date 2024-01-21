from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
import os
import requests
# from openai import OpenAI
# from elevenlabs import set_api_key, generate, play
import openai
from io import BytesIO

class JokeResponse(BaseModel):
    joke: str
    audio_base64: str


router = APIRouter()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
ELEVENLABS_API_KEY = os.getenv("ELEVENLABS_API_KEY")

# openai.api_key = OPENAI_API_KEY
# set_api_key(ELEVENLABS_API_KEY)


@router.get("/api/joke")
async def get_joke():
    try:
        #API Call to OpenAI
        MODEL = "gpt-3.5-turbo"
        user_messages = [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": "Tell me a good Dad Joke."},
            {"role": "user", "content": "Give me a funny joke."},
            {"role": "user", "content": "Share a humorous joke with me."},
        ]
        joke_response = openai.ChatCompletion.create(
            model=MODEL,
            messages=user_messages,
            temperature=0.9,
        )
        # # cleans up joke text
        joke = joke_response.choices[0].message['content']
        cleaned_joke = joke.replace("\n", " ")

        # Use OpenAI TTS instead
        # audio_response = openai.Audio.speech.create(
        #     model="tts-1",
        #     voice="onyx",
        #     input=cleaned_joke
        # )

        # audio_bytes = BytesIO()
        # audio_response.stream_to_file(audio_bytes)
        # audio_bytes.seek(0)
        # audio_base64 = base64.b64encode(audio_bytes.read()).decode("utf-8")

        return JokeResponse(joke=cleaned_joke, audio_base64=audio_base64)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
