from crewai.flow.flow import Flow, listen, start

from PM_agent import PM_agent
from DK_agent_company import DK_agent_company
from DK_agent_process import DK_agent_process
from WriterAgent import WriterAgent
import asyncio


class ResearchCrewFlow(Flow):
    #the class Flow gets passed, try to use this for passing variables
    # This is from the other branch, possibly something like this will work?
    # focus = str(
    #     input("What is the focus of your research? e.g. bottlenecks, financial risks, IT and Cyber risks, audit risk"))
    # company = str(input("What is the company your research? e.g. Google, IKEA, proctor and gamble (P&G)"))
    # process = str(input(
    #     "What is the process your research should analyse? e.g. loan application, purchase-to-pay, IT incident handling, order to cash"))
    # filename = str(input("What is the filename (stored int he Event_logs folder) do you want to analyse? e.g. O2C.csv"))
    # prompt_DK_company = f'Conduct a thorough research about {company}  using the context of {process} if you have it. Use the tavily_search_company and make sure that the research has many references.'
    # prompt_DK_process = f'Conduct a thorough research about the {process} process using the context of {company} if you have it. Use the tavily_search_process and make sure that the research has many references.'
    # inputs = {
    #              'process': process,
    #              'company': company,
    #              'focus': focus,
    #              'chosen_approach': 'DFG',
    #              'filename': filename,
    #              'prompt_DK_company': prompt_DK_company,
    #              'prompt_DK_process': prompt_DK_process
    # }
    @start()
    def PM_agent(self):
        PM_agent()

    @listen(PM_agent)
    async def DK_company_agent(self):
        await DK_agent_company()

    @listen(DK_company_agent)
    async def DK_process_agent(self):
        await DK_agent_process()

    @listen(DK_process_agent)
    def Writing(self):
        WriterAgent()


async def kickoff():
    final_flow = ResearchCrewFlow(inputs={"product": "AI-powered chatbots"})
    final_flow.plot("PoemFlowPlot")
    await final_flow.kickoff_async()


if __name__ == "__main__":
    asyncio.run(kickoff())
