from event_log_actions import append_to_event_log
from event_log_actions import storing_results
def introduction_agent():
    focus = str(input("What would you like the focus of the question to be? audit risks, sustainability risks, "
                      "cyber security risks, financial risks, bottlenecks and inefficiencies. Type it out literally. "))
    company = str(input("What is the name of the company which you want to analyse a process of? E.g. IKEA, google, "
                        "Proctor and Gamble (P&G)"))
    #If you don;t know the company maybe add a function later that they can add their own knowledge or skip this step
    file = str(input("What is the filename of the file that is in the event logs folder which you want to analyse? "
                     "E.g. purchase_to_pay_event_log.csv, AP_event_log_26052023.csv, O2C.csv"))
    process = str(input("What is the name of the process that is being analysed in the event lof file? E.g. order to "
                        "cash, purchase to pay, accounts payable"))
    #maybe add a human element here
    variables = f"focus: {focus}, company: {company}, file: {file}, process: {process}"
    storing_results("Introduction_agent", variables)
    append_to_event_log("Introduction agent")
    return company, process, focus, file
