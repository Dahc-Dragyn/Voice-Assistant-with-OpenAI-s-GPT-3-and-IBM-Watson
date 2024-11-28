# AI Voice Assistant with OpenAI and IBM Watson

This project demonstrates how to build a simple AI-powered voice assistant using OpenAI's GPT-3 and IBM Watson's Speech-to-Text and Text-to-Speech services.

## Features

*   **Speech-to-Text:** Converts spoken audio to text using IBM Watson.
*   **OpenAI Integration:** Sends the transcribed text to OpenAI's GPT-3 to generate a response.
*   **Text-to-Speech:** Converts the OpenAI response back to spoken audio using IBM Watson.
*   **Web Interface:** Provides a basic web interface for interacting with the assistant.

## Getting Started

### Prerequisites

*   Python 3.10 (or later)
*   OpenAI API key
*   IBM Cloud API key
*   Docker (optional, but recommended)

### Installation

1.  Clone the repository:

    ```bash
    git clone [invalid URL removed]
    ```

2.  Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3.  Set up environment variables:

    *   Create a `.env` file in the project root directory.
    *   Add your API keys to the `.env` file:

        ```
        OPENAI_API_KEY=your_actual_openai_api_key
        IBM_CLOUD_API_KEY=your_actual_ibm_cloud_api_key
        ```

### Running the application

1.  **Using Docker (recommended):**

    *   Build the Docker image:

        ```bash
        docker build . -t voice-assistant
        ```

    *   Run the Docker container:

        ```bash
        docker run -p 8000:8000 voice-assistant
        ```

2.  **Without Docker:**

    *   Run the Flask app directly:

        ```bash
        python server.py
        ```

### Usage

1.  Open the web interface in your browser (the URL will be provided when you run the app).
2.  Use the microphone button to record your voice input.
3.  The assistant will transcribe your speech, send it to OpenAI, and speak the response back to you.

## Project Structure

*   `server.py`: Flask backend for handling API requests.
*   `worker.py`: Worker functions for speech-to-text, text-to-speech, and OpenAI integration.
*   `templates/index.html`: HTML template for the web interface.
*   `static/`: Static files (CSS, JavaScript) for the web interface.
*   `Dockerfile`: Dockerfile for building the application image.
*   `requirements.txt`: Python dependencies.

## Contributing

Contributions are welcome! Feel free to open issues or submit pull requests.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
