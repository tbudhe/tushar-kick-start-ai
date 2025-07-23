from openai import OpenAI
import os
from dotenv import load_dotenv

# Load environment variables from .envrc or .env
load_dotenv(dotenv_path=".envrc")
api_key = os.getenv("OPENAI_API_KEY")
print(f"API Key: {api_key}")  # Debugging line to check if the key is loaded
if not api_key:
    raise ValueError(
        "API key not found. Please set the OPENAI_API_KEY environment variable.")
client = OpenAI( api_key=api_key)

response = client.responses.create(
    model="gpt-4o-mini",
    input="write a haiku about ai",
    store=True,
)

print(response.output_text)
