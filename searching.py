import pyttsx3
import speech_recognition as sr
import wikipedia
import pywhatkit as kit
import webbrowser


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

def speakwithout(audio):
    engine.say(audio)                               #speak function
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






def searchGoogle(self):
    if "google" in self.query:
        self.query = self.query.replace("Anna" , "")
        self.query = self.query.replace("google search", "")
        self.query = self.query.replace("google", "")
        speakwithout("this is what i found on google")

        try:
          kit.search(self.query)
          result = wikipedia.summary(self.query,1)
          speak(result)
        except:
         speak("no speakable output available")

def searchyoutube(self):
    if "youtube" in self.query:
        speakwithout("this is what i found for your search!")
        self.query = self.query.replace("youtube search ", "")
        self.query = self.query.replace("youtube" , "")
        self.query = self.query.replace("Anna" , "")
        web = "https://www.youtube.com/results?search_query=" + self.query
        webbrowser.open(web)
        kit.playonyt(self.query)
        speak("Done, sir")

def searchwikipedia(self):
    if "wikipedia" in self.query:
        speak("Searching from wikipedia...")
        self.query = self.query.replace("Anna" , "")
        self.query = self.query.replace("wikipedia" , "")
        self.query = self.query.replace("search wikipedia" , "")
        results = wikipedia.summary(self.query , sentences=2)
        speak("According to wikipedia")
        speak(results)