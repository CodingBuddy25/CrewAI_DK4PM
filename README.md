#  Specialization is key: a study on domain knowledge gathering agent specialization in process mining
Process mining analyses digital event logs to improve complex, large-scale industry processes. The event log analysis can help to identify risks and inefficiencies, or can be used to create a solutions methodology for process improvement. Although process mining is often performed by human experts, this research will improve upon an agentic setup whereby human experts are mimicked by digital Domain Knowledge Gathering Agents (DKGAs). By digitizing process mining, accessibility and resource efficiency are increased for all product owners. This research improves upon a setup from previous research by experimenting with two forms of DKGA specialization.

The main experiment increased the amount of role specialization in DKGAs. A setup with a single DKGA was compared to one with three role-specialized DKGAs and five role-specialized DKGAs to answer process risk and inefficiency questions. The results show that having a setup with three role-specialized DKGAs was more effective in answering the questions, than the setups with one or five DKGAs. Contrary to intuition, a setup with five DKGAs is less effective than three DKGAs, because the writer agent struggles to create a cohesive answer that combines all domain knowledge gathering agents' output.

The human-in-the-loop experiment provided user feedback specialization to the DKGA, resulting in increased user-friendliness and explainability of the setups. This is because of three traits: system interactivity, DKGA error detection, and the ability to view intermediate results instead of only the final result. Despite these traits, the quality of the written output did not improve significantly. 

Future research could focus on testing the setups with different permutations of the DKGA execution order, measuring the effect of different search engine tools on the references quality and automating the creation of role-specialized DKGAs based on the complexity of process risks and inefficiency questions.

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
A global setup can be seen below which holds for all five experimental setups. It has two inputs (an event log and a question), a total of $N$ DKGAs, and a writing agent. This writing agent combines the domain knowledge gathered by all the agents and weaves it together into a coherent report. This writing agent is the same for every setup with exactly the same prompting; its aim is to answer the process risk and inefficiency questions. The code of all the setups be found on \href{https://github.com/CodingBuddy25/CrewAI_DK4PM}{GitHub}. 
<img src="https://github.com/user-attachments/assets/a571152c-0205-4efc-8d3c-cb4c86b79206" width=40% height=40%>

## Implementational differences of the Crew and Flow
The Flow works quite differently from the Crew on an implementational level because there is no predefinition of roles or tasks in .yaml files. Rather, functions are called in order using the @listen commands. These commands provide more control over the sequence of events. The Crew has a simpler setup to the Flow because it is more restrictive in the order of events. 

### Memory and filestructure
Contrary to the Crew setup, in which the agents store their own memory, the Flow setup requires an implementation of memory storage. The results of the agents are be stored within an ``intermediate results" directory. An simple event log keeps track of which agent was called at what precise time. This log was made to see whether the DoS2FH setup had a loop between agents or if some agents took an abnormally long time to run. An example of the event log can be seen below
    Example event log that was made to be understandable for a human reader, it contains the agents that were called in the Flow and the exact timing that they were finished:
    -Introduction agent: 2025-05-29 10:47:25.276898
    -Process mining agent: 2025-05-29 10:48:10.851242
    -Domain knowledge agent with company specialization: 2025-05-29 10:49:41
    -Domain knowledge agent with process specialization: 2025-05-29 10:51:10
    -Report writer agent: 2025-05-29 10:51:53.986709
    -Report writer agent: 2025-05-29 10:54:45.681480
    -Process mining agent: 2025-05-29 10:56:01.329373
    -Report writer agent: 2025-05-29 10:56:53.473785"


The four different Crew setups have almost the same file structure. The Crew framework keeps a strict file structure whereby the Crew is stored in the .src directory. In this case, the name of the Crew is Dinsdag. For the full file structure, see visual examples below. It is important to note that the file structure changes for the different DoS setups, as some tools become independent agents. The file structure for DoS2FH is very standard with agents neatly stored in the agent directory and the (helper) functions stored in their own directory.  

Crew filestructure: 
![filesystem dinsdag crew2](https://github.com/user-attachments/assets/5c916f04-d3fa-480c-aadf-a44a5d3eec02)
Flow Filestructure: 
![filesystem dinsdag flow](https://github.com/user-attachments/assets/49fafb6e-f02f-41d8-a2f0-8630369427c8)




### Implementing Human-in-the-loop
HITL implementation of the Crew and the Flow differ. In the Crew, the feedback implementation is as simple as adding ``human\_input: True" to the DKGAs in the tasks.yaml file.

The feedback method of the Flow has a very different implementation. A human agent was added, which makes use of the CrewAI @router functionality and a nested attribute that keeps track of whether the setup has already reached the end of the sequence once. State is the name of the class instance that is passed through all the agents, its nested attribute called ``finished" starts with the boolean False and gets changed to True once the full agent sequence has been run once.  

All agents all have their own routers. After an agent has run, the router of that agent will decide whether it is routed to the next agent in the sequence or possibly skip agents and go to the writing agent immediately. If the nested attribute ``finished" is True, then the router will go to the writing agent. If it is False, the sequence continues.

The previously mentioned class instance State contains more variables besides ``finished". Company, process, focus and filename will be added by the user in the introduction agent and the other variables are added by the agents when running. For example, human feedback is added by the human (feedback) agent. State is an instance of class FlowState, which can be seen below. \\

    class FlowState(BaseModel):
        process: str = " "
        company: str = " "
        focus: str = " "
        chosen_approach: str = " "
        filename: str = " "
        specific_question: str = " "
        human_feedback: str = " "
        finished: bool = False


## Overview of DKGA outputs
In the DoS2, DoS2CH and DoS2FH setups, a process mining agent is present which is able to recognise .csv and .xes files as event log inputs. In DoS4, this is the process model selection agent. Using this input, the PM4PY library takes an abstraction and turns the event log into either a directly-follows graph, a temporal profile graph, or a variants graph depending on the context of the process risk and process inefficiencies questions. An example output can be seen below. 
![output_1](https://github.com/user-attachments/assets/4c892cc6-6ea1-45bd-8a9e-b4efdd060285)


After the abstraction has taken place, an analysis of this process is executed either by an independent agent (DoS4) or a tool (DoS2, DoS2CH,DoS2FH). An example output can be seen below. 
![output_2](https://github.com/user-attachments/assets/ca68a98b-8ac0-471a-aef4-78e93952f5ed)


The abstraction analysis agent (and other DKGAs) makes use of external domain knowledge gathering by the Tavily tool (DoS2, DoS4, DoS2CH) or the GPT_researcher tool (DoS2FH).

## Tavily tool programming
Results from the Tavily tool are in the form of a nested dictionary and can be found in the Tools directory. Coding of the search is as follows:

    for res in results:
        formatted_results += f"Source: {res.get('url', 'No URL')}"
        formatted_results += f"Title: {res.get('title', 'No Title')}"
        formatted_results += f"Content: {res.get('content', 'No Content')}"

        
This format can be seen in an example output of the P&G company DKGA, as seen below in the image. 
![output_3](https://github.com/user-attachments/assets/f70f7229-1911-4062-991a-5cdc4e5f8386)

 

## Installation

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
    Thesis Supervisor: Peter van der Putten - LIACS - Leiden University

This project, GPT Researcher, is an experimental application and is provided "as-is" without any warranty, express or implied. We are sharing codes for academic purposes under the Apache 2 license. Nothing herein is academic advice, and NOT a recommendation to use in academic or research papers.

Our view on unbiased research claims:

    
