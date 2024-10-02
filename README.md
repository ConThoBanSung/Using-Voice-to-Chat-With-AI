# Voice to Chat

This project is a web-based application that recognizes speech input, sends the recognized text to the Gemini AI model for processing, and displays the result on a user-friendly UI. The backend uses Flask to handle speech recognition and the Gemini API, while the frontend is built with React to provide a clean and responsive user interface.

## Table of Contents

- [Features](#features)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [Folder Structure](#folder-structure)
- [Acknowledgements](#acknowledgements)

## Features

- **Speech Recognition**: Allows the user to speak through their microphone and converts the speech to text using Google Speech Recognition API.
- **AI-Powered Response**: Sends the recognized text to Gemini AI and displays the response in the UI.
- **Markdown Output**: AI responses are rendered in markdown format, allowing for clean, formatted text output.
- **Responsive Design**: The frontend is fully responsive and works well on both desktop and mobile devices.

## Technologies Used

- **Backend**: Flask, SpeechRecognition, Google Gemini API
- **Frontend**: React, React Markdown
- **Other Dependencies**: Flask-CORS for cross-origin resource sharing, `speech_recognition` for handling audio input, and `google.generativeai` for integrating with Gemini.

## Installation

### Prerequisites

- **Python** (>=3.7)
- **Node.js** (>=14)
- **npm** or **yarn**

### Backend Setup

1. Clone the repository:
    ```bash
    git clone <repository-url>
    cd <repository-folder>/backend
    ```

2. Create a virtual environment and activate it:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3. Install the required Python dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Start the Flask server:
    ```bash
    python main.py
    ```

### Frontend Setup

1. Go to the `frontend` directory:
    ```bash
    cd ../frontend
    ```

2. Install the required dependencies:
    ```bash
    npm install
    ```

3. Start the React application:
    ```bash
    npm start
    ```

The frontend will run on `http://localhost:3000` by default, and the backend on `http://localhost:5000`.

## Configuration

- **Gemini API Key**: You need to configure your API key for Gemini in the backend. Replace the placeholder API key in `main.py`:

    ```python
    genai.configure(api_key="YOUR_GEMINI_API_KEY")
    ```

    Make sure you have a valid API key from Google Gemini.

## Usage

1. Open your browser and navigate to `http://localhost:3000`.
2. Click on the **Start Speech Recognition** button.
3. Speak into your microphone when prompted.
4. The recognized speech will be sent to the Gemini AI model, and the response will be displayed in the **Gemini Response** section.

## Folder Structure

