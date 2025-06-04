from crewai.tools import tool
import os
from langchain_community.tools.tavily_search import TavilySearchResults
from langchain_openai import ChatOpenAI


@tool
def research_tool(subquestion: str) -> str:
    """Answer subquestions with this tool. Tavily will search the internet for domain knowledge"""
    TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")
    research = TavilySearchResults(api_key=TAVILY_API_KEY, max_results=10)
    # can increase the max results
    try:
        # from the example in https://medium.com/@venugopal.adep/building-an-ai-research-pipeline-with-crewai-and-langchain-a013a627824f
        results = research.invoke(subquestion)

        formatted_results = ""
        for res in results:
            formatted_results += f"Source: {res.get('url', 'No URL')}\n"
            formatted_results += f"Title: {res.get('title', 'No Title')}\n"
            formatted_results += f"Content: {res.get('content', 'No Content')}\n\n"

        print("The result is:", formatted_results, "\n __________________________________________________________")

        if not formatted_results:
            return "No results found."

    except Exception as e:
        return f"Error searching the internet: {str(e)}"

    model = ChatOpenAI(temperature=0, model_name="gpt-4o-mini")
    subquestion_prompt = "answer the {subquestion} as well as possible. Use the results of the internet search: {formatted_results}. Provide a logical and clear answer. Make sure the references style is adequate and that everything is fully referenced"
    formatted_prompt = subquestion_prompt.format(subquestion=subquestion, formatted_results=formatted_results)
    response = model.invoke(formatted_prompt)
    response = response.content
    return response