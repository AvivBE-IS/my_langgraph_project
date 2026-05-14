from fastapi import FastAPI

from src.builder import build_graph
from src.state import AssistantState

app = FastAPI(title="LangGraph Boilerplate")
compiled_graph = build_graph()


@app.get("/health")
def health_check() -> dict[str, str]:
    return {"status": "ok"}


@app.post("/chat")
def chat(payload: dict[str, str]) -> AssistantState:
    initial_state: AssistantState = {
        "user_input": payload.get("user_input", ""),
        "route": "",
        "draft": "",
        "final_answer": "",
        "error": "",
    }
    return compiled_graph.invoke(initial_state)
