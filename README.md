#  Specialization is key: a study on domain knowledge gathering agent specialization in process mining
Within the area of process mining, there is a lot of expertise required to answer event log questions. However, expertise is expensive. This research will expand upon a proof of concept (PoC) by Vogt (2023) which uses a ReWOO framework to answer such event log questions. The framework supplements human experts with large language models (LLM) in an agentic environment. The domain knowledge required to answer the event log question was gathered by one ``worker agent". This domain knowledge gathering agent (DKGA) proved effective in the PoC. 

This research will expand upon the PoC by including more DKGAs with their own domain expertise. The results show that having three specialized DKGAs is much more effective in answering event log questions than one DKGA. Another interesting result is that when there are five DKGAs, the quality of the answer decreases compared to three DKGAs. Therefore, there is an optimum amount of DKGAs. 

A human-in-the-loop experiment (HITL) added the possibility for the user to give feedback after a DKGA has run. This increases the amount of specialization further. The result of the HITL experiment shows  added user-friendliness and a new explainability aspect. However, the quality of the output itself improved only little and  the user should posses some knowledge about prompt engineering to be able to provide correct feedback. An analysis of the references was made and the results show that different search engine tools can significantly influence the quality of the references. 

Future research could look at improving the human-in-the-loop method, measuring the effect of different search engine tools and using different event log questions.


Keywords: process mining - multi agent systems - domain knowledge - prompt answering - CrewAI framework


    Paper:  Specialization is key: a study on domain knowledge gathering agent specialization in process mining
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

    
