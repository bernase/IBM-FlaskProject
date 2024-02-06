''' Executing this function initiates the application of sentiment
    analysis to be executed over the Flask channel and deployed on
    localhost:5000.
'''

from flask import Flask, jsonify, request
from EmotionDetection.emotion_detection import emotion_detector 

app = Flask("Emotion Detector")


@app.route("/emotionDetector", methods=["POST"])
def emotion_detector_route():
    '''
    Handle POST requests to the /emotionDetector endpoint.
    
    Analyzes the provided text for emotion and returns the result.
    '''

    try:
        text_to_analyze = request.json.get("text", "")
        result = emotion_detector(text_to_analyze)

        # Check if None
        if result['dominant_emotion'] is None:
            return jsonify({"error": "Invalid text! Please try again."})
        
        return jsonify(result)
    except Exception as e:
        return jsonify({"error": str(e)})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
