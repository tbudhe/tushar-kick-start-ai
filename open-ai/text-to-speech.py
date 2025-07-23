from openai import OpenAI
import os
from dotenv import load_dotenv
from pathlib import Path
# Load environment variables from .envrc or .env
load_dotenv(dotenv_path=".envrc")
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise ValueError(
        "API key not found. Please set the OPENAI_API_KEY environment variable.")
client = OpenAI(api_key=api_key)

speech_file_path = Path(__file__).parent / "out-puts/output.mp3"
if speech_file_path.exists():
    speech_file_path.unlink()  # Remove the existing file if it exists


with client.audio.speech.with_streaming_response.create(
    model="gpt-4o-mini-tts",
    voice="coral",
    input="Today is a wonderful day to build something people love!",
    instructions="Speak in a cheerful and positive tone.",
) as response:
    response.stream_to_file(speech_file_path)
