import os
from dotenv import load_dotenv

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
MODEL_NAME = "gemini-2.5-flash"
VECTOR_DB_DIR = "data/cache/vectorstore"
VOICE_PROFILE_PATH = "data/posts_data.csv"