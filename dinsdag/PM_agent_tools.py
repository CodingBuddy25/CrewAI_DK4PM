# from langchain_core.prompts import ChatPromptTemplate
# from langchain_openai import ChatOpenAI

from CSV_config import CSV_format_O2C
from CSV_config import CSV_format_P2P
from CSV_config import CSV_format_AP

from prompts import choosing_approach_prompt
from prompts import Process_analysis_prompt

from event_log_actions import storing_results

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
    approach = "DFG"
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

    # if approach == "DFG":
    #     abstraction = pm4py.llm.abstract_dfg(file_read)
    # elif approach == "Temporal Profile":
    #     temporal_profile = pm4py.discover_temporal_profile(file_read)
    #     abstraction = pm4py.llm.abstract_temporal_profile(temporal_profile, include_header=True)
    # elif approach == "Variants":
    #     abstraction = pm4py.llm.abstract_variants(file_read)
    # else:
    #     print("error: expected DFG, Temporal Profile or Variants. Got: ", approach)
    abstraction = """Order Confirmation Sent -> Prepare Goods for Shipment ( frequency = 38119  performance = 363528.248 )
Prepare Goods for Shipment -> Goods Shipped ( frequency = 37663  performance = 161225.308 )
Customer Credit Check -> Order Approval ( frequency = 35102  performance = 150234.508 )
Send Invoice -> Payment Received ( frequency = 34168  performance = 199630.362 )
Goods Shipped -> Send Invoice ( frequency = 32561  performance = 62525.077 )
Customer Credit Check -> Customer Credit Check ( frequency = 27826  performance = 232651.050 )
Prepare Goods for Shipment -> Send Invoice ( frequency = 21018  performance = 175118.150 )
Goods Shipped -> Payment Received ( frequency = 20969  performance = 108023.372 )
Order Confirmation Sent -> Order Approval ( frequency = 19759  performance = 65798.510 )
Send Invoice -> Goods Shipped ( frequency = 19411  performance = 103830.620 )
Order Approval -> Prepare Goods for Shipment ( frequency = 19004  performance = 298758.249 )
Customer Credit Check -> Order Confirmation Sent ( frequency = 17419  performance = 214266.362 )
Order Validation -> Order Validation ( frequency = 13913  performance = 232620.000 )
Order Rejected -> Order Completed ( frequency = 10551  performance = 345600.000 )
Customer Credit Check -> Order Rejected ( frequency = 10551  performance = 173545.181 )
Order Validation -> Order Approval ( frequency = 4588  performance = 320696.077 )
Payment Received -> Goods Shipped ( frequency = 2375  performance = 86400.000 )
Goods Shipped -> Order Completed ( frequency = 2375  performance = 86400.000 )
Order Validation -> Order Confirmation Sent ( frequency = 2340  performance = 384000.000 )
Send Invoice -> Prepare Goods for Shipment ( frequency = 2326  performance = 86400.000 )
Order Confirmation Sent -> Send Invoice ( frequency = 1571  performance = 345600.000 )
Prepare Goods for Shipment -> Payment Received ( frequency = 768  performance = 259200.000 )
Order Approval -> Send Invoice ( frequency = 755  performance = 259200.000 )"""
    return abstraction

def process_analysis(abstraction_file, specific_question, approach):
    """Creates an analysis of the graph analysis. To run, uncomment the LLM prompt."""
    analyse_model = {"DFG": "structural insights and identifying common paths",
                     "Temporal Profile": "the timing and duration of process activities",
                     "Variants": "comparing variants to identify best practices or areas for optimization"}
    model_analysis = analyse_model[approach]
    filled_template = Process_analysis_prompt.format(user_prompt=specific_question, model=approach,
                                                     characteristics_model=model_analysis)
    # prompt = filled_template + abstraction_file

    # resp = pm4py.llm.openai_query(prompt, api_key=os.getenv('OPENAI_API_KEY'), openai_model="gpt-4o")
    resp = """Based on the DFG abstraction of the order-to-cash process at Procter and Gamble, some potential audit risks and their possible causes include:
                    1. Duplicate Orders:
                    - Cause: The frequency of "Order Validation -> Order Validation" is 13913, indicating a potential risk of duplicate orders being validated.
                    - Root Cause: Lack of system controls to prevent duplicate orders from entering the system.

                    2. Inaccurate Credit Checks:
                    - Cause: The frequency of "Customer Credit Check -> Customer Credit Check" is 27826, suggesting multiple credit checks being performed on the same customer.
                    - Root Cause: Inadequate integration between systems leading to repeated credit check requests.

                    3. Delayed Payments:
                    - Cause: The performance time for "Payment Received -> Goods Shipped" is 86400, indicating a potential delay in payments being processed.
                    - Root Cause: Inefficient payment processing systems or delays in reconciliation between payment received and goods shipped.

                    4. Manual Order Approvals:
                    - Cause: The performance time for "Order Validation -> Order Approval" is 320696.077, suggesting a lengthy approval process.
                    - Root Cause: Manual order approval processes leading to delays in order processing.

                    5. Inaccurate Invoicing:
                    - Cause: The frequency of "Send Invoice -> Prepare Goods for Shipment" is 2326, indicating potential issues with invoicing being sent before goods are ready for shipment.
                    - Root Cause: Lack of synchronization between invoicing and shipment preparation processes, leading to incorrect or premature invoices.

                    6. Invalid Orders:
                    - Cause: The frequency of "Order Rejected -> Order Completed" is 10551, indicating a significant number of rejected orders that are still being completed.
                    - Root Cause: Inadequate order rejection processes or lack of proper communication between order validation and completion stages."""


    storing_results("Process_mining_agent", resp)

