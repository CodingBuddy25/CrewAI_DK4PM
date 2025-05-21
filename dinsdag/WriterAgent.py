from prompts import report_prompt
from event_log_actions import update_event_log
from event_log_actions import read_event_log
import os
def WriterAgent():
        #to write!!
    # prompt = filled_template + abstraction_file
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

