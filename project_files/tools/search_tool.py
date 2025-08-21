from langchain_community.tools import DuckDuckGoSearchRun

def search_web_ddg(query: str) -> list[dict]:
    """Search the web using DuckDuckGo and return a list of results."""
    search_tool = DuckDuckGoSearchRun()
    results = search_tool.invoke(query)
    return results