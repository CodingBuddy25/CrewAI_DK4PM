import sys
import os

from crewai.tools import BaseTool
from typing import Type
from pydantic import BaseModel

from .metadata_abstraction_tool import CSV_format_O2C
from .metadata_abstraction_tool import CSV_format_P2P
from .metadata_abstraction_tool import CSV_format_AP

import pandas as pd
import pm4py

class abstraction_tool_inputs(BaseModel):
    """Takes the abstraction of a file, this is either a DFG, a Temporal Profile and a Variants approach"""
    filename: str
    chosen_approach:str


class abstraction_tool(BaseTool):
    name: str = "abstraction"
    description: str = (
        """Takes the abstraction of a file, this is either a DFG, a Temporal Profile and a Variants approach"""
    )
    args_schema: Type[BaseModel] = abstraction_tool_inputs

    def _run(self, filename: str, chosen_approach:str) -> str:
        # workingDirectory = os.path.dirname(sys.argv[0])
        workingDirectory = os.path.dirname(os.path.abspath(filename))
        # print(os.getcwd(), "is the current working directory")
        file_path = os.path.join(workingDirectory, "tools", "Event_logs", filename)

        # Distinction between CSV and XES file formats
        if filename == "O2C.csv":
            used_class = CSV_format_O2C
            formatvariable = ('mixed')
        elif filename == "purchase_to_pay_event_log.csv":
            used_class = CSV_format_P2P
            formatvariable = 'ISO8601'
        elif filename == "AP_event_log_26052023.csv":
            used_class = CSV_format_AP
            formatvariable = 'mixed'

        if "csv" in file_path:
            # For CSV file formats paramters for 3 columns have to be set manually here
            df = pd.read_csv(file_path, sep=used_class.sep)

            # If required, convert time format
            df[used_class.timestamp] = pd.to_datetime(df[used_class.timestamp], format=formatvariable)
            df = pm4py.format_dataframe(df, case_id=used_class.case, activity_key=used_class.activity,
                                        timestamp_key=used_class.timestamp)
            event_log = pm4py.convert_to_event_log(df)
        else:
            # Reading the event log directly from XES file
            event_log = pm4py.read_xes(file_path)

        file_read = event_log
        approach = chosen_approach
        abstraction = False
        if approach == "DFG":
            abstraction = pm4py.llm.abstract_dfg(file_read)
        elif approach == "Temporal Profile":
            temporal_profile = pm4py.discover_temporal_profile(file_read)
            abstraction = pm4py.llm.abstract_temporal_profile(temporal_profile, include_header=True)
        elif approach == "Variants":
            abstraction = pm4py.llm.abstract_variants(file_read)
        else:
            print("error: expected DFG, Temporal Profile or Variants. Got: ", approach)
        print(type(abstraction))
        print("ABSTRACTION: ", abstraction)
        return abstraction

    def _arun(self, question: str):
        raise NotImplementedError("Async not supported.")

