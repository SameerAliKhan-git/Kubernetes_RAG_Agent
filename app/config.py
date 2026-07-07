import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    # Groq Reasoning Engine (Llama 3.3)
    GROQ_API_KEY = os.getenv("GROQ_API_KEY")
    GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

    QDRANT_API_KEY = os.getenv("QDRANT_API_KEY")
    QDRANT_URL = os.getenv("QDRANT_CLUSTER_ENDPOINT")

    QDRANT_COLLECTION = "enterprize_RAG"


    GROQ_MODEL = "llama-3.3-70b-versatile"
    GEMINI_MODEL = "gemini-2.5-flash-13b"


settings = Settings()
