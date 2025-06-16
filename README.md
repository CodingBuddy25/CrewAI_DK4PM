# Specialization is key: a study on the effects of specialization of LLM agents for the answering of complex business prompts

This research concludes that there is an optimal degree of specialization (N_agents − 1) above zero for domain knowledge agents when answering complex prompts. The main research creates three multi agent system setups with varying degrees of specialization for domain knowledge gathering agents. What can be seen is that as the number of specialized agents $N$ increases, the quality of the answer initially increases in terms of integrated domain knowledge (which is linked to the absence of repetition and the reduction of generalized statements). However at a certain point, there are more domain knowledge agents than domain knowledge areas in the prompt at which point the quality of the output decreases again. An exploratory experiment adds additional specialization to the agents by adding a human-in-the-loop (HITL) whereby the user can provide feedback either within-agent (agent is finished once the feedback is processed) or between-agents (which returns to agents after full execution). Of the two setups, the within-agent feedback method was very effective in increasing the quality of the output and the between-agent setup did not. Future research could look at experimenting with the length of prompts and improving the quality of the individual agents with stronger researcher implementations (such as GPT_researcher).  
    Paper:  Specialization is key: a study on the effects of specialization of LLM agents for the answering of complex prompts
            Reintje van Gulijk, Peter van der Putten, Aske Plaat
            July 2025

For the experiment outputs and the calculation method of the contribution percentage see the [testing repository](https://github.com/CodingBuddy25/Evaluation_LLM)

## Branches overview
In this repository there are quite a 5 branches so there will be a brief explanation per branch.

Crew_DoS0: In this branch, there is only one worker agent that gathers domain knowledge. Using a planner agent it executes the tasks given by it. 

<img src="https://github.com/user-attachments/assets/c44c58c8-abf1-4447-9fba-58182a07aae5" width=40% height=60%>

Crew_DoS2: There are three specialized domain knowledge agents. One is a process mining expert, one is a company expert and one is a process expert. 
<img src="https://github.com/user-attachments/assets/c7dbeefe-e56b-48aa-9507-9140f7515325" width=50% height=50%>

Crew_DoS4: There are five specialized domain knowledge agents. See the image for the roles. 
![Schermafbeelding 2025-05-30 212415](https://github.com/user-attachments/assets/84e22037-6152-4fcf-a912-17527e81bb67)

Crew_DoS2_HITL: Adding extra specialization by allowing the human user to input feedback after an agent is completed. The agent can be rerun as many times as the user wants. You cannot hop back to an agent that was executed before.

Flow_DoS_HITL: Using a different coding structure altogether, the human-in-the-loop can rerun entire agents. The image below is of the automatically generated image with the use of the function .plot("FlowPlot.html")

<img src="https://github.com/user-attachments/assets/cf6e4be5-1eef-452f-8136-4f626bcfdf8c" width=25% height=50%>


## Folder structure
- `src/dinsdag/config/agents.yaml` has the agents definition
- `src/dinsdag/config/tasks.yaml` has the task definitions and the agent that the task is coupled with
- `src/dinsdag/crew.py` to set the sequential interaction of the agents
- `src/dinsdag/main.py` to define the main inputs that will be passed throughout the program
- `src/dinsdag/tools/Event Logs` contains five of the six event logs. One of the event logs is unfortunately too big but it can be found on https://data.4tu.nl/articles/dataset/BPI_Challenge_2017/12696884
- `src/dinsdag/tools/...` these files are tools that the agents can call upon to accomplish their tasks, have a look in the company tavily search and the choosing approach tool if you are interested. 

## Architecture

<img src="https://github.com/user-attachments/assets/f4d1d7fd-7f19-42a6-b609-889f56d65c9d" width=40% height=40%>


## ⚙️ Getting Started
### Installation

1. Install Python 3.11 or later. Guide.

2. Clone the project and navigate to the directory:

`git clone https://github.com/assafelovic/gpt-researcher.git
cd gpt-researcher`

3. Set up API keys by exporting them or storing them in a .env file.

`export OPENAI_API_KEY={Your OpenAI API Key here}
export TAVILY_API_KEY={Your Tavily API Key here}`

4. Install dependencies and start the server:

`pip install -r requirements.txt'

## ✉️ Support / Contact us

    Bachelor thesis student email: s3291480@vuw.leidenuniv.nl
    Thesis Supervisor: Peter van der Putten - LIACS - Leiden University

This project, GPT Researcher, is an experimental application and is provided "as-is" without any warranty, express or implied. We are sharing codes for academic purposes under the Apache 2 license. Nothing herein is academic advice, and NOT a recommendation to use in academic or research papers.

Our view on unbiased research claims:

    
