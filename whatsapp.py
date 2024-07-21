import time
import pyttsx3
import pywhatkit as kit
import speech_recognition as sr

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


def sendmassage(self):
    speak("Sure sir")
    speak("Who do you want to massage")
    self.query = self.takecommand().lower()
    if "dad" in self.query:
        speak("what you want to message")
        self.uu = self.takecommand().lower()
        speak("wait for some time sir i am sending message.....")
        kit.sendwhatmsg("+919641059732",(f"{self.uu}"),2,25)
        time.sleep(2)
        speak("Do you have any other work")
    elif "didi" in self.query:
        speak("what you want to message")
        self.ue = self.takecommand().lower()
        speak("wait for some time sir i am sending message.....")
        kit.sendwhatmsg("+917319463869",(f"{self.ue}"),2,25)
        time.sleep(2)
        speak("Do you have any other work")
    else:
        speak("sorry sir but i can't hear you?")