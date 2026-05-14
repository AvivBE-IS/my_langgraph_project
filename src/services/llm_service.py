from dataclasses import dataclass

from src.config import get_settings


@dataclass
class MockOllama:
    model: str
    base_url: str

    def invoke(self, prompt: str) -> str:
        return f"[MockOllama:{self.model}] {prompt}"


def get_ollama() -> MockOllama:
    settings = get_settings()
    return MockOllama(model=settings.ollama_model, base_url=settings.ollama_base_url)
