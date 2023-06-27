import moviepy.editor as mp

def get_shortest_length(video_file, sound_file):
    video = mp.VideoFileClip(video_file)
    audio = mp.AudioFileClip(sound_file)
    video_length = video.duration
    audio_length = audio.duration

    if video_length < audio_length:
        if video_length > 15:
            return 15
        else:
            return video_length
    else:
        if audio_length > 15:
            return 15
        else:
            return audio_length