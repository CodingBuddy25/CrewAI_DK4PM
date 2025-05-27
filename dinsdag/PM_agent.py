from PM_agent_tools import choosing_approach
from PM_agent_tools import abstraction
from PM_agent_tools import process_analysis

from event_log_actions import append_to_event_log

def PM_agent(file,specific_question):
    flag = False
    while flag == False:
        approach, flag = choosing_approach(specific_question)

    abstraction_file = abstraction(file, approach)
    process_analysis(abstraction_file, specific_question, approach)
    append_to_event_log("Process mining agent")
    return approach
