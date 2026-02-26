from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
import httpx
import os
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

WOLFRAM_APP_ID = os.getenv("WOLFRAM_APP_ID")

@app.get("/")
def root():
    return {"message": "Hoppi backend is alive."}

@app.get("/wolfram")
async def query_wolfram(query: str = Query(...)):
    url = "https://api.wolframalpha.com/v1/result"

    params = {
        "appid": WOLFRAM_APP_ID,
        "i": query
    }

    async with httpx.AsyncClient() as client:
        response = await client.get(url, params=params)

    if response.status_code != 200:
        return {"error": "Wolfram request failed"}
    return {"result": response.text}    