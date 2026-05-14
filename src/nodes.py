from src.state import AssistantState


BLOCKED_KEYWORDS = {"hack", "malware"}


def input_guard(state: AssistantState) -> AssistantState:
    lowered = state.get("user_input", "").lower()
    if any(keyword in lowered for keyword in BLOCKED_KEYWORDS):
        state["error"] = "Input blocked by guard."
        state["route"] = "error"
    return state


def router(state: AssistantState) -> AssistantState:
    if not state.get("error"):
        state["route"] = "tool_agent"
    return state


def tool_agent(state: AssistantState) -> AssistantState:
    if state.get("error"):
        return state
    cleaned_input = state.get("user_input", "").strip()
    state["draft"] = f"Draft response for: {cleaned_input}"
    return state


def quality_check(state: AssistantState) -> AssistantState:
    if state.get("error"):
        return state
    state["final_answer"] = state.get("draft", "")
    return state
