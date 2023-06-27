import os

# Write print functions to output.txt file
def write_output(text):
    print(text)
     # Get the absolute path of the current Python script
    current_script_path = os.path.abspath(__file__)

    # Get the directory containing the current script
    current_directory = os.path.dirname(current_script_path)

    # Navigate up the directory tree until you reach the project directory
    project_directory = current_directory
    while not os.path.basename(project_directory) == 'silent_autopost':
        project_directory = os.path.dirname(project_directory)

    # Define the relative path to your file within the project directory
    file_path = 'App/output.txt'

    path = os.path.join(project_directory,file_path)
    file = open(path, "a")
    file.write(text)
    file.write("\n")
    file.close()

# Delete the previous data from the output.txt file
def create_new_session():
         # Get the absolute path of the current Python script
    current_script_path = os.path.abspath(__file__)

    # Get the directory containing the current script
    current_directory = os.path.dirname(current_script_path)

    # Navigate up the directory tree until you reach the project directory
    project_directory = current_directory
    while not os.path.basename(project_directory) == 'silent_autopost':
        project_directory = os.path.dirname(project_directory)

    # Define the relative path to your file within the project directory
    file_path = 'App/output.txt'

    path = os.path.join(project_directory,file_path)
    file = open(path, "w")
    file.write("")
    file.close()