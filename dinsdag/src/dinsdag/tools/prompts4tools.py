choosing_approach_prompt = """
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
     responses: "DFG", "Temporal Profile" or "Variants".
     
     The focus the user gave is:
    """

process_analysis_prompt = """
        You are a business process consultant, 
        specialized in analyzing processes and the components of processes. 
        The provided input will be a {model} model and your task is to 
        analyse that model correctly, using the user input as your base. 

        To analyse a {model} you can look at {characteristics_model}. 
        You should look for elements in the {process} process that have to do with {focus}. 
        You should list those steps/components of the provided process
         in a structured way in your response.\n

        Can you give me the most important process steps/activities of your analysis?
         Remember to justify the answer always! Preferably give between 3 to 5 process steps
          and their explanation, nothing else.
        List those in a structured way. Here is the process you have to analyze:\n
        """
