from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from typing import List
from tools.research_tool import research_tool
from tools.process_discovery_tool import process_discovery_tool

@CrewBase
class Dinsdag():
    """Dinsdag crew"""

    agents: List[BaseAgent]
    tasks: List[Task]

    @agent
    def planner_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['planner_agent'],
            verbose=True,
        )

    @agent
    def Worker_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['Worker_agent'],
            verbose=True,
            tools = [process_discovery_tool,research_tool]
        )

    @agent
    def writing_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['writing_agent'],
            verbose=True,
            tools=[]
        )

    @task
    def planner_agent_task(self) -> Task:
        return Task(
            config=self.tasks_config['planner_agent_task'],
        )

    @task
    def Worker_agent_task(self) -> Task:
        return Task(
            config=self.tasks_config['Worker_agent_task'],
        )
    @task
    def writing_task(self) -> Task:
        return Task(
            config=self.tasks_config['writing_task'],
            output_file='report.md'
        )

    @crew
    def crew(self) -> Crew:
        """Creates the Dinsdag crew"""

        return Crew(
            agents=self.agents, # Automatically created by the @agent decorator
            tasks=self.tasks, # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
            # process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
        )
