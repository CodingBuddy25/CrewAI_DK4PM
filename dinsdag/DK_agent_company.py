from prompts import DK_company_prompt

from gpt_researcher import GPTResearcher
import os
#Maybe import the keys here as well, you need tavily and GPT

async def DK_agent_company():
    """uses GPTresearcher to search the internet
    From documentation https://docs.gptr.dev/docs/gpt-researcher/gptr/pip-package
    For changing the background model: https://docs.gptr.dev/docs/gpt-researcher/gptr/deep_research"""
    current_research = open("Collaborative_answer.txt", "r")
    current_research = current_research.read()
    input = DK_company_prompt + current_research
    researcher = GPTResearcher(query=input, report_type="research_report")
    research_result = await researcher.conduct_research()
    report = await researcher.write_report()
    files = [file_name for file_name in os.listdir("Intermediate_results/Company_DK_agent/") if
             (os.path.isfile(f"Intermediate_results/Company_DK_agent/{file_name}") and file_name.endswith('.txt'))]
    number_files = len(files)
    print(number_files, "are the number of files in the directory")
    output_file = open(f"Intermediate_results/Company_DK_agent/output_{number_files}.txt", "w")
    output_file.write(report)
    output_file.close()
