import requests
import json

def emotion_detector(text_to_analyse):
    """Function for analyzing text"""
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_json = { "raw_document": { "text": text_to_analyse } }
    response = requests.post(url, json = input_json, headers = headers)
    if response.status_code == 200:
        response = response.json()
        emotions = response['emotionPredictions'][0]['emotion']
        dom_emo = ["", 0]
        for k,v in emotions.items():
            if v > dom_emo[1]:
                dom_emo[0]=k
                dom_emo[1] = v
        emotions['dominant_emotion'] = dom_emo[0]
        res_str = f"For the given statement, the system response is <b>{emotions['dominant_emotion']}</b>: <br>"
        for k,v in emotions.items():
            res_str+=f"{k}: {v}<br>"
    else:
        res_str = None
    return res_str