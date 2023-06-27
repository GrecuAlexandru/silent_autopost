import subprocess

def cut_video(video_path, length, output_path):
    start_time=0
    duration=length

    command = [
        'ffmpeg',
        '-y',
        '-loglevel', 'error',
        '-i', video_path,
        '-t', str(duration),
        '-c', 'copy',
        '-avoid_negative_ts', '1',
        output_path
    ]

    subprocess.run(command, check=True)
    