from crewai.flow.flow import Flow, listen, start
from pydantic import BaseModel

from Introduction_agent import introduction_agent
from PM_agent import PM_agent
from DK_agent_company import DK_agent_company
from DK_agent_process import DK_agent_process
from WriterAgent import WriterAgent
import asyncio


class FlowState(BaseModel):
    process: str = " "
    company: str = " "
    focus: str = " "
    chosen_approach: str = " "
    filename: str = " "
    specific_question: str = " "


class ResearchCrewFlow(Flow[FlowState]):
    @start()
    def introduction_agent(self):
        company, process, focus, file = introduction_agent()
        self.state.company = company
        self.state.process = process
        self.state.focus = focus
        self.state.filename = file

        # option number 1
        self.state.specific_question = f"Can you find the {focus} in the {process} process at {company}. What are potential causes for the {focus} that you identified?"

        # #option number 2
        # self.state.specific_question = f"Can you find the {focus} in the {process} at {company}. What are the {focus} for specific steps that you identified?"
        #
        # #option number 3
        # self.state.specific_question = f"Can you find the {focus} in the {process} process at {company}. What are {focus} that you identified?"

    @listen(introduction_agent)
    def PM_agent(self):
        approach = PM_agent(self.state.filename, self.state.specific_question)
        self.state.chosen_approach = approach

    @listen(PM_agent)
    async def DK_company_agent(self):
        await DK_agent_company(self.state.company, self.state.focus,self.state.process)

    @listen(DK_company_agent)
    async def DK_process_agent(self):
        await DK_agent_process(self.state.company, self.state.focus,self.state.process)

    @listen(DK_process_agent)
    def Writing(self):
        WriterAgent(self.state.specific_question)


async def kickoff():
    final_flow = ResearchCrewFlow()
    await final_flow.kickoff_async()


if __name__ == "__main__":
    asyncio.run(kickoff())
