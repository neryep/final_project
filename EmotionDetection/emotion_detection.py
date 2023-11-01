import requests
import json

def emotion_detector(text_to_analyse):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = { "raw_document": { "text": text_to_analyse } }
    response = requests.post(url, json=myobj, headers=headers)
    response_data = json.loads(response.text)
    
    #extract required emotions and scores
    emotions_data = response_data.get('emotionPredictions', []) #assumes the first prediction
    emotions = emotions_data[0].get('emotion', {})
    anger_score = emotions.get("anger", 0)
    disgust_score = emotions.get("disgust", 0)
    fear_score = emotions.get("fear", 0)
    joy_score = emotions.get("joy", 0)
    sadness_score = emotions.get("sadness", 0)

    #determine the dominant emotion
    emotions_scores = {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score
    }

    dominant_emotion = max(emotions_scores, key=emotions_scores.get)

    formatted_output = {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score,
        'dominant_emotion': dominant_emotion
    }

    return formatted_output