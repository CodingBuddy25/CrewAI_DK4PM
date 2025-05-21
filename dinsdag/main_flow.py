from crewai.flow.flow import Flow, listen, start

from PM_agent import PM_agent
from DK_agent_company import DK_agent_company
from DK_agent_process import DK_agent_process
from WriterAgent import WriterAgent
import asyncio


class ResearchCrewFlow(Flow):
    #the class Flow gets passed, try to use this for passing variables
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
