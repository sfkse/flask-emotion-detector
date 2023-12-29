import requests
import json

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    myobj = { "raw_document": { "text": text_to_analyze } }
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    response = requests.post(url, json = myobj, headers=header)
    emotions = dict()
    if response.status_code == 400:
        emotions["anger"] = None
        emotions["disgust"] = None
        emotions["fear"] = None
        emotions["joy"] = None
        emotions["sadness"] = None
        emotions["dominant_emotion"] = None
    else:    
        formatted_response = json.loads(response.text)
        emotions = formatted_response["emotionPredictions"][0]["emotion"]
        emotions["dominant_emotion"] = max(emotions, key=emotions.get)
    modified_response = {
        'anger': emotions["anger"],
        'disgust': emotions["disgust"],
        'fear': emotions["fear"],
        'joy': emotions["joy"],
        'sadness': emotions["sadness"],
        'dominant_emotion': emotions["dominant_emotion"]
    }
    return modified_response
