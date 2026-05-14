from langgraph.graph import END, START, StateGraph

from src.nodes import input_guard, quality_check, router, tool_agent
from src.routes import quality_gate, select_route
from src.state import AssistantState


def build_graph():
    graph = StateGraph(AssistantState)

    graph.add_node("input_guard", input_guard)
    graph.add_node("router", router)
    graph.add_node("tool_agent", tool_agent)
    graph.add_node("quality_check", quality_check)

    graph.add_edge(START, "input_guard")
    graph.add_edge("input_guard", "router")

    graph.add_conditional_edges(
        "router",
        select_route,
        {
            "tool_agent": "tool_agent",
            "error": END,
        },
    )

    graph.add_edge("tool_agent", "quality_check")
    graph.add_conditional_edges(
        "quality_check",
        quality_gate,
        {
            "tool_agent": "tool_agent",
            "error": END,
            "end": END,
        },
    )

    return graph.compile()
