import speech_recognition as sr

import os
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="Path-to-Credentials-file"

def spTtxt() :
    # Create a recognizer
    recognizer = sr.Recognizer()

    # Initialize a microphone instance
    mic = sr.Microphone()

    # Start listening to the microphone
    with mic as source:
        recognizer.adjust_for_ambient_noise(source)
        print("Say something!")
        audio = recognizer.listen(source)

    # Recognize speech
    try:
        # Convert the audio to text
        text = recognizer.recognize_google_cloud(audio, language="hi")
        print(f"You said: {text}")
    except sr.UnknownValueError:
        print("I didn't understand what you said.")
    except sr.RequestError as e:
        print(f"Error: {e}")

    return text