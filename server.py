''' Executing this function initiates the application of emotion
    detection to be executed over the Flask channel and deployed on
    localhost:5000.
'''
from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route("/emotionDetector")
def analyze_emotion():
    ''' This function takes the text input and send it to emotion_detector
        to analyze the emotion of the user '''
    text_to_analyze = request.args["textToAnalyze"]

    emotions = emotion_detector(text_to_analyze)
    if emotions["dominant_emotion"] is None:
        return ' Invalid text! Please try again!.'

    return f'For the given statement, the system response is "anger": {emotions["anger"]},\
            "disgust": {emotions["disgust"]},\
            "fear": {emotions["fear"]},\
            "joy": {emotions["joy"]}\
            and "sadness": {emotions["sadness"]}.\
            The dominant emotion is {emotions["dominant_emotion"]}.'

@app.route("/")
def render_index_page():
    ''' This function renders the home page of the application '''
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000)
