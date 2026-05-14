from typing import TypedDict


class AssistantState(TypedDict):
    user_input: str
    route: str
    draft: str
    final_answer: str
    error: str
