from dinsdag.Functions_for_agents.prompts import report_prompt
from dinsdag.Functions_for_agents.event_log_actions import append_to_event_log
from dinsdag.Functions_for_agents.event_log_actions import summary_event_log
from dinsdag.Functions_for_agents.event_log_actions import storing_results
from crewai import LLM


def WriterAgent(process,company,feedback):

    #https://docs.crewai.com/concepts/llms
    llm = LLM(
        model="openai/gpt-4o",
        temperature=0.1)

    summary_event_log()
    output_file = open('Intermediate_results/event_log_agents.txt', "r")
    full_output = output_file.read()
    output_file.close()
    formatted_prompt = report_prompt.format(process=process, company=company)
    input = formatted_prompt
    if len(feedback) > 1:
        input = input + "Also implement this feedback:" + feedback + ". Implementing the feedback is very important!"
    final_input = input + "\n All of the knowledge that you should integrate is written after this. Note that you can distinguish the agents with their titles Process_mining_agent,Company_DK_agent and Process_expert_DK_agent:" + full_output

    resp = llm.call(final_input)
    storing_results("Writing_report_agent", resp)
    append_to_event_log("Report writer agent")