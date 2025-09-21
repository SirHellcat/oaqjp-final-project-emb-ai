"""
Flask application for emotion detection.
Provides a web interface and API endpoint to analyze text emotions.
"""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detection")


@app.route("/emotionDetector")
def emotion_detect():
    """
    Handle emotion detection requests.

    Returns:
        str: A formatted string with emotion scores and the dominant emotion,
        or an error message if the input is invalid.
    """
    text_to_analyze = request.args.get("textToAnalyze")
    response = emotion_detector(text_to_analyze)

    anger_score = response["anger"]
    disgust_score = response["disgust"]
    fear_score = response["fear"]
    joy_score = response["joy"]
    sadness_score = response["sadness"]
    dominant_emotion = response["dominant_emotion"]

    if dominant_emotion is None:
        return "Invalid text! Please try again!"

    response_out = (
        f"For the given statement, the system response is "
        f"'anger': {anger_score}, 'disgust': {disgust_score}, "
        f"'fear': {fear_score}, 'joy': {joy_score}, "
        f"and 'sadness': {sadness_score}. "
        f"The dominant emotion is {dominant_emotion}."
    )
    return response_out


@app.route("/")
def render_index_page():
    """
    Render the index page with the input form.
    """
    return render_template("index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
