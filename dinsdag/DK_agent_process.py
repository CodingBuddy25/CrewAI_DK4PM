import os

from gpt_researcher import GPTResearcher

from event_log_actions import update_event_log
from event_log_actions import read_event_log




#Maybe import the keys here as well, you need tavily and GPT

async def DK_agent_process(company, focus,process):
    """uses GPTresearcher to search the internet
    From documentation https://docs.gptr.dev/docs/gpt-researcher/gptr/pip-package
    For changing the background model: https://docs.gptr.dev/docs/gpt-researcher/gptr/deep_research

    It researches the focus, which is for example bottlenecks and risks.
    """
    DK_process_prompt = f"You are a process expert. Use the process mining information available to search the internet for useful facts and suggestions that link the company in question to {focus} or the {process} process."
    readings = read_event_log()
    input = DK_process_prompt + "\n" + readings
    researcher = GPTResearcher(query=input, report_type="research_report")
    research_result = await researcher.conduct_research()
    report = await researcher.write_report()
    files = [file_name for file_name in os.listdir("Intermediate_results/Process_expert_DK_agent/") if
             (os.path.isfile(f"Intermediate_results/Process_expert_DK_agent/{file_name}") and file_name.endswith('.txt'))]
    number_files = len(files)
    print(number_files, "are the number of files in the directory")
    output_file = open(f"Intermediate_results/Process_expert_DK_agent/output_{number_files}.txt", "w")
    output_file.write(report)
    output_file.close()
    update_event_log("DK_company_agent", report)

