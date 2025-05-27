import os

from gpt_researcher import GPTResearcher

from event_log_actions import storing_results
from event_log_actions import append_to_event_log

async def DK_agent_process(company, focus,process):
    """uses GPTresearcher to search the internet
    From documentation https://docs.gptr.dev/docs/gpt-researcher/gptr/pip-package
    For changing the background model: https://docs.gptr.dev/docs/gpt-researcher/gptr/deep_research

    It researches the focus, which is for example bottlenecks and risks.
    """
    DK_process_prompt = f"You are a process expert. Use the process mining information available to search the internet for useful facts and suggestions that link the {process} process to {company} and {focus}. Try to find at least 20 references."
    # readings = read_event_log()
    # input = DK_process_prompt + "\n Previous research is:" + readings
    input = DK_process_prompt
    researcher = GPTResearcher(query=input, report_type="research_report")
    research_result = await researcher.conduct_research()
    report = await researcher.write_report()
    storing_results("Process_expert_DK_agent", report)
    append_to_event_log("Domain knowledge agent with process specialization")

