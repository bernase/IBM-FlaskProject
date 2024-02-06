import json
import requests

def emotion_detector(text_to_analyze):
    #1
    if not text_to_analyze:
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        } 
    
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    jsonObj = { "raw_document": { "text": text_to_analyze } }
    response = requests.post(url, json=jsonObj, headers=headers)

    # checking if it's successful
    if response.status_code == 200:
        try:
            response_dict = json.loads(response.text)
            print("Response Dictionary:", response_dict)  # Print the response dictionary for debugging
            
            # Check the structure of the response
            if 'emotionPredictions' in response_dict and response_dict['emotionPredictions']:
                # Extract the first prediction (assuming there is at least one)
                first_prediction = response_dict['emotionPredictions'][0]
                
                emotions = first_prediction['emotion']
                dominant_emotion = max(emotions, key=emotions.get)

                # specified return format
                return {
                    'anger': emotions.get('anger', 0),
                    'disgust': emotions.get('disgust', 0),
                    'fear': emotions.get('fear', 0),
                    'joy': emotions.get('joy', 0),
                    'sadness': emotions.get('sadness', 0),
                    'dominant_emotion': dominant_emotion
                }
            else:
                print("Error: Unexpected response structure.")
                return None
        except json.JSONDecodeError as e:
            print(f"Error decoding JSON: {e}")
            return None
    elif response.status_code == 400:
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }
    else:
        print(f"Error: {response.status_code}")
        return None

if __name__ == "__main__":
    text_to_analyze = "I am so happy I am doing this."
    result = emotion_detector(text_to_analyze)
    print(result)
