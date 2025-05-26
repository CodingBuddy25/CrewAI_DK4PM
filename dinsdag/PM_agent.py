from PM_agent_tools import choosing_approach
from PM_agent_tools import abstraction
from PM_agent_tools import process_analysis
from PM_agent_tools import Event_log_readings




def PM_agent(file,specific_question):
    flag = False
    while flag == False:
        approach, flag = choosing_approach(specific_question)

    abstraction_file = abstraction(file, approach)
    process_analysis(abstraction_file, specific_question, approach)
    return approach
