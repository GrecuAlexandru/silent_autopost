import os
import time
import random
import psutil
import requests
import datetime
import subprocess
from MakeVideo import make_video
from multiprocessing import freeze_support
from write_output import write_output, create_new_session


# Limit the priority of this process to BELOW-NORMAL
def limit_cpu():
    p = psutil.Process(os.getpid())
    p.nice(psutil.BELOW_NORMAL_PRIORITY_CLASS)


# Upload the video to YouTube Shorts
def youtube_shorts_upload():

    # Command to upload the video
    command = 'python ./Engine/YoutubeShorts/upload_video.py --file="./Output/final_video.mp4" --title="The Quote Realm | Quotes #quotes #shorts #deep #advice #motivation" --description="Quotes | The Quote Realm #quotes #shorts" --privacyStatus="private" --noauth_local_webserver'

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


    # Get a random quote
    response = requests.get("https://zenquotes.io/api/random")
    text = '"' + response.json()[0]["q"] + '"'
    author = response.json()[0]["a"]

    # Make the video
    make_video(text, author)

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

                # Make the video and upload it
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