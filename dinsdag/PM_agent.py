from PM_agent_tools import choosing_approach
from PM_agent_tools import abstraction
from PM_agent_tools import process_analysis
from PM_agent_tools import Event_log_readings




def PM_agent():
    menu = int(input(
        "Would you like to analyse the O2C process (1), P2P process (2) or the accounts payable process (3)? Press 0 to exit"))
    flag = False
    while flag == False:
        focus = str(input(
            "What would you like the focus of the question to be? audit risks, sustainability risks, cyber security risks, financial risks, bottlenecks and inefficiencies. Type it out literally. "))
        if menu == 1:
            file = "O2C.csv"
            specific_question = f"Can you find the {focus} in the order to cash process at Procter & Gamble (P&G). What are potential causes for the {focus} that you identified?"
            company = "proctor & gamble"
            process = "order to cash"
        if menu == 2:
            file = "purchase_to_pay_event_log.csv"
            specific_question = f"Can you find the {focus} in the purchase to pay process at IKEA. What are the {focus} for specific steps that you identified?"
            company = "IKEA"
            process = "purchase to pay"
        if menu == 3:
            file = "AP_event_log_26052023.csv"
            specific_question = f"Can you find the {focus} in the accounts payable (AP) process at General Electric (GE). What are {focus} that you identified?"
            company = "General Electric"
            process = "accounts payable"
        approach, flag = choosing_approach(specific_question)

    abstraction_file = abstraction(file, approach)
    process_analysed = process_analysis(abstraction_file, specific_question, approach)
    # print("PROCESS ANALYSED FINAL ANSWER: \n \n", process_analysed)
    print(process_analysed)
    return process_analysed
