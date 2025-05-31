from crewai.tools import BaseTool
import os
from pydantic import BaseModel
from typing import Type


from langchain_community.tools.tavily_search import TavilySearchResults

class tavily_search_basic_inputs(BaseModel):
    """uses tavily to search the internet"""
    prompt_causes_agent: str

class tavily_search_basic(BaseTool):
    """Uses tavily to searc the internet"""
    name: str = "Tavily search tool basic"
    description: str = ("""uses tavily to search the internet""")
    args_schema: Type[BaseModel] = tavily_search_basic_inputs

    def _run(self, prompt_causes_agent):
        TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")
        research = TavilySearchResults(api_key=TAVILY_API_KEY, max_results=10)
        #can increase the max results
        try:
            #from the example in https://medium.com/@venugopal.adep/building-an-ai-research-pipeline-with-crewai-and-langchain-a013a627824f
            results = research.invoke(prompt_causes_agent)

            formatted_results = ""
            for res in results:
                formatted_results += f"Source: {res.get('url', 'No URL')}\n"
                formatted_results += f"Title: {res.get('title', 'No Title')}\n"
                formatted_results += f"Content: {res.get('content', 'No Content')}\n\n"

            return formatted_results if formatted_results else "No results found."
        except Exception as e:
            return f"Error searching the internet: {str(e)}"
