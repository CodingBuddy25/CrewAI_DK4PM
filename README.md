# Specialization is key: a study on the effects of specialization of LLM agents for the answering of complex prompts

This research concludes that there is an optimal degree of specialization (N_agents − 1) above zero for domain knowledge agents when answering complex prompts. The main research creates three multi agent system setups with varying degrees of specialization for domain knowledge gathering agents. What can be seen is that as the number of specialized agents $N$ increases, the quality of the answer initially increases in terms of integrated domain knowledge (which is linked to the absence of repetition and the reduction of generalized statements). However at a certain point, there are more domain knowledge agents than domain knowledge areas in the prompt at which point the quality of the output decreases again. An exploratory experiment adds additional specialization to the agents by adding a human-in-the-loop (HITL) whereby the user can provide feedback either within-agent (agent is finished once the feedback is processed) or between-agents (which returns to agents after full execution). Of the two setups, the within-agent feedback method was very effective in increasing the quality of the output and the between-agent setup did not. Future research could look at experimenting with the length of prompts and improving the quality of the individual agents with stronger researcher implementations (such as GPT_researcher).  
    Paper:  Specialization is key: a study on the effects of specialization of LLM agents for the answering of complex prompts
            Reintje van Gulijk, Peter van der Putten, Aske Plaat
            July 2025

## Branches overview
In this repository there are quite a few branches so there will be a brief explanation per branch.

## Folder structure

    Event_Logs:
    There are five event logs that can be found in the different branches, they are BPI_Challenge_2013_incidents.xes, AP_event_log_26052023.csv,O2C.csv, PrepaidTravelCost.xes and purchase_to_pay_event_log.csv.

    One of the event log files named BPI_Challenge_2017.xes is not found in the files because it is too large to store, it can be found on https://data.4tu.nl/articles/dataset/BPI_Challenge_2017/12696884 if you want to reproduce the results.

    Prototype: contains the code of the PoC
    Experiments: contains the setup and outputs of the conducted experiments

## Architecture
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

`pip install -r requirements.txt
python -m uvicorn main:app --reload`

Visit http://localhost:8000 to start.

## ✉️ Support / Contact us

    Bachelor thesis student email: s3291480@vuw.leidenuniv.nl
    Thesis Supervisor: Peter van der Putten - LIACS - Leiden University

This project, GPT Researcher, is an experimental application and is provided "as-is" without any warranty, express or implied. We are sharing codes for academic purposes under the Apache 2 license. Nothing herein is academic advice, and NOT a recommendation to use in academic or research papers.

Our view on unbiased research claims:

    
