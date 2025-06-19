from fastapi import FastAPI
from urls import register_routes

app = FastAPI(title="FastAPI SSE Example")

register_routes(app)
