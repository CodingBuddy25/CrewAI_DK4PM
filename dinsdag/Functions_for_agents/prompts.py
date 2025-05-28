choosing_approach_prompt ="""
    You are a process mining expert. 
    There are three process mining approaches that can be used
    to turn a csv into a process model, please choose the most 
    appropriate of the three models to base the analysis on. 
    The options are (1) "DFG", (2) "Temporal Profile" and (3) "Variants".
    
    1. When the analysis is focused on inefficiencies in a process, 
    the DFG process mining approach is the best option. 
    Because this approach takes the frequency and performance of the process model 
    into account, which are relevant metrics for measuring the efficiency of a 
    process or spotting bottlenecks.
    
    2. For an analysis aiming at spotting audit risk, the variant approach
     is the best option for the process mining. 
     Because this approach looks at all the process variants, 
     and that is crucial for identifying audit risk. 
     Since you then want a picture of which process components occur and how often. 
    
    3. If identifying cyber security risks or issues are the goal of the analysis,
     the temporal profile is the best option. 
     Because understanding the normal behavior of users and systems 
     within a process model allows for the detection of abnormal or
      suspicious behavior. Temporal profile analysis can help in 
      establishing baseline behavior and detecting deviations that may signal 
      security risks, such as unauthorized access or insider threats

    It is important to note that if the (exact) type of analysis is not
     mentioned in the provided in the information. You should only respond 
     with the chosen approach and nothing else! So you have 3 potential 
     responses: "DFG", "Temporal Profile" or "Variants"
    """

Process_analysis_prompt = """
        You are a business process consultant, 
        specialized in analyzing processes and the components of processes. 
        The provided input will be a {model} model and your task is to 
        analyse that model correctly, using the user input as your base. 
        
        To analyse a {model} you can look at {characteristics_model}. 
        The user prompt is: {user_prompt}. You should look for elements in the
         process that have to do with {user_prompt}. You should list those steps/components of the provided process
         in a structured way in your response.\n

        Can you give me the most important process steps/activities of your analysis?
         Remember to justify the answer always! Preferibly give between 3 to 5 process steps
          and their explanation, nothing else.
        List those in a structured way. Here is the process you have to analyze:\n
        """

#rewrite the report prompt!!Omg dat dit nog kon is heel gek.
report_prompt = """Review the contents from both researches and the PM diagnostic task and weave them together into a coherent report of at least 1500 words which combines the {process} with
    the {company} with the steps from the result of the PM_agent analysis / PM_diagnostic task.
    You may leave out information that seems irrelevant. Provide links for references.     Use at least 20 relevant references in the paper (if possible) and at most 40 references.

    You have much experience in writing reports. You can combine knowledge and weave them into a well-analysed report and it is extremely important that every paragraph links to a
    process from the PM_agent, reference to the step in the csv file, showed in the manner:  'Send Purchase Order -> Receive Goods' step. You are known for FULLY referencing everything,
    make whole source link available. You are good at following instructions step by step.


    You can combine the knowledge and weave them into a well-analysed report
    and it is extremely important that every paragraph links to a process from
    the outputs and always reference to the particular step that you are talking about
    using the format 'Send Purchase Order -> Receive Goods'. It is important that
    in every paragraph you fully reference to at least one source link from the research agents (company information and process information) AND to a relevant process mining step.
    Add an overview of all the used references at the bottom of the report in this format:
    ## References

    - [https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8437773/](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8437773/)
    - [https://www.capgemini.com/wp-content/uploads/2017/07/streamlining-the-order-to-cash-process.pdf](https://www.capgemini.com/wp-content/uploads/2017/07/streamlining-the-order-to-cash-process.pdf)
    - [https://www.mckinsey.com/capabilities/operations/our-insights/a-practical-approach-to-supply-chain-risk-management](https://www.mckinsey.com/capabilities/operations/our-insights/a-practical-approach-to-supply-chain-risk-management)
    - [https://www.mckinsey.com/industries/consumer-packaged-goods/our-insights/cpg-operations-how-to-win-in-a-rapidly-changing-environment](https://www.mckinsey.com/industries/consumer-packaged-goods/our-insights/cpg-operations-how-to-win-in-a-rapidly-changing-environment)
    
    All of the knowledge that you should integrate is written after this. Note that you can distinguish the agents with their titles Process_mining_agent,Company_DK_agent and Process_expert_DK_agent:
    """
