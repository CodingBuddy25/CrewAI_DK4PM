#https://github.com/crewAIInc/crewAI/discussions/1096
#https://docs.crewai.com/tools/filewritetool
from crewai.tools import BaseTool
from typing import Type
from pydantic import BaseModel
import os
from crewai_tools import FileWriterTool

# Initialize the tool
file_writer_tool = FileWriterTool()

# Write content to a file in a specified directory
result = file_writer_tool._run('example.txt', 'This is a test content.', 'test_directory')
print(result)

class file_writing_tool_inputs(BaseModel):
    """Analyses the process with an LLM call, it will return the most important elements for the specific prompt"""
    response:str
str

class FileWriterTool(BaseTool):
    name: str = "file_writing_tool"
    description: str = "Writes given content to a specified file."

    def _run(self, response: str) -> str:
        # Open the specified file in write mode and write the content

        # saving the results to a file
        workingDirectory = os.path.dirname(os.path.abspath("output_0.txt"))
        file_path = os.path.join(workingDirectory, "tools", "process_analysis_results")

        print("The filepath is", file_path)
        folder_path = os.path.join(file_path, "tools", "process_analysis_results")
        files = [file_name for file_name in os.listdir(folder_path) if
                 (os.path.isfile(f"tools/process_analysis_results/{file_name}") and file_name.endswith('.txt'))]

        number_files = len(files)
        output_file = open(f"process_analysis_results/output_{number_files}.txt", "w")
        output_file.write(response)
        output_file.close()
        print("the conclusion is: ", response,
              "\n ______________________________________________ \n The content above was written to the file. ")


        return f"Content successfully written"
