from flask import Flask, render_template, request
import speech_recognition as sr
import os

app = Flask(__name__)

# Directory where you want to save the text file
output_directory = "output_texts"

# Create the output directory if it doesn't exist
if not os.path.exists(output_directory):
    os.makedirs(output_directory)

# Initialize recognizer class (for recognizing the speech)
r = sr.Recognizer()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/record', methods=['POST'])
def record():
    with sr.Microphone() as source:
        print("Talk")
        
        # Adjust the timeout (in seconds) according to your preference
        audio_text = r.listen(source, timeout=5)
        
        print("Time over, thanks")

    # Recognize the speech
    try:
        # Using Google Speech Recognition
        recognized_text = r.recognize_google(audio_text)
        print("Text: " + recognized_text)
        
        # Save the recognized text to a file
        output_file_path = os.path.join(output_directory, "recognized_text.txt")
        with open(output_file_path, "w") as f:
            f.write(recognized_text)
        print(f"Recognized text saved to: {output_file_path}")
        
        return recognized_text
        
    except sr.UnknownValueError:
        print("Sorry, I did not get that")
        return "Sorry, I did not get that"
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")
        return f"Could not request results from Google Speech Recognition service; {e}"

if __name__ == '__main__':
    app.run(debug=True)
