#!/usr/bin/env python
import warnings
from crew import Dinsdag

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

# This main file is intended to be a way for you to run your
# crew locally, so refrain from adding unnecessary logic into this file.
# Replace with inputs you want to test with, it will automatically
# interpolate any tasks and agents information

def run():
    """
    Run the crew.
    """
    focus = str(input("What is the focus of your research? e.g. bottlenecks, financial risks, IT and Cyber risks, audit risk"))
    company = str(input("What is the company your research? e.g. Google, IKEA, proctor and gamble (P&G)"))
    process = str(input("What is the process your research should analyse? e.g. loan application, purchase-to-pay, IT incident handling, order to cash"))
    filename = str(input("What is the filename (stored int he Event_logs folder) do you want to analyse? e.g. O2C.csv"))
    prompt_DK_company = f'Conduct a thorough research about {company}  using the context of {process} if you have it. Use the tavily_search_company and make sure that the research has many references.'
    prompt_DK_process = f'Conduct a thorough research about the {process} process using the context of {company} if you have it. Use the tavily_search_process and make sure that the research has many references.'
    inputs = {
        'process': process,
        'company': company,
        'focus': focus,
        'chosen_approach': 'DFG',
        'filename': filename,
        'prompt_DK_company': prompt_DK_company,
        'prompt_DK_process': prompt_DK_process,
    }
    
    try:
        Dinsdag().crew().kickoff(inputs=inputs)
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")


run()
