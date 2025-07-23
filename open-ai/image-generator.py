from openai import OpenAI
import os
from dotenv import load_dotenv
load_dotenv(dotenv_path=".envrc")
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise ValueError(
        "API key not found. Please set the OPENAI_API_KEY environment variable.")
client = OpenAI(api_key=api_key)
completion = client.images.generate(
    model="dall-e-3",
    prompt="A futuristic cityscape at sunset, with flying cars and neon lights, blending nature with advanced technology. The skyline features towering skyscrapers with greenery integrated into the architecture, and a vibrant sky filled with hues of orange, pink, and purple.",
    n=1,
    size="1024x1024",
    quality='standard',
    response_format="url"
)
# Print the URL of the generated image
print(f' total images : {len(completion.data)}')
print(completion.data[0].url)  # Print the URL of the generated image
