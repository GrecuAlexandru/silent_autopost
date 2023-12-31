<div align="center">

[![logo](/Docs/logo.png)](https://github.com/GrecuAlexandru)

# Silent Autopost
Python script that automatically creates a short video and posts it on Youtube Shorts

</div>


# Disclaimer

**This is a _personal project_ and is meant for educational purposes only. I am not responsible for any misuse of this program. Please use it at your own risk. Please **DO NOT** contact me for any issues with this program. It is simply just a proof of concept and is not meant to be used in a production environment.**

## Description

This program automatically creates a short video and posts it on Youtube Shorts. It is intended to run on system startup and will post at a specified time. The program uses a random video and a random sound provided by you on top of which it adds a [random quote](https://zenquotes.io/) and its author.


## Getting Started

Clone the repository:

```
git clone https://github.com/GrecuAlexandru/silent_autopost.git
```


## Prerequisites

* [Register your application](https://developers.google.com/youtube/v3/guides/uploading_a_video) with Google so that it can use the OAuth 2.0 protocol to access Google APIs.

* Download the **`client_secrets.json`** file from the [Google Developers Console](https://console.cloud.google.com/apis/credentials/) and place it in `silent_autopost/Engine/YoutubeShorts/`. You will notice that it has a strange name like `client_secrets_1234567890-abcdefg.apps.googleusercontent.com.json`. Make a copy of it and rename it to `client_secrets.json`. Keep both files in that folder.

## Installation

* Install the Google APIs Client Library for Python (google-api-python-client) using pip:

    ```
    pip install --upgrade google-api-python-client
    ```

    The installation guide from Google suggests to install the library in a virtual environment, but it is not necessary:
    > With virtualenv, it's possible to install this library without needing system install permissions, and without clashing with the installed system dependencies.

    You can follow the guide [here](https://github.com/googleapis/google-api-python-client) if you want to install it in a virtual environment.



* Install the required packages:

    ```
    pip install -r requirements.txt
    ```
* Install [ffmpeg](https://ffmpeg.org/download.html) and add it to the PATH environment variable. You can follow the guide [here](https://www.wikihow.com/Install-FFmpeg-on-Windows).


## Usage

The program is intended to run on system startup and it will automatically create a short video and post it on Youtube Shorts at a specified time. You can change the time in `silent_autopost/Engine/auto.py`. The default time is 11:00 AM, 13:00 PM, 18:00 PM and 20:00 PM.

### Add your videos and sounds
Firstly, you must add your videos in `silent_autopost/Videos/`
and your sounds in `silent_autopost/Sounds/`. The program will randomly select a video and a sound from those folders and combine them into a short video. The video must be in `.mp4` format and the sound must be in `.mp3` format. You can add as many videos and sounds as you want. There is a video file and a sound file in the `Docs/Example/` folder that you can use to test the program.

### Add your own title and description

You must modify the title and description of your Youtube short by changing the `title` and `description` variables in `silent_autopost/Engine/auto.py`. Modify this line according to your needs:

```
command = 'python ./Engine/YoutubeShorts/upload_video.py --file="./Output/final_video.mp4" --title="<YOUR_TITLE>" --description="<YOUR_DESCRIPTION>" --privacyStatus="private" --noauth_local_webserver'
````

### Make the video public

If you want to make the video public, you must modify the `privacyStatus` variable in `silent_autopost/Engine/auto.py` like this:

```
command = 'python ./Engine/YoutubeShorts/upload_video.py --file="./Output/final_video.mp4" --title="<YOUR_TITLE>" --description="<YOUR_DESCRIPTION>" --privacyStatus="public" --noauth_local_webserver'
```

### Run manually
You can run the program manually from the root directory of the cloned repository by typing:
```
python silent_autopost.py
```

### Run on system startup

Modify `silent_autopost.cmd` with the absolute path to `silent_autopost.py` and place it in the `Startup` folder. You can find the `Startup` folder by pressing `Win + R` and typing `shell:startup`. This will make the program run on system startup, but it will run in the background and you won't be able to see the console window.

### Important!

To know the program is up and running, you can check the system tray icons for the Silent Autopost icon. 

You can see what the program outputs by opening the file located at `silent_autopost/App/output.txt`. If you want to see the console window, you must run the program manually in the command prompt.

### To close the program, right click on the icon in the system tray and select `Exit`.

## Built With

* [Python](https://www.python.org/) - Programming language
* [Google APIs Client Library for Python](https://github.com/googleapis/google-api-python-client)
* [Pillow](https://pillow.readthedocs.io/en/stable/) - Used to add text to the video
* [OpenCV](https://opencv.org/) - Used to make the video
* [MoviePy](https://zulko.github.io/moviepy/) - Used to make the video
* [ffmpeg](https://ffmpeg.org/) - Used to cut the video
* [Youtube Data API v3](https://developers.google.com/youtube/v3) - Used to upload the video on Youtube Shorts
* [Youtube Shorts](https://www.youtube.com/shorts) - The platform where the video is uploaded
* [ZenQuotes](https://zenquotes.io/) - Used to get random quotes

## Authors

* **Alexandru Grecu** - *Full project* - [GrecuAlexandru](https://github.com/GrecuAlexandru)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details