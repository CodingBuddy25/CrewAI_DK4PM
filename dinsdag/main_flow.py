from crewai.flow.flow import Flow, listen, start
from pydantic import BaseModel
from dinsdag.crews.research_crew.crew import Dinsdag


class ResearchCrew(BaseModel):
    result: str


class ResearchCrewFlow(Flow[ResearchCrew]):

    @start()
    def generate_poem(self):
        print("Generating poem")
        result = Dinsdag().crew().kickoff()

        print("Poem generated", result.content)
        self.state.result = result.content

    @listen(generate_poem)
    def save_poem(self):
        print("Saving poem")
        with open("poem.txt", "w") as f:
            f.write(self.state.poem)



def kickoff():
    final_flow = ResearchCrewFlow()
    final_flow.kickoff()


def plot():
    final_flow = ResearchCrewFlow()
    final_flow.plot("PoemFlowPlot")


if __name__ == "__main__":
    kickoff()
    plot()
