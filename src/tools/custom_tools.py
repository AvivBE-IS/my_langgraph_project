from langchain.tools import tool


@tool
def mock_search_tool(query: str) -> str:
    """Mock tool that returns a static answer."""
    return f"Mock result for query: {query}"


def get_tools():
    return [mock_search_tool]
