import sys
sys.path.insert(0, "./Engine")

import pystray
import threading
from PIL import Image
from Engine.auto import autopost

# Function to run after clicking on the icon
def after_click(icon, query):
    if str(query) == "Exit":
        icon.stop()

# Load the icon
image = Image.open("./App/icon.ico")

# Create the menu
menu = (
    pystray.MenuItem("Exit", after_click),
)

# Create the icon
icon = pystray.Icon("Silent Autopost", image, "Silent Autopost", menu)



# Create a separate thread to run the autopost() function
autopost_thread = threading.Thread(target=autopost)
autopost_thread.daemon = True  # Set the thread as a daemon thread
autopost_thread.start()


# Run the icon in the main thread
icon.run()
