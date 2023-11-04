from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route("/emotionDetector", methods=["POST"])
def emotion_wDetector():
    if request.method == 'POST':
        text_to_analyze = request.form['text']
        result = emotion_detector(text_to_analyze)
        
        if result['dominant_emotion'] is None:
            return "Invalid text! Please try again."
        
        return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
