# app/main.py
import logging

from fastapi import FastAPI

from app.routers import memos

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(name)s - %(message)s")

app = FastAPI(title="사내 규정 도우미 API", version="0.1.0")
app.include_router(memos.router)


@app.get("/health")
def health():
    return {"status": "ok"}