import time
import logfire
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from app.config import settings

BATCH_SIZE = 50
_GEMINI_DIM = 3072
_FALLBACK_DIM = 768     # All-mpnet-base-v2

_active_model = None
_model_type : str | None = None # Gemini or Fallback


def _probe_gemini():
    """Try one embed call to see if Gemini is available., Returns True if Gemini is available, False otherwise."""



def load_fallback():
    """Load the fallback embedding model."""

    return

def _get_embeddings_model():
    """Get the embeddings model, either Gemini or fallback."""

    return


def _embed_batch(batch: list[str]) -> list[list[float]]:
    """Embed a batch of texts using the active model."""

    return


def embed_query(query: str) -> list[float]:
    """Embed a single query string."""

    return