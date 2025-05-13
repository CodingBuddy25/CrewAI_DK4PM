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
