from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
import os
import requests
# from openai import OpenAI
import openai
import random

class JokeResponse(BaseModel):
    joke: str

def get_random_prompt():
    prompts = [
        "Can you share a dad joke I haven't heard?",
        "Surprise me with a clever Dad joke!",
        "Tell me a joke about birds",
        "I need a laugh",
        "I need a knock knock joke",
        "I need a dad joke",
        "I need a dad joke about food",
        "I need a comically bad joke to tell my wife",
        "I need a dad joke to tell my coworker",
        "I just need a joke to say to a stranger at the dog park so I can tell them their dog pooped without feeling awkward"
    ]
    return random.choice(prompts)

router = APIRouter()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

@router.get("/api/joke")
async def get_joke():
    try:
        #API Call to OpenAI
        MODEL = "gpt-3.5-turbo"
        user_messages = [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": get_random_prompt()},
        ]
        joke_response = openai.ChatCompletion.create(
            model=MODEL,
            messages=user_messages,
            temperature=0.9,
        )
        # # cleans up joke text
        joke = joke_response.choices[0].message['content'].strip()

        return JokeResponse(joke=joke)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
