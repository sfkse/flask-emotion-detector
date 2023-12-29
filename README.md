# Flask Emotion Detector

The Flask Emotion Detector is a web application that utilizes Natural Language Processing (NLP) to analyze emotions in text. Built with Flask, this application provides a simple interface for users to input text and receive an analysis of the dominant emotion present in the text.

## Features

- **Emotion Analysis**: Leverages NLP to detect emotions such as anger, disgust, fear, joy, and sadness in text.
- **Flask Web Server**: Utilizes Flask, a lightweight WSGI web application framework, to handle requests and responses.
- **Interactive UI**: Offers a user-friendly interface for inputting text and viewing the emotion analysis results.
- **Unit Testing**: Includes unit tests for the emotion detection functionality.

## Getting Started

### Prerequisites

- Python
- Flask

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/sfkse/flask-emotion-detector.git
   ```
2. Navigate to the project directory:
   ```bash
   cd flask-emotion-detector
   ```
3. Install the required Python packages:
   ```bash
   pip3 install -r requirements.txt
   ```

### Running the Application

Start the Flask server:

```bash
python3 server.py
```

The application will be available at http://localhost:5000.

## Usage

- Navigate to http://localhost:5000 in your web browser.
- Enter the text you want to analyze in the provided text area.
- Click the "Run Sentiment Analysis" button to view the emotion analysis results.

## Testing

Run the unit tests to ensure the emotion detection functionality is working as expected:

1. Navigate to the package directory::

```bash
cd EmotionDetection
```

1. Run the tests:

```bash
python3 test_emotion_detection.py
```

## Contributing

Contributions to the Flask Emotion Detector are welcome! Feel free to fork the repository, make changes, and submit pull requests. If you find any issues or have suggestions, please open an issue in the GitHub repository.

