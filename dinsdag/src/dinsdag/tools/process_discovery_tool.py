from crewai.tools import tool
import os

@tool
def process_analysis_tool(focus:str, company: str, process:str, filename:str) -> str:
    """Clear description for what this tool is useful for, your agent will need this information to use it."""
    # Function logic here
    return "Result from your custom tool"
