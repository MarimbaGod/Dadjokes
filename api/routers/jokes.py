from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
import os
import requests
# import openai
from elevenlabs import set_api_key, generate, play

# class JokeResponse(BaseModel):
#     joke: str
#     audioUrl: str

router = APIRouter()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
ELEVENLABS_API_KEY = os.getenv("ELEVENLABS_API_KEY")

# openai.api_key = OPENAI_API_KEY
set_api_key(ELEVENLABS_API_KEY)


@router.get("/api/joke")
async def get_joke():
    try:
        #API Call to OpenAI
        # MODEL = "gpt-3.5-turbo"
        # user_messages = [
        #     {"role": "system", "content": "You are a helpful assistant."},
        #     {"role": "user", "content": "Tell me a good Dad Joke."},
        #     {"role": "user", "content": "Give me a funny joke."},
        #     {"role": "user", "content": "Share a humorous joke with me."},
        # ]
        # joke_response = openai.ChatCompletion.create(
        #     model=MODEL,
        #     messages=user_messages,
        #     temperature=0.9,
        # )
        # # cleans up joke text
        # joke = joke_response.choices[0].message['content']
        # cleaned_joke = joke.replace("\n", " ")
        cleaned_joke = "Sure, here's a classic Dad joke for you:  Why don't skeletons fight each other?  Because they don't have the guts!"
        # ElevenLabs TTS
        # tts_url = "https://api.elevenlabs.io/synthesize"
        # headers = {"Authorization": f"Bearer {ELEVENLABS_API_KEY}"}
        # payload = {"text": joke}
        # audio_response = requests.post(tts_url, headers=headers, json=payload)

        # audioUrl = audio_response.json()["audioUrl"]
        audio = generate(
            text=cleaned_joke,
            voice="Bella",
            model="eleven_multilingual_v2"
        )
        play(audio)
        # return JokeResponse(joke=joke, audioUrl=audioUrl)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
