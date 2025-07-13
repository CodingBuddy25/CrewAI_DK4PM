choosing_approach_prompt = """
    You are a process mining expert. 
    There are three process mining approaches that can be used
    to turn a csv into a process model, please choose the most 
    appropriate of the three models to base the analysis on. 
    The options are (1) "DFG", (2) "Temporal Profile" and (3) "Variants".

    1.   DFG is the most suitable process mining approach when the analysis focuses on identifying inefficiencies. This is because it considers both the frequency and performance of the process, which are key metrics for evaluating efficiency and detecting bottlenecks.

    2. Variants is the best approach when the goal is to identify audit risks. It examines all process variants, providing a comprehensive view of which components occur and how often—crucial for audit-related insights.

    3. Temporal Profile is the preferred approach for identifying cybersecurity risks. By analyzing normal user and system behavior over time, it helps establish baselines and detect deviations that may indicate threats such as unauthorized access or insider activity.

Important: If the specific type of analysis is not provided, respond only with one of the following options: "DFG", "Temporal Profile", or "Variants"—nothing else."""

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
        List those in a structured way. Here is the process you have to analyze: {abstraction}\n
        """
