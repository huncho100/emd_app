import requests
import json

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
    }
    input_json = {
        "raw_document": {
            "text": text_to_analyze
        }
    }

    response = requests.post(url, headers=headers, json=input_json)
    response_data = response.json()

    # Extract the emotion predictions from the response
    emotion_predictions = response_data.get('emotionPredictions', [])

    if emotion_predictions:
        emotions = emotion_predictions[0].get('emotion', {})
        # Check if the emotions dictionary is not empty
        if emotions:
            # Extract required emotions and their scores
            anger = emotions.get('anger', 0)
            disgust = emotions.get('disgust', 0)
            fear = emotions.get('fear', 0)
            joy = emotions.get('joy', 0)
            sadness = emotions.get('sadness', 0)

            # Find the dominant emotion
            dominant_emotion = max(emotions, key=emotions.get)

            # Return the formatted output
            return {
                'anger': anger,
                'disgust': disgust,
                'fear': fear,
                'joy': joy,
                'sadness': sadness,
                'dominant_emotion': dominant_emotion
            }
        else:
            return 'No emotions found'
    else:
        return 'No emotion predictions found'

# Test the application
#text = "I am so happy I am doing this."
#result = emotion_detector(text)
#print(result)