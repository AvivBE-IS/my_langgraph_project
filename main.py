from fastapi import FastAPI
from pydantic import BaseModel

from src.builder import build_graph
from src.state import AssistantState

app = FastAPI(title="LangGraph Boilerplate")
compiled_graph = build_graph()


class ChatRequest(BaseModel):
    user_input: str


@app.get("/health")
def health_check() -> dict[str, str]:
    return {"status": "ok"}


@app.post("/chat")
def chat(payload: ChatRequest) -> AssistantState:
    initial_state: AssistantState = {
        "user_input": payload.user_input,
        "route": "",
        "draft": "",
        "final_answer": "",
        "error": "",
    }
    return compiled_graph.invoke(initial_state)
