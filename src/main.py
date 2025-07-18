from fastapi import FastAPI
import redis
import requests
import os

app = FastAPI()

redis_host = os.getenv("REDIS_HOST", "redis")
redis_port = int(os.getenv("REDIS_PORT", "6379"))
r = redis.Redis(host=redis_host, port=redis_port, decode_responses=True)

@app.get("/weather/{city}")
def get_weather(city: str):
    if r.exists(city):
        return {"source" : "cache", "data" : r.get(city)}

    response = requests.get(f"https://wttr.in/{city}?format=3")
    r.setex(city, 60, response.text)
    return {"source" : "api", "data" : response.text}