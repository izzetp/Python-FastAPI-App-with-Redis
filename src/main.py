from fastapi import FastAPI
import redis
import os
from urllib.parse import urlparse
import requests

app = FastAPI()

# Parse a single REDIS_URL (e.g. redis://redis:6379)
redis_url = os.getenv("REDIS_URL", "redis://localhost:6379")
parsed = urlparse(redis_url)
r = redis.Redis(host=parsed.hostname, port=parsed.port, decode_responses=True)

@app.get("/")
def root():
    return {"message": "FastAPI with Redis is working!"}

@app.get("/weather/{city}")
def get_weather(city: str):
    if r.exists(city):
        return {"source": "cache", "data": r.get(city)}
    response = requests.get(f"https://wttr.in/{city}?format=3")
    r.setex(city, 60, response.text)
    return {"source": "api", "data": response.text}
