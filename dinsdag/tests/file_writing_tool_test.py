#https://github.com/crewAIInc/crewAI/discussions/1096
#https://docs.crewai.com/tools/filewritetool
from crewai.tools import BaseTool
from typing import Type
from pydantic import BaseModel
import os

response = "thirdfile"
        # saving the results to a file
workingDirectory = os.getcwd()
file_path = os.path.join(workingDirectory, "process_analysis_results")
print(os.listdir(file_path))
files = [file_name for file_name in os.listdir(file_path)]
print(files)
number_files = len(files)
output_file = open(f"{file_path}/output_{number_files}.txt", "w")
output_file.write(response)
output_file.close()
print("the conclusion is: ", response,
      "\n ______________________________________________ \n The content above was written to the file. ")