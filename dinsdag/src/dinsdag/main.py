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
    main_question = f"Can you find the {focus} in the {process} process at {company} and what are the potential causes reasons for the {focus}?"
    inputs = {
        'process': process,
        'company': company,
        'focus': focus,
        'chosen_approach': '',
        'filename': filename,
        'main_question': main_question
    }
    
    try:
        Dinsdag().crew().kickoff(inputs=inputs)
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")


run()
