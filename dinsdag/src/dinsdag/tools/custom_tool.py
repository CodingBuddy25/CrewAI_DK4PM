from crewai.tools import BaseTool
from typing import Type
from pydantic import BaseModel, Field
import os
from langchain_openai import ChatOpenAI
from .prompts4tools import choosing_approach_prompt
class choosing_approach_inputs(BaseModel):
    """This tool helps to choose which abstraction method will be chosen for the csvs"""
    focus: str

class choosing_approach_tool(BaseTool):
    name: str = "choosing_approach"
    description: str = (
        """Choose an abstraction type based on the focus of the user input"""
    )
    args_schema: Type[BaseModel] = choosing_approach_inputs

    def _run(self, focus: str) -> str:
        model = ChatOpenAI(temperature=0, model_name="gpt-4o-mini")
        formatted_prompt = choosing_approach_prompt + focus
        response = model.invoke(formatted_prompt)
        print("the response is:", response.content)
        return response.content



    def _arun(self, question: str):
        raise NotImplementedError("Async not supported.")