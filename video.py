import requests
import os

def generate_video_scene(prompt, duration, output_name):
    url = "YOUR_VIDEO_API_ENDPOINT"
    headers = {"Authorization": f"Bearer {os.getenv('VIDEO_API_KEY')}"}

    payload = {
        "prompt": prompt,
        "duration": duration
    }

    response = requests.post(url, json=payload, headers=headers)

    with open(output_name, "wb") as f:
        f.write(response.content)

    return output_name
