"""Required packages"""
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector


app = Flask("__main__")


@app.route('/emotionDetector', methods=['GET', 'POST'])
def emotedetect():
    """Text analyzer method"""
    text_to_analyse = request.args.get('textToAnalyze')
    result = emotion_detector(text_to_analyse)
    if result is None:
        return "Invalid text! Please try again!"
    return result


@app.route('/')
def main():
    """Main fumction for rendering page"""
    return render_template("index.html", responseText="asdf")

if __name__ == "__main__":
    app.run(debug=True)
