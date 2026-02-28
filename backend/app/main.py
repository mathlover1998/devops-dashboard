from fastapi import FastAPI
from contextlib import asynccontextmanager

@asynccontextmanager
async def lifespan(app:FastAPI):
    print("Starting application...")
    yield
    print("Closing application...")

app = FastAPI(
    title="Real-time Devops Dashboard",
    version = "0.1.0",
    lifespan = lifespan
)

@app.get("health")
async def health():
    return {"status": "ok"}