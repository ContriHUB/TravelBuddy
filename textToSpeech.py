import os
import sys
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "Path-to-Credentials-file"

from gtts import gTTS
from playsound import playsound

def text_to_speech(text, output_file):
    source_language = sys.argv[1] #take input of source language as first command line argument
    tts = gTTS(text=text, lang=source_language)  # Specify the language (e.g., 'en' for English)
    tts.save(output_file)
    playsound(output_file)

# Example usage
#text = "What is job"
#output_file = "output.mp3"

