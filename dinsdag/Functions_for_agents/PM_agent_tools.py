# from langchain_core.prompts import ChatPromptTemplate
# from langchain_openai import ChatOpenAI

from .CSV_config import CSV_format_O2C
from .CSV_config import CSV_format_P2P
from .CSV_config import CSV_format_AP

from .prompts import choosing_approach_prompt
from .prompts import Process_analysis_prompt

from .event_log_actions import storing_results

import sys
import os
import pandas as pd
import pm4py

def Event_log_readings(file_path: str, file: str) -> str:
    """ basically the function is that of the Process discovery of Max in Tools, process mining, process mining tool
Event_log_readings is called a tool right now but I want to change it to a normal function, it is not a tool per se
"""
    # Distinction between CSV and XES file formats
    if file == "O2C.csv":
        used_class = CSV_format_O2C
        formatvariable = ('mixed')
    elif file == "purchase_to_pay_event_log.csv":
        used_class = CSV_format_P2P
        formatvariable = 'ISO8601'
    elif file == "AP_event_log_26052023.csv":
        used_class = CSV_format_AP
        formatvariable = 'mixed'

    if "csv" in file_path:
        # For CSV file formats paramters for 3 columns have to be set manually here
        df = pd.read_csv(file_path, sep=used_class.sep)

        # If required, convert time format
        df[used_class.timestamp] = pd.to_datetime(df[used_class.timestamp], format=formatvariable)
        print("fine")
        df = pm4py.format_dataframe(df, case_id=used_class.case, activity_key=used_class.activity,
                                    timestamp_key=used_class.timestamp)
        print("fine2")

        event_log = pm4py.convert_to_event_log(df)
    else:
        # Reading the event log directly from XES file
        event_log = pm4py.read_xes(file_path)
    return event_log

def choosing_approach(specific_question):
    """Takes the dictionary of different answers and compares them using the rules defined below"""

    filled_template = choosing_approach_prompt.format(user_query=specific_question)
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
    return approach, flag

def abstraction(filename, approach):
    """Creates an abstraction of the event log. To run, uncomment the code."""
    workingDirectory = os.path.dirname(sys.argv[0])
    print(workingDirectory)
    fileName = os.path.join(workingDirectory, "Event_logs", filename)
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
    return abstraction

def process_analysis(abstraction_file, specific_question, approach,feedback):
    """Creates an analysis of the graph analysis. To run, uncomment the LLM prompt."""
    analyse_model = {"DFG": "structural insights and identifying common paths",
                     "Temporal Profile": "the timing and duration of process activities",
                     "Variants": "comparing variants to identify best practices or areas for optimization"}
    model_analysis = analyse_model[approach]
    filled_template = Process_analysis_prompt.format(user_prompt=specific_question, model=approach,
                                                     characteristics_model=model_analysis)
    prompt = filled_template + abstraction_file + "human feedback is:" + feedback + "it may be true that there is no feedback."

    resp = pm4py.llm.openai_query(prompt, api_key=os.getenv('OPENAI_API_KEY'), openai_model="gpt-4o")

    storing_results("Process_mining_agent", resp)

