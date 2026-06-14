import os

from dotenv import load_dotenv

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

DATABASE_URL = os.getenv("DATABASE_URL")

if not GEMINI_API_KEY:
    raise ValueError("GEMINI_API_KEY not found")

if not DATABASE_URL:
    raise ValueError("DATABASE_URL not found")
