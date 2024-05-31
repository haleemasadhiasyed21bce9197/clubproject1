import speech_recognition as sr
from googletrans import Translator
from gtts import gTTS
from pydub import AudioSegment
from pydub.playback import play 

translator = Translator()
r = sr.Recognizer()

while True:
    with sr.Microphone() as source:
        print("Speak Now...")
        audio = r.listen(source)
        try:
            speech_text = r.recognize_google(audio , language="bn-BD")
            # print(speech_text)
            if(speech_text == "থাম"):
                break
        except sr.UnknownValueError:
            print("Could not interpret , Please try again...")
        except sr.RequestError:
            print("Can't request to API")

    trans_text = translator.translate(speech_text ,  dest='en')
    print(trans_text.text)


    voice = gTTS(trans_text.text , lang ='en')
    voice.save("translated_voice.mp3")
    audio = AudioSegment.from_mp3("translated_voice.mp3")
    play(audio)
    import os
    os.remove("translated_voice.mp3")
