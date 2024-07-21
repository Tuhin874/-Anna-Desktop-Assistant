from time import sleep
from googletrans import Translator
import googletrans
from gtts import gTTS
import pyttsx3
import speech_recognition as sr
import os
from playsound import playsound
import time


engine = pyttsx3.init()
voices = engine.getProperty('voices')
#print(voices[0].id)                               #taking voices
engine.setProperty('voice', voices[1].id)
# engine.setProperty('rate',20) #To slow down(0 - 100) and fast the voice speed(100 - 200)


def speak(audio):
    engine.say(audio)
    print(audio)                                #speak function
    engine.runAndWait()
    engine.setProperty('volume' , 1.0)


def takecommand(self):
        r = sr.Recognizer()
        with sr.Microphone() as source:                #taking commands from user
            print("listening...")
            r.pause_threshold = 0.8
            audio= r.listen(source)

        try:
            print("Recognizing...")
            self.query= r.recognize_google(audio, language='en-in') 
            print(f"user said: {self.query}")


        except Exception as e:
            # speak("say that again please...")
            return "none"
        return self.query



def translategl(self):
     speak("SURE SIR")
     print(googletrans.LANGUAGES)
     translator = Translator()
     speak("Choose the language in which you want to  translate")
     b = input("TO_Lang:- ")
     text_to_translate = translator.translate(self,src = "auto" , dest=b,)
     text = text_to_translate.text
     try:
          speakgl = gTTS(text=text, lang=b, slow=False)
          speakgl.save("voice.mp3")
          playsound("voice.mp3")

          time.sleep(5)
          os.remove("voice.mp3")
     except:
          print("Unable to translate")