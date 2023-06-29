import os
import time
import random
import psutil
import requests
import datetime
import subprocess
from .MakeVideo import make_video
from multiprocessing import freeze_support
from .write_output import write_output, create_new_session


# Limit the priority of this process to BELOW-NORMAL
def limit_cpu():
    p = psutil.Process(os.getpid())
    p.nice(psutil.BELOW_NORMAL_PRIORITY_CLASS)


# Upload the video to YouTube Shorts
def youtube_shorts_upload():
    # Get the absolute path of the current Python script
    current_script_path = os.path.abspath(__file__)

    # Get the directory containing the current script
    current_directory = os.path.dirname(current_script_path)

    # Navigate up the directory tree until you reach the project directory
    project_directory = current_directory
    while not os.path.basename(project_directory) == "silent_autopost":
        project_directory = os.path.dirname(project_directory)

    # Define the relative path to your file within the project directory
    upload_video_script_path = os.path.join(
        project_directory, "Engine/YoutubeShorts/upload_video.py"
    )

    final_video_path = os.path.join(project_directory, "Output/final_video.mp4")
    # Command to upload the video
    command = f'python {upload_video_script_path} --file={final_video_path} --title="The Quote Realm | Quotes #shorts #quotes #deep #advice #motivation" --description="Quotes | The Quote Realm #shorts #quotes" --privacyStatus="public" --noauth_local_webserver'

    # Run the command and capture the output
    output = subprocess.check_output(command, shell=True)

    # write_output the output
    write_output(output.decode())

    # Return a random minute between 0 and 60
    return random.randint(0, 60)


# The main autopost function
def autopost():
    # Delete the previous data from the output.txt file
    create_new_session()

    write_output("Silent Autopost started!")

    # Limit cpu usage
    freeze_support()
    limit_cpu()

    # Get a random minute between 0 and 60 before starting the machine
    random_minute = random.randint(0, 30)
    write_output("RANDOM MINUTE : " + str(random_minute))

    # Start the machine
    write_output("STARTED MACHINE")
    while True:
        # Get the current time
        now = datetime.datetime.now()

        # Check if it's 11am 13pm 18pm or 20pm
        if now.hour == 11 or now.hour == 13 or now.hour == 18 or now.hour == 20:
            # Check if it's the right random minute
            if now.minute == random_minute:
                write_output("It's time to post!")

                # Get a random quote
                write_output("Getting Quote : " + str(datetime.datetime.now()))
                response = requests.get("https://zenquotes.io/api/random")
                text = '"' + response.json()[0]["q"] + '"'
                author = response.json()[0]["a"]
                write_output("Got Quote : " + str(datetime.datetime.now()))

                # Wait for 30 sec before making the video and uploading it
                time.sleep(30)

                # Make the video
                make_video(text, author)

                time.sleep(30)

                # Upload it
                write_output(
                    "Uploading to Youtube Shorts : " + str(datetime.datetime.now())
                )
                # Get the random minute for the next upload
                random_minute = youtube_shorts_upload()
                write_output(
                    "Uploaded to Youtube Shorts : " + str(datetime.datetime.now())
                )

                write_output("Video Uploaded!")

        # Wait for 30 sec before checking again
        time.sleep(30)
