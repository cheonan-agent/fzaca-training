# 도전 — app/config.py
import os
from dotenv import load_dotenv

load_dotenv()

MODEL_NAME = os.getenv("MODEL_NAME", "gpt-6-luna")
MAX_TOKENS = int(os.getenv("MAX_TOKENS", "500"))