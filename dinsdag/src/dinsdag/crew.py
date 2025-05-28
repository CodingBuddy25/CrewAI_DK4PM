from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from typing import List

from tools.choosing_approach_tool import choosing_approach_tool
from tools.abstraction_tool import abstraction_tool
from tools.process_analysis_tool import process_analysis_tool
from tools.file_writing_tool import writing_file_tool

from tools.tavily_search_company import tavily_search_company
from tools.tavily_search_process import tavily_search_process

@CrewBase
class Dinsdag():
    """Dinsdag crew"""

    agents: List[BaseAgent]
    tasks: List[Task]

    # Learn more about YAML configuration files here:
    # Agents: https://docs.crewai.com/concepts/agents#yaml-configuration-recommended
    # Tasks: https://docs.crewai.com/concepts/tasks#yaml-configuration-recommended
    

    @agent
    def PM_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['PM_agent'],
            tools=[choosing_approach_tool(), abstraction_tool(),process_analysis_tool()],
            verbose=True
        )

    @agent
    def DK_company_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['DK_company_agent'], # type: ignore[index]
            verbose=True,
            tools=[tavily_search_company()]
        )

    @agent
    def DK_process_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['DK_process_agent'], # type: ignore[index]
            verbose=True,
            tools = [tavily_search_process()]
        )

    @agent
    def writing_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['writing_agent'], # type: ignore[index]
            verbose=True,
            tools=[]
        )

    @task
    def PM_diagnostic(self) -> Task:
        return Task(
            config=self.tasks_config['PM_diagnostic'],
        )

    @task
    def DK_company_search(self) -> Task:
        return Task(
            config=self.tasks_config['DK_company_search'],
        )

    @task
    def DK_process_search(self) -> Task:
        return Task(
            config=self.tasks_config['DK_process_search'],
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
