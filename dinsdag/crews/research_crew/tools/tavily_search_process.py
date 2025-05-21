from crewai.tools import BaseTool
from typing import Type
from pydantic import BaseModel

import os

from langchain_community.tools.tavily_search import TavilySearchResults


class tavily_tool_inputs(BaseModel):
    """uses tavily to search the internet"""
    prompt_DK_process: str

class tavily_search_process(BaseTool):
    name: str = "Tavily search tool"
    description: str = (
        """uses tavily to search the internet""")
    args_schema: Type[BaseModel] = tavily_tool_inputs

    def _run(self, prompt_DK_process:str):
        TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")
        research = TavilySearchResults(api_key=TAVILY_API_KEY, max_results=10)
        try:
            #from the example in https://medium.com/@venugopal.adep/building-an-ai-research-pipeline-with-crewai-and-langchain-a013a627824f
            results = research.invoke(prompt_DK_process)

            formatted_results = ""
            for res in results:
                formatted_results += f"Source: {res.get('url', 'No URL')}\n"
                formatted_results += f"Title: {res.get('title', 'No Title')}\n"
                formatted_results += f"Content: {res.get('content', 'No Content')}\n\n"

            print("THE RESULTS ISSSSSS:", formatted_results, "\n RETREVTIOETNE$R#W$ORCTSEO*SUTS$*UCT SGOER")
            return formatted_results if formatted_results else "No results found."
        except Exception as e:
            return f"Error searching the internet: {str(e)}"

    def _arun(self, question: str):
        raise NotImplementedError("Async not supported.")