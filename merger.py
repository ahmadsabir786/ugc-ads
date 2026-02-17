from moviepy.editor import VideoFileClip, AudioFileClip, CompositeAudioClip

def merge_audio_video(video_path, voice_path, final_output):
    video = VideoFileClip(video_path)
    voice = AudioFileClip(voice_path)

    video = video.set_audio(voice)
    video.write_videofile(final_output, codec="libx264")

    video.close()
    voice.close()
