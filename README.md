# Dinsdag Crew

Welcome to the Dinsdag Crew project, powered by [crewAI](https://crewai.com). 
This crew_DoS0 setup has been made by expanding and building upon the crewAI template, the information below is the standard information for CrewAI projects. For specific information on the project, see the README file of the crew_DoS2 branch.

## Installation

Ensure you have Python >=3.10 <3.13 installed on your system. This project uses [UV](https://docs.astral.sh/uv/) for dependency management and package handling, offering a seamless setup and execution experience.

First, if you haven't already, install uv:

```bash
pip install uv
```

Next, navigate to your project directory and install the dependencies:

(Optional) Lock the dependencies and install them by using the CLI command:
```bash
crewai install
```
## Exploring the setup

- `src/dinsdag/config/agents.yaml` has the agents definition
- `src/dinsdag/config/tasks.yaml` has the task definitions and the agent that the task is coupled with
- `src/dinsdag/crew.py` to set the sequential interaction of the agents
- `src/dinsdag/main.py` to define the main inputs that will be passed throughout the program
- `src/dinsdag/tools/Event Logs` contains five of the six event logs. One of the event logs is unfortunately too big but it can be found on https://data.4tu.nl/articles/dataset/BPI_Challenge_2017/12696884
- `src/dinsdag/tools/...` these files are tools that the agents can call upon to accomplish their tasks, have a look in the company tavily search and the choosing approach tool if you are interested. 

## Running the Project

To kickstart your crew of AI agents and begin task execution, run this from the root folder of your project:

```bash
$ crewai run
```

This command initializes the dinsdag Crew, assembling the agents and assigning them tasks as defined in your configuration.

## Understanding the Crew

The dinsdag Crew is composed of multiple AI agents, each with unique roles, goals, and tools. These agents collaborate on a series of tasks, defined in `config/tasks.yaml`, leveraging their collective skills to achieve complex objectives. The `config/agents.yaml` file outlines the capabilities and configurations of each agent in your crew.

