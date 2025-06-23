import os
from datetime import datetime
def storing_results(directory_name,report):
    """Stores the intermediate results of the agents in their own separate folder"""

    files = [file_name for file_name in os.listdir(f"Intermediate_results/{directory_name}/") if
             (os.path.isfile(f"Intermediate_results/{directory_name}/{file_name}") and file_name.endswith('.txt'))]

    # https://stackoverflow.com/questions/50752844/python-count-number-of-text-file-in-certain-directory
    number_files = len(files)

    #writing results to file
    path_to_last_output = f"Intermediate_results/{directory_name}/output_{number_files}.txt"
    try:
        output_file = open(path_to_last_output, "w", encoding="utf-8")
        output_file.write(report)
        output_file.close()
    except UnicodeDecodeError:
        output_file = open(path_to_last_output, "w" , encoding="utf-8")
        output_file.write(report)
        output_file.close()
    #storing the path of the most recent output

def append_to_event_log(agent_name):
    """For a human observer to see back the flow process"""
    current_time = datetime.now()
    event_log = open("../event_log_human_readable.txt", "a")
    to_write = f"""\n -{agent_name}: {current_time}"""
    event_log.write(to_write)
    event_log.close()

def summary_event_log():
    #is not correct yet because if I haven't run process expert yet, it will add it to the list. Maybe making it a dictionary and saying True when it has run.

    directory_names = ["Process_mining_agent","Company_DK_agent","Process_expert_DK_agent"]
    path = "Intermediate_results/event_log_agents.txt"

    if os.path.exists(path):
        os.remove(path)
        print("Intermediate_results/event_log_agents.txt removed")

    for directory in directory_names:
        files = [file_name for file_name in os.listdir(f"Intermediate_results/{directory}/") if
             (os.path.isfile(f"Intermediate_results/{directory}/{file_name}") and file_name.endswith('.txt'))]
        most_recent_output = len(files) -1
        output_file = open(f"Intermediate_results/{directory}/output_{most_recent_output}.txt", "r", encoding="utf-8")
        full_output = output_file.read()
        output_file.close()
        log = open(path, "a")
        log.write(directory + ": \n" + full_output + '_________________________________________________________________\n\n\n')
