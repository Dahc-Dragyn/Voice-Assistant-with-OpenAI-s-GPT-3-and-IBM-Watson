import os
import json
from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
from dotenv import load_dotenv
import openai
from worker import speech_to_text, text_to_speech, openai_process_message

# Load environment variables
load_dotenv()

# Initialize Flask app
app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

# Ensure the OpenAI API key is set
openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route('/', methods=['GET'])
def index():
    """Render the index.html template."""
    return render_template('index.html')

@app.route('/speech-to-text', methods=['POST'])
def speech_to_text_route():
    """Process speech-to-text."""
    audio_data = request.files.get('audio')
    if not audio_data:
        return jsonify({"error": "No audio data provided"}), 400
    result = speech_to_text(audio_data.read())
    return jsonify({"text": result})

@app.route('/process-message', methods=['POST'])
def process_message_route():
    """Process user message and return OpenAI response."""
    data = request.get_json()
    user_message = data.get("message")
    if not user_message:
        return jsonify({"error": "No message provided"}), 400
    response_text = openai_process_message(user_message)
    return jsonify({"openaiResponseText": response_text})

if __name__ == "__main__":
    app.run(port=8000, host='0.0.0.0')

