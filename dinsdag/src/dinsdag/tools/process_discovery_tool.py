from crewai.tools import tool
import os
import sys
import pm4py

from dinsdag.src.dinsdag.tools.Event_log_reading import Event_log_readings
from dinsdag.src.dinsdag.tools.prompts4tools import choosing_approach_prompt,process_analysis_prompt


@tool
def process_discovery_tool(focus:str, filename:str) -> str:
    """Clear description for what this tool is useful for, your agent will need this information to use it."""
    flag = False
    while flag == False:
        filled_template = choosing_approach_prompt.format(user_query=focus)
        prompt = filled_template

        # retrieving reponse from LLM
        openai_key = os.getenv('OPENAI_API_KEY')
        approach = pm4py.llm.openai_query(prompt, api_key=openai_key, openai_model="gpt-4o-mini")
        print("CHOSEN APPROACH: ", approach, "_______________________________________________--")
        if approach in ["DFG", "Variants", "Temporal Profile"]:
            flag = True
        else:
            flag = False
            print(
                "Unable to find the right approach, try again with another analysis or explain in more detail what needs to be analysed")

    """Creates an abstraction of the event log. To run, uncomment the code."""
    workingDirectory = os.path.dirname(sys.argv[0])
    print(workingDirectory)
    fileName = os.path.join(workingDirectory, "tools","Event_logs", filename)
    file_read = Event_log_readings(fileName, filename)

    if approach == "DFG":
        abstraction = pm4py.llm.abstract_dfg(file_read)
    elif approach == "Temporal Profile":
        temporal_profile = pm4py.discover_temporal_profile(file_read)
        abstraction = pm4py.llm.abstract_temporal_profile(temporal_profile, include_header=True)
    elif approach == "Variants":
        abstraction = pm4py.llm.abstract_variants(file_read)
    else:
        print("error: expected DFG, Temporal Profile or Variants. Got: ", approach)

    """Creates an analysis of the graph analysis. To run, uncomment the LLM prompt."""
    analyse_model = {"DFG": "structural insights and identifying common paths",
                     "Temporal Profile": "the timing and duration of process activities",
                     "Variants": "comparing variants to identify best practices or areas for optimization"}
    model_analysis = analyse_model[approach]
    filled_template = process_analysis_prompt.format(user_prompt=focus, model=approach,
                                                     characteristics_model=model_analysis)
    prompt = filled_template + abstraction

    resp = pm4py.llm.openai_query(prompt, api_key=os.getenv('OPENAI_API_KEY'), openai_model="gpt-4o")

    return resp