
from gpt_researcher import GPTResearcher
from dinsdag.Functions_for_agents.event_log_actions import storing_results
from dinsdag.Functions_for_agents.event_log_actions import append_to_event_log
async def DK_agent_company(company, focus,process):
    """uses GPTresearcher to search the internet
    From documentation https://docs.gptr.dev/docs/gpt-researcher/gptr/pip-package
    For changing the background model: https://docs.gptr.dev/docs/gpt-researcher/gptr/deep_research"""
    DK_company_prompt = f"You are a company expert. Search the internet for useful facts and suggestions that link the {company} in question to {focus} and the {process} process. You must have at least 20 references in the final report, try to make the report as detailed as possible. "
    # input = DK_company_prompt + current_research
    researcher = GPTResearcher(query=DK_company_prompt, report_type="research_report")
    research_result = await researcher.conduct_research()
    report = await researcher.write_report()
    storing_results("Company_DK_agent", report)
    append_to_event_log("Domain knowledge agent with company specialization")
