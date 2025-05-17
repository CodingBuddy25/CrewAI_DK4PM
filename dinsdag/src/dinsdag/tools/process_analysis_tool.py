from crewai.tools import BaseTool
from typing import Type
from pydantic import BaseModel

from langchain_openai import ChatOpenAI

from .prompts4tools import process_analysis_prompt
class process_analysis_tool_inputs(BaseModel):
    """Analyses the process with an LLM call, it will return the most important elements for the specific prompt"""
    chosen_approach:str
    focus: str
    process: str
    abstraction: str

#Finish this!! Check the prompt and whether the code could work. Also, check the choosing_approach method again becasue I dont think that it is returning just DFG or temporal etc.
class process_analysis_tool(BaseTool):
    name: str = "process analysis"
    description: str = (
        """Analyses the process with an LLM call, it will return the most important elements for the specific prompt"""
    )
    args_schema: Type[BaseModel] = process_analysis_tool_inputs

    def _run(self, chosen_approach:str, focus:str, process:str,abstraction: str) -> str:
        # To Improve!
        analyse_model = {"DFG": "Common Paths: Look for nodes with high incoming or outgoing edges"
                                ", Loops and Rework: Detect cycles that may suggest rework",
                         'Temporal Profile': "Activity Durations: identify slow steps,"
                                             " Waiting Times: Analyze the time between activities to detect waiting periods"
                                             " or delays, Variability: Look for inconsistencies in timing that may indicate "
                                             "process instability.",
                         "Variants": "Frequency of Variants: Identify which variants are most common and which are rare"
                                     "Performance Differences: Compare variants to see which are less efficient, "}
        model = ChatOpenAI(temperature=0, model_name="gpt-4o-mini")
        model_analysis = analyse_model[chosen_approach]

        formatted_prompt = process_analysis_prompt.format(focus=focus, model=chosen_approach,
                                                          characteristics_model=model_analysis,
                                                          abstraction=abstraction, process=process)
        response = model.invoke(formatted_prompt)
        response = response.content
        print("the conclusion is: ", response)

        return response

    def _arun(self, question: str):
        raise NotImplementedError("Async not supported.")

