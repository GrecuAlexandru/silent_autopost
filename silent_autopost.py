import os
from PIL import Image
import pystray
import threading
from Engine.auto import autopost


# Function to run after clicking on the icon
def after_click(icon, query):
    if str(query) == "Exit":
        icon.stop()


# Get the absolute path of the current Python script
current_script_path = os.path.abspath(__file__)

# Get the directory containing the current script
current_directory = os.path.dirname(current_script_path)

# Navigate up the directory tree until you reach the project directory
project_directory = current_directory
while not os.path.basename(project_directory) == "silent_autopost":
    project_directory = os.path.dirname(project_directory)

# Define the relative path to your file within the project directory
file_path = "App/icon.ico"

icon_path = os.path.join(project_directory, file_path)

# Load the icon
image = Image.open(icon_path)

# Create the menu
menu = (pystray.MenuItem("Exit", after_click),)

# Create the icon
icon = pystray.Icon("Silent Autopost", image, "Silent Autopost", menu)

# Create a separate thread to run the autopost() function
autopost_thread = threading.Thread(target=autopost)
autopost_thread.daemon = True  # Set the thread as a daemon thread
autopost_thread.start()

# Run the icon in the main thread
icon.run()
