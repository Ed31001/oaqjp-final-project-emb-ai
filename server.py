"""import"""
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def emo_detector():
    """emotion detector"""
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)
    anger = response['anger']
    disgust = response['disgust']
    fear = response['fear']
    joy = response['joy']
    sadness = response['sadness']
    domin_emotion = response['dominant_emotion']

    if domin_emotion is None:
        return "Invalid text! Please try again!"

    return f"For the given statement, the system resonse is \
    'anger': {anger}, 'disgust': {disgust}, 'fear': {fear}, \
    'joy': {joy}, 'sadness': {sadness}. The dominant emotion is {domin_emotion}."

@app.route("/")
def render_index_page():
    """render index"""
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
