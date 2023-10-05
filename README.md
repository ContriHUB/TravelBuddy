## TravelBuddy

TravelBuddy is a voice translation tool that uses Google's SpeechToText, TextToSpeech, and Translate APIs to translate voice from one language to another. It is written in Python and can be used to translate voice in real time.

## Getting Started

To get started with the project, you will need to follow these steps:

1. Clone the repository: `git clone https://github.com/admirerr/TravelBuddy.git`
2. Install the necessary packages: `pip install google-cloud-speech google-cloud-texttospeech google-cloud-translate`
3. Go to Google Console and create a new project. Enable `Cloud Speech-to-Text API`, `Cloud Text-to-Speech API` and `Cloud Translation API` in the Enabled APIs & services section.
4. Download the `credentials.json` file from Google Cloud Platform and place it in the root directory of the project. Remember to provide the location of this downloaded file in place of `Path-to-the-Credentials-file`.
5. Open terminal and run the model by using command `python translate.py`.


## Contributing

If you would like to contribute to TravelBuddy, you can follow these steps:

1. Fork the repository
2. Create a new branch: `git checkout -b new-feature`
3. Make your changes and commit them: `git commit -m "Add new feature"`
4. Push to the branch: `git push origin new-feature`
5. Create a pull request
