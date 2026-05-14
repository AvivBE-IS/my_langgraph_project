from src.state import AssistantState


def select_route(state: AssistantState) -> str:
    if state.get("error"):
        return "error"
    if state.get("route"):
        return state["route"]
    return "tool_agent"


def quality_gate(state: AssistantState) -> str:
    if state.get("error"):
        return "error"
    if state.get("final_answer"):
        return "end"
    return "tool_agent"
