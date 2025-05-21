from prompts import report_prompt
from event_log_actions import update_event_log
from event_log_actions import read_event_log
import os
def WriterAgent():
        #to write!!
    # prompt = filled_template + abstraction_file
    #read the last files of Company DK and process expert
    """Review the contents from both researches and the PM diagnostic task and weave them together into a coherent report of at least 1500 words which combines the {process} with
    the {company} with the steps from the result of the PM_agent analysis / PM_diagnostic task.
    You may leave out information that seems irrelevant. Provide links for references.     Use at least 20 relevant references in the paper (if possible) and at most 40 references.

    You have much experience in writing reports. You can combine knowledge and weave them into a well-analysed report and it is extremely important that every paragraph links to a
    process from the PM_agent, reference to the step in the csv file, showed in the manner:  'Send Purchase Order -> Receive Goods' step. You are known for FULLY referencing everything,
    make whole source link available. You are good at following instructions step by step.


    You can combine the knowledge and weave them into a well-analysed report
    and it is extremely important that every paragraph links to a process from
    the outputs: {skip_analysis} and {skip_flow}, and reference to the particular step that you are talking about
    using the format 'Send Purchase Order -> Receive Goods'. It is important that
    in every paragraph you fully reference to at least one source link from the research agents AND to a relevant step from the results of the PM_agent / the PM diagnostic task.
    Add an overview of all the used references at the bottom of the report in this format:
    ## References

    - [https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8437773/](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8437773/)
    - [https://www.capgemini.com/wp-content/uploads/2017/07/streamlining-the-order-to-cash-process.pdf](https://www.capgemini.com/wp-content/uploads/2017/07/streamlining-the-order-to-cash-process.pdf)
    - [https://www.mckinsey.com/capabilities/operations/our-insights/a-practical-approach-to-supply-chain-risk-management](https://www.mckinsey.com/capabilities/operations/our-insights/a-practical-approach-to-supply-chain-risk-management)
    - [https://www.mckinsey.com/industries/consumer-packaged-goods/our-insights/cpg-operations-how-to-win-in-a-rapidly-changing-environment](https://www.mckinsey.com/industries/consumer-packaged-goods/our-insights/cpg-operations-how-to-win-in-a-rapidly-changing-environment)


    """
    readings = read_event_log()
    input = report_prompt + "\n" + readings
    resp = input.llm.openai_query(input, api_key=os.getenv('OPENAI_API_KEY'), openai_model="gpt-4o")
    # resp = "This is the final report with many many references of course"
    files = [file_name for file_name in os.listdir("Intermediate_results/Writing_report_agent/") if
             (os.path.isfile(f"Intermediate_results/Writing_report_agent/{file_name}") and file_name.endswith('.txt'))]
    number_files = len(files)
    print(number_files, "are the number of files in the directory")
    output_file = open(f"Intermediate_results/Writing_report_agent/output_{number_files}.txt", "w")
    output_file.write(resp)
    output_file.close()
    update_event_log("writer_agent", resp)

