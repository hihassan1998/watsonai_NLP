"""
This module defines a Flask web application for emotion detection.
"""
from flask import Flask, render_template, request, jsonify
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route('/')
def index():
    """
    Render the index template.

    Returns:
        str: HTML content for the index page.    """
    return render_template('index.html')

@app.route('/emotionDetector', methods=['GET'])
def emotion_detector_route():
    """
    Handle the emotionDetector route for GET requests.

    Returns:
        str: JSON response containing emotion predictions or an error message.
    """
    if request.method == 'GET':
        statement = request.args.get('textToAnalyze', '')
        result = emotion_detector(statement)
        if result['dominant_emotion'] is None:
            response = jsonify({
                'error': 'Invalid text! Please try again.'
            })
    else:
        response_text = (
            f"For the given statement, the system response is 'anger': {result['anger']}, "
            f"'disgust': {result['disgust']}, 'fear': {result['fear']}, 'joy': {result['joy']} "
            f"and 'sadness': {result['sadness']}. "
            f"The dominant emotion is {result['dominant_emotion']}."
        )
        response = jsonify(response_text)

    return response

if __name__ == '__main__':
    app.run(debug=True, port=5001)
