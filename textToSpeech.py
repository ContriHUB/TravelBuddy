import os
import sys
import datetime
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "Path-to-Credentials-file"

from gtts import gTTS
from playsound import playsound


def get_file_name(file_name):
    directory = 'outputs' #output directory name: outputs
    output_directory = os.path.join(os.getcwd(), directory) 
    
    if not os.path.exists(output_directory):
        os.makedirs(output_directory, exist_ok=True)
    
    file_name = directory + '/' + file_name
    
    # if file already exists, rename it with timestamp
    if os.path.isfile(file_name):
        timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
        new_file_name = file_name.split(".mp3")[0] + "_" + timestamp + ".mp3"
        while os.path.isfile(os.path.join(output_directory, new_file_name)):
            timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
            new_file_name = file_name.split(".mp3")[0] + "_" + timestamp + ".mp3"
        file_name = new_file_name
    
    return file_name

def text_to_speech(text, output_file):
    source_language = sys.argv[1] #take input of source language as first command line argument
    tts = gTTS(text=text, lang=source_language)  # Specify the language (e.g., 'en' for English)
    file_name = get_file_name(output_file)
    tts.save(file_name)
    playsound(file_name)

# Example usage
#text = "What is job"
#output_file = "output.mp3"

