from flask import Flask, request, jsonify
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route('/emotionDetector', methods=['POST'])
def detect_emotion():
    data = request.get_json()
    text_to_analyze = data.get('text', '')

    if not text_to_analyze:
        return jsonify({"error": "No text provided"}), 400

    emotions = emotion_detector(text_to_analyze)

    # Format the response
    response = {
        "anger": emotions.get('anger', 0),
        "disgust": emotions.get('disgust', 0),
        "fear": emotions.get('fear', 0),
        "joy": emotions.get('joy', 0),
        "sadness": emotions.get('sadness', 0),
        "dominant_emotion": emotions.get('dominant_emotion', '')
    }

    # Create the output string as per the required format
    response_string = (f"For the given statement, the system response is 'anger': {response['anger']}, "
                       f"'disgust': {response['disgust']}, 'fear': {response['fear']}, 'joy': {response['joy']} "
                       f"and 'sadness': {response['sadness']}. The dominant emotion is {response['dominant_emotion']}.")

    return jsonify({"result": response_string})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
