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
    finished: bool = False


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
        self.state.finished = False
        # #option number 2
        # self.state.specific_question = f"Can you find the {focus} in the {process} at {company}. What are the {focus} for specific steps that you identified?"
        #
        # #option number 3
        # self.state.specific_question = f"Can you find the {focus} in the {process} process at {company}. What are {focus} that you identified?"

    @listen(or_(introduction_agent,"PM_agent"))
    def PM_agent(self):
        approach = PM_agent(self.state.filename, self.state.specific_question)
        self.state.chosen_approach = approach

    @router(PM_agent)
    def PM_router(self):
        if self.state.finished:
            return "feedback writing"
        else:
            return "DK_company_agent"

    @listen("DK_company_agent")
    async def DK_company_agent(self):
        await DK_agent_company(self.state.company, self.state.focus, self.state.process)

    @router(DK_company_agent)
    def DK_company_router(self):
        if self.state.finished:
            return "feedback writing"
        else:
            return "DK_process_agent"
    @listen("DK_process_agent")
    async def DK_process_agent(self):
        await DK_agent_process(self.state.company, self.state.focus, self.state.process)


    # @router(DK_process_agent)
    # def DK_process_router(self):
    #     if self.state.finished:
    #         return "feedback writing"
    #     else:
    #         return "feedback writing"

    @listen(or_(DK_process_agent,"feedback writing"))
    def Writing(self):
        WriterAgent(self.state.process, self.state.company)

    # https://github.com/crewAIInc/crewAI-examples/blob/main/lead-score-flow/src/lead_score_flow/main.py
    # https://docs.crewai.com/learn/human-in-the-loop
    # https://docs.crewai.com/concepts/flows
    @router(Writing)
    def human_agent(self):
        self.state.finished = True
        print("\nPlease choose an option:")
        print("1. The paper is good. Exit the program. ")
        print("2. Redo PM agent")
        print("3. Redo company agent")
        print("4. Redo process agent")
        print("5. Redo writing agent")


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
            return "PM_agent"
        elif choice == "3":
            feedback = input(
                "\nPlease provide additional feedback on what you're looking for in candidates:\n"
            )
            self.state.human_feedback = feedback
            print("\nRe-running lead scoring with your feedback...")
            return "DK_company_agent"
        elif choice == "4":
            feedback = input(
                "\nPlease provide additional feedback on what you're looking for in candidates:\n"
            )
            self.state.human_feedback = feedback
            print("\nRe-running lead scoring with your feedback...")
            return "DK_process_agent"
        elif choice == "5":
            feedback = input(
                "\nPlease provide additional feedback on what you're looking for in candidates:\n"
            )
            self.state.human_feedback = feedback
            print("\nRe-running lead scoring with your feedback...")
            return "feedback writing"
        else:
            print("Wrong input: exiting the program.")
            exit()


async def kickoff():
    final_flow = ResearchCrewFlow()
    final_flow.plot("FlowPlot.html")
    await final_flow.kickoff_async()


if __name__ == "__main__":
    asyncio.run(kickoff())
