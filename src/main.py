from fastapi import FastAPI
import redis
import requests
import os

app = FASTAPI()

redis_host = os.getenv("REDIS_HOST", "redis")
