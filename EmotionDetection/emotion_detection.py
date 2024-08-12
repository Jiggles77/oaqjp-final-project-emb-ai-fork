import requests
import json

def emotion_detector(text_to_analyze):
    URL = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_json = {"raw_document": {"text": text_to_analyze}}
    response = requests.post(URL, json=input_json, headers=header)

    if response.status_code == 200:
        formated_response = response.json()
        emotion = formated_response['emotionPredictions'][0]['emotion']
        
        dominant_emotion = None
        dominant_emotion_value = 0

        for item, value in emotion.items():
            if value > dominant_emotion_value:
                dominant_emotion_value = value
                dominant_emotion = item

        emotion['dominant_emotion'] = dominant_emotion
        
        return emotion
    
    elif response.status_code == 400:
        return {
            'anger': None,
            'disgust': None, 
            'fear': None, 
            'joy': None, 
            'sadness': None, 
            'dominant_emotion': None
        }
