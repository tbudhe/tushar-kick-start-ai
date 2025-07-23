from openai import OpenAI
import os
from dotenv import load_dotenv

# Load environment variables from .envrc or .env
load_dotenv(dotenv_path=".envrc")
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise ValueError(
        "API key not found. Please set the OPENAI_API_KEY environment variable.")
client = OpenAI( api_key=api_key)
completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Write a motivational message for set of learner, learning about AI and ML."},
    ],
    store=True)
print(completion.choices)
print(completion.choices[0].message.content)