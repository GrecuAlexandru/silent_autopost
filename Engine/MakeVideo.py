import os
import cv2
import time
import random
import textwrap
from cutVideo import cut_video
from PIL import Image, ImageFont, ImageDraw
from getShortestLength import get_shortest_length
from moviepy.editor import VideoFileClip, AudioFileClip

# Function to delete a file
def deleteFile(filename):
    if os.path.exists(filename):
        os.remove(filename)

# Funciton to add text on a frame
def add_subtitle(
    bg,
    text="text",
    author="author",
):
    # Configurable variables
    stroke_color=(0, 0, 0)
    font_color=(255, 255, 255)

    # Get the absolute path of the current Python script
    current_script_path = os.path.abspath(__file__)

    # Get the directory containing the current script
    current_directory = os.path.dirname(current_script_path)

    # Navigate up the directory tree until you reach the project directory
    project_directory = current_directory
    while not os.path.basename(project_directory) == 'silent_autopost':
        project_directory = os.path.dirname(project_directory)

    # Define the relative path to your file within the project directory
    font_path = 'Engine/Utils/ProximaNovaSemibold.otf'

    font = os.path.join(project_directory, font_path)

    # Function to center the text
    def center_wrap(text, cwidth=80, **kw):
        lines = textwrap.wrap(text, **kw)
        return "\n".join(line.center(cwidth) for line in lines)

    # Wrap the text
    text = center_wrap(text, cwidth=40, width=40)
    
    # Get the width and height of the background image
    W, H = bg.width, bg.height

    # Draw the background image
    draw = ImageDraw.Draw(bg)

    # Set the font size and stroke width
    font_size = int(35*W/720)
    stroke_width = int(3*W/720)

    # Set the font
    font = ImageFont.truetype(font, font_size)

    # Get the width and height of the text
    xy = (0, 0)
    box = draw.multiline_textbbox(xy, text, font=font)

    # Calculate the x and y coordinates of the text (centered horizontally and vertically)
    # (x,y) is top left corner of the text
    x = (W - box[2]) / 2
    y = ((H - box[3]) / 2) - (H*700/3840)

    # Draw the text
    draw.multiline_text(
        (x, y),
        text,
        font=font,
        align="center",
        fill=font_color,
        stroke_width=stroke_width,
        stroke_fill=stroke_color,
    )   

    # Get the width and height of the author text
    author_box_width = draw.textbbox((0, 0), author, font=font)[2]
    author_box_height = draw.textbbox((0, 0), author, font=font)[3]

    # Calculate the x and y coordinates of the author text (centered horizontally and vertically)
    # (author_x,author_y) is top left corner of the author text
    author_x = x + box[2] - author_box_width - 30
    author_y = y + box[3] + author_box_height + 30

    # Save the image created until now to a temporary file
    auxx_path = 'Engine/Temp/auxx.jpg'

    auxx = os.path.join(project_directory, auxx_path)

    bg.save(auxx)

    # Open the temporary file
    bg = Image.open(auxx)

    # Draw the author text on the image opened
    drawAuthor = ImageDraw.Draw(bg)
    drawAuthor.text(
        (author_x, author_y), 
        "- "+author, 
        font=font,
        align="center",
        fill=font_color,
        stroke_width=stroke_width,
        stroke_fill=(15,15,15)
    )

    # Return the final image
    return bg


# Function to make a video
def make_video(text, author):

    # Get random sound #

    # Get the absolute path of the current Python script
    current_script_path = os.path.abspath(__file__)

    # Get the directory containing the current script
    current_directory = os.path.dirname(current_script_path)

    # Navigate up the directory tree until you reach the project directory
    project_directory = current_directory
    while not os.path.basename(project_directory) == 'silent_autopost':
        project_directory = os.path.dirname(project_directory)

    # Define the relative path to your file within the project directory
    sounds_path = 'Sounds'

    sound_folder_path = os.path.join(project_directory, sounds_path)

    # Get a list of all the files in the folder
    sound_files = [f for f in os.listdir(sound_folder_path) if os.path.isfile(os.path.join(sound_folder_path, f))]

    # Choose a random file from the list
    random_sound_file = random.choice(sound_files)

    # Get the path to the random file
    sound_file = os.path.join(sound_folder_path, random_sound_file)


    # Get a random video #

    videos_path = 'Videos'

    video_folder_path = os.path.join(project_directory, videos_path)

    # Get a list of all the files in the folder
    video_files = [f for f in os.listdir(video_folder_path) if os.path.isfile(os.path.join(video_folder_path, f))]

    # Choose a random file from the list
    random_video_file = random.choice(video_files)

    # Get the path to the random file
    video_file = os.path.join(video_folder_path, random_video_file)

    # Find the shortest length between the video and the sound file (so we can cut it)
    shortest_length = get_shortest_length(video_file, sound_file)

    # Load the video
    cap = cv2.VideoCapture(video_file)

    # Get the frame rate of the video
    fps = cap.get(cv2.CAP_PROP_FPS)


    # Define the codec and create VideoWriter object
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter('output.mp4', fourcc, fps,
                        (int(cap.get(3)), int(cap.get(4))))


    frame_path = os.path.join(project_directory, "Engine/Temp/frame.jpg")
    # Read frames from video and add text
    while (cap.isOpened()):
        ret, frame = cap.read()
        if ret:
            # Write the frame to the output file
            cv2.imwrite(frame_path, frame)
            
            # For each frame wait 0.25 seconds for it to be processed
            time.sleep(0.25)

            # Open the frame
            frame = Image.open(frame_path)
            
            # Add the text to the frame
            frame = add_subtitle(frame, text, author)
            
            # Save the frame
            frame.save(frame_path)

            # Read the frame
            frame = cv2.imread(frame_path)
            
            # Write the frame to the output file
            out.write(frame)
        else:
            break

    # Release the objects
    cap.release()
    out.release()

    output_video_path = os.path.join(project_directory, "Engine/Temp/output.mp4")
    # Load the video clip
    video = VideoFileClip(output_video_path)

    # Load the audio clip
    audio = AudioFileClip(sound_file)

    # Overlay the audio on the video
    final_video = video.set_audio(audio)


    video_with_music_path = os.path.join(project_directory, "Engine/Temp/video_with_music.mp4")
    # Write the final video to disk
    final_video.write_videofile(video_with_music_path)


    # Get the absolute path of the current Python script
    current_script_path = os.path.abspath(__file__)

    # Get the directory containing the current script
    current_directory = os.path.dirname(current_script_path)

    # Navigate up the directory tree until you reach the project directory
    project_directory = current_directory
    while not os.path.basename(project_directory) == 'silent_autopost':
        project_directory = os.path.dirname(project_directory)

    # Define the relative path to your file within the project directory
    relative_path_to_video_with_music = 'Engine/Temp/video_with_music.mp4'
    relative_path_to_output_video = 'Output/final_video.mp4'


    # Construct the absolute path by joining the project directory and the relative path
    absolute_path_to_video_with_music = os.path.join(project_directory, relative_path_to_video_with_music)
    absolute_path_to_output_video = os.path.join(project_directory, relative_path_to_output_video)

    print(absolute_path_to_output_video)
    print(absolute_path_to_video_with_music)


    # Cut the video to the shortest length
    cut_video(absolute_path_to_video_with_music, shortest_length, absolute_path_to_output_video)

    cv2.destroyAllWindows()