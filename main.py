from vision import analyze_image
from script import generate_script
from voice import generate_voice
from utils import get_audio_duration
from video import generate_video_scene
from merger import merge_audio_video

def run_pipeline(image_path):
    print("Analyzing image...")
    product_info = analyze_image(image_path)

    print("Generating script...")
    script = generate_script(product_info)

    print("Generating voice...")
    voice_path = generate_voice(script)

    duration = get_audio_duration(voice_path)
    print(f"Voice duration: {duration}")

    print("Generating video...")
    video_prompt = f"Create UGC style ad showing product in natural setting."
    video_path = generate_video_scene(video_prompt, duration, "video.mp4")

    print("Merging...")
    merge_audio_video(video_path, voice_path, "final_output.mp4")

    print("Done!")

if __name__ == "__main__":
    run_pipeline("product.jpg")
