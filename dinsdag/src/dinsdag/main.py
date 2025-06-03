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
    #DFG is the default plot
    focus = str(input("What is the focus of your research? e.g. bottlenecks, financial risks, IT and Cyber risks, audit risk"))
    company = str(input("What is the company your research? e.g. Google, IKEA, proctor and gamble (P&G)"))
    process = str(input("What is the process your research should analyse? e.g. loan application, purchase-to-pay, IT incident handling, order to cash"))
    filename = str(input("What is the filename (stored int he Event_logs folder) do you want to analyse? e.g. O2C.csv"))
    prompt_DK_company = f'Conduct a thorough research about {company}  using the context of {process} if you have it. Use the tavily_search_company and make sure that the research has many references.'
    prompt_DK_process = f'Conduct a thorough research about the {process} process using the context of {company} if you have it. Use the tavily_search_process and make sure that the research has many references.'
    main_question = f"Can you find the {focus} in the {process} process at {company} and what are the potential causes reasons for the {focus}?"
    inputs = {
        'process': process,
        'company': company,
        'focus': focus,
        'chosen_approach': 'DFG',
        'filename': filename,
        'prompt_DK_company': prompt_DK_company,
        'prompt_DK_process': prompt_DK_process,
        'main_question': main_question
    }
    
    try:
        Dinsdag().crew().kickoff(inputs=inputs)
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")


run()
#
# def train():
#     """
#     Train the crew for a given number of iterations.
#     """
#     inputs = {
#         "topic": "AI LLMs",
#         'current_year': str(datetime.now().year)
#     }
#     try:
#         Dinsdag().crew().train(n_iterations=int(sys.argv[1]), filename=sys.argv[2], inputs=inputs)
#
#     except Exception as e:
#         raise Exception(f"An error occurred while training the crew: {e}")
#
# def replay():
#     """
#     Replay the crew execution from a specific task.
#     """
#     try:
#         Dinsdag().crew().replay(task_id=sys.argv[1])
#
#     except Exception as e:
#         raise Exception(f"An error occurred while replaying the crew: {e}")
#
# def test():
#     """
#     Test the crew execution and returns the results.
#     """
#     inputs = {
#         "topic": "AI LLMs",
#         "current_year": str(datetime.now().year)
#     }
#
#     try:
#         Dinsdag().crew().test(n_iterations=int(sys.argv[1]), eval_llm=sys.argv[2], inputs=inputs)
#
#     except Exception as e:
#         raise Exception(f"An error occurred while testing the crew: {e}")
