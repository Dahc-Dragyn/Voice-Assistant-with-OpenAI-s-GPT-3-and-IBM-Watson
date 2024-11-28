import requests
import openai
import os
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

# Access the API keys
openai.api_key = os.getenv("OPENAI_API_KEY")
ibm_cloud_api_key = os.getenv("IBM_CLOUD_API_KEY")

def speech_to_text(audio_binary):
    """Transcribe speech from audio data to text."""

    # ... (Your speech_to_text implementation) ...


def openai_process_message(user_message):
    """Process a user message using the OpenAI API."""

    # ... (Your openai_process_message implementation) ...


def text_to_speech(text, voice=""):  # Correct indentation here
    """Convert text to speech using the Watson Text-to-Speech API."""

    # Set up Watson Text-to-Speech HTTP API URL
    base_url = 'https://sn-watson-tts.labs.skills.network'  # Use the provided URL
    api_url = f"{base_url}/text-to-speech/api/v1/synthesize?output=output_text.wav"

    # ... (The rest of your text_to_speech implementation) ...


