from google.cloud import translate_v2 as translate
import os
import sys
import speechToText
import textToSpeech

os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="Path-to-the-Credentials-file"

translate_client = translate.Client()
text = speechToText.spTtxt()

if isinstance(text, bytes):
    text = text.decode("utf-8")

# Text can also be a sequence of strings, in which case this method
# will return a sequence of results for each text.
target_language = sys.argv[2] #take input of target language as second command line argument
result = translate_client.translate(text, target_language=target_language)

print("Text: {}".format(result["input"]))
print("Translation: {}".format(result["translatedText"]))
print("Detected source language: {}".format(result["detectedSourceLanguage"]))


final = textToSpeech.text_to_speech(result["translatedText"], "output.mp3")