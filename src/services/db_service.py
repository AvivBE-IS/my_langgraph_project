from pathlib import Path

import chromadb
from sqlalchemy import create_engine
from sqlalchemy.engine import Engine

from src.config import get_settings


def get_chroma_client() -> chromadb.PersistentClient:
    settings = get_settings()
    Path(settings.chroma_persist_dir).mkdir(parents=True, exist_ok=True)
    return chromadb.PersistentClient(path=settings.chroma_persist_dir)


def get_sqlite_engine() -> Engine:
    settings = get_settings()
    db_path = settings.sqlite_url.replace("sqlite:///", "")
    Path(db_path).parent.mkdir(parents=True, exist_ok=True)
    return create_engine(settings.sqlite_url, future=True)
