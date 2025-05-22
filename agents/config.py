from dotenv import load_dotenv
from pathlib import Path
from pydantic_settings import BaseSettings, SettingsConfigDict, Field

load_dotenv()   

BASE_DIR = Path(__file__).resolve().parent.parent.parent
DATA_DIR = BASE_DIR / "data"

class Settings(BaseSettings):
    """
    Application settings loaded from environment or .env.

    Attributes:
        openai_api_key (str): API key for OpenAI.
        chroma_collection (str): Name of Chroma collection.
        llm_model (str): LLM model identifier.
        embedding_model (str): Embedding model identifier.
    """
    BINANCE_API_KEY = Field(..., json_schema_extra={"env": "BINANCE_API_KEY"})
    BINANCE_API_SECRET = Field(..., json_schema_extra={"env": "BINANCE_API_SECRET"})
    openai_api_key: str = Field(..., json_schema_extra={"env": "OPENAI_API_KEY"})
    llm_model: str = Field("gpt-4o-mini", json_schema_extra={"env": "LLM_MODEL"})

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

settings = Settings()          # importable partout
DATA_DIR.mkdir(exist_ok=True)