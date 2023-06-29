import subprocess


# Cut video from start_time to start_time+duration
def cut_video(video_path, length, output_path):
    start_time = 0
    duration = length

    # Uses ffmpeg to cut video, must install manually
    command = [
        "ffmpeg",
        "-y",
        "-loglevel",
        "error",
        "-i",
        video_path,
        "-t",
        str(duration),
        "-c",
        "copy",
        "-avoid_negative_ts",
        "1",
        output_path,
    ]

    subprocess.run(command, check=True)
