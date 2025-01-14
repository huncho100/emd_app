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

    # Print the entire response JSON to inspect its structure
    print(response_data)

    # Extract the emotion predictions from the response
    emotion_predictions = response_data.get('emotionPredictions', [])

    if emotion_predictions:
        emotions = emotion_predictions[0].get('emotion', {})
        # Check if the emotions dictionary is not empty
        if emotions:
            return emotions
        else:
            return 'No emotions found'
    else:
        return 'No emotion predictions found'
