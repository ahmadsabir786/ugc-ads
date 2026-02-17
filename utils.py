from moviepy.editor import AudioFileClip

def get_audio_duration(audio_path):
    audio = AudioFileClip(audio_path)
    duration = audio.duration
    audio.close()
    return duration
