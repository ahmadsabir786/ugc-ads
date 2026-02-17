from elevenlabs import generate, save, set_api_key
import os

set_api_key(os.getenv("ELEVENLABS_API_KEY"))

def generate_voice(script_text):
    audio = generate(
        text=script_text,
        voice="Rachel",
        model="eleven_monolingual_v1"
    )

    output_path = "voice.mp3"
    save(audio, output_path)
    return output_path
