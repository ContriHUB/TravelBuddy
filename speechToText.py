import speech_recognition as sr
import sys
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
        source_language = sys.argv[1] #take input of source language as first command line argument
        text = recognizer.recognize_google_cloud(audio, language=source_language)
        print(f"You said: {text}")
    except sr.UnknownValueError:
        print("I didn't understand what you said.")
    except sr.RequestError as e:
        print(f"Error: {e}")

    return text