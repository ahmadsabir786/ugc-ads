from openai import OpenAI
import os

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_script(product_description):
    prompt = f"""
    Create a 20-second UGC-style marketing script.
    Product details: {product_description}
    Include:
    - 3 second hook
    - Natural tone
    - Clear CTA
    """

    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content
