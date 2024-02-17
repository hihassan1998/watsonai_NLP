from flask import Flask, render_template, request, jsonify
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/emotionDetector', methods=['GET'])
def emotion_detector_route():
    if request.method == 'GET':
        statement = request.args.get('textToAnalyze', '')
        result = emotion_detector(statement)
        response_text = (
            f"For the given statement, the system response is 'anger': {result['anger']}, "
            f"'disgust': {result['disgust']}, 'fear': {result['fear']}, 'joy': {result['joy']} "
            f"and 'sadness': {result['sadness']}. The dominant emotion is {result['dominant_emotion']}."
        )

        return jsonify(response_text)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
