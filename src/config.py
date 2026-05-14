import os
from dataclasses import dataclass


@dataclass(frozen=True)
class Settings:
    app_name: str = os.getenv("APP_NAME", "LangGraph Boilerplate")
    app_env: str = os.getenv("APP_ENV", "development")
    ollama_base_url: str = os.getenv("OLLAMA_BASE_URL", "http://localhost:11434")
    ollama_model: str = os.getenv("OLLAMA_MODEL", "llama3.1")
    chroma_persist_dir: str = os.getenv("CHROMA_PERSIST_DIR", "./data/chroma")
    sqlite_url: str = os.getenv("SQLITE_URL", "sqlite:///./data/app.db")


def get_settings() -> Settings:
    return Settings()
