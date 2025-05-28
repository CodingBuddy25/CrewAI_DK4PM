from crewai.flow.flow import Flow, listen, start, router, or_
from pydantic import BaseModel

from dinsdag.Agents.Introduction_agent import introduction_agent
from dinsdag.Agents.PM_agent import PM_agent
from dinsdag.Agents.DK_agent_company import DK_agent_company
from dinsdag.Agents.DK_agent_process import DK_agent_process
from dinsdag.Agents.WriterAgent import WriterAgent
import asyncio


class FlowState(BaseModel):
    process: str = " "
    company: str = " "
    focus: str = " "
    chosen_approach: str = " "
    filename: str = " "
    specific_question: str = " "
    human_feedback: str = " "

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
        self.state.human_feedback = " "
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

    @listen(or_(DK_process_agent,"feedback writing"))
    def Writing(self):
        WriterAgent(self.state.process, self.state.company)

#https://github.com/crewAIInc/crewAI-examples/blob/main/lead-score-flow/src/lead_score_flow/main.py
#https://docs.crewai.com/learn/human-in-the-loop
#https://docs.crewai.com/concepts/flows
    @router(Writing)
    def human_agent(self):
        print("\nPlease choose an option:")
        print("1. The paper is good. Exit the program. ")
        print("2. Redo writing agent")

        choice = input("Enter the number of your choice: ")

        if choice == "1":
            print("Exiting the program.")
            exit()
        elif choice == "2":
            feedback = input(
                "\nPlease provide additional feedback on what you're looking for in candidates:\n"
            )
            self.state.human_feedback = feedback
            print("\nRe-running lead scoring with your feedback...")
            return "feedback writing"
        else:
            print("\nInvalid choice. Please try again.")
            return "human_in_the_loop"
async def kickoff():
    final_flow = ResearchCrewFlow()
    final_flow.plot("FlowPlot.html")
    await final_flow.kickoff_async()


if __name__ == "__main__":
    asyncio.run(kickoff())
