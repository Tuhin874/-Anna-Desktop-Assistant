import os
import pyttsx3
import webbrowser
import pyautogui
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




dictapp1 ={"video" :"video" ,"command prompt":"cmd","notepad":"notepad","word":"winword","excel":"excel","chrome" or "google" or "google chrome":"chrome","vscode" or "vs code":"code","powerpoint":"powerpnt"}


def openappweb(self):
    if ".com" in self.query or ".co.in" in self.query or ".org" in self.query:
        self.query = self.query.replace("open","")
        self.query = self.query.replace("launch","")
        self.query = self.query.replace("anna","")
        self.query = self.query.replace(" ","")
        speak(f"opening {self.query} sir, please wait..")
        webbrowser.open(f"https://www.{self.query}")
        speak("Done sir, do you have any other work")

    else:
        self.query = self.query.replace("open","")
        self.query =self.query.replace("Anna","")
        self.query =self.query.replace("Anna open","")
        speak(f"opening {self.query} sir, please wait..")
        pyautogui.press("super")
        pyautogui.typewrite(self.query)
        pyautogui.sleep(2)
        pyautogui.press("enter") 

    # else:
    #     keys = list(dictapp1.keys())
    #     for app in keys:
    #         if app in self.query:
    #             os.system(f"start {dictapp1[app]}")

def closeappweb(self):
    speak("closing sir, please wait..")
    if "one tab" in self.query or "1 tab" in self.query:
        pyautogui.hotkey("ctrl" , "w")
        time.sleep(0.5)
        speak("All tabs closed")
        speak("Done sir, do you have any other work")
    elif "two tab" in self.query or "2 tab" in self.query:
        pyautogui.hotkey("ctrl" , "w")
        time.sleep(0.5)
        pyautogui.hotkey("ctrl" , "w")
        time.sleep(0.5)
        speak("All tabs closed")
        speak("Done sir, do you have any other work")
    elif "three tab" in self.query or "3 tab" in self.query:
        pyautogui.hotkey("ctrl" , "w")
        time.sleep(0.5)
        pyautogui.hotkey("ctrl" , "w")
        time.sleep(0.5)
        pyautogui.hotkey("ctrl" , "w")
        time.sleep(0.5)
        speak("All tabs closed")
        speak("Done sir, do you have any other work")
    elif "four tab" in self.query or "4 tab" in self.query:
        pyautogui.hotkey("ctrl" , "w")
        time.sleep(0.5)
        pyautogui.hotkey("ctrl" , "w")
        time.sleep(0.5)
        pyautogui.hotkey("ctrl" , "w")
        time.sleep(0.5)
        pyautogui.hotkey("ctrl" , "w")
        time.sleep(0.5)
        speak("All tabs closed")
        speak("Done sir, do you have any other work")
    elif "five tab" in self.query or "5 tab" in self.query:
        pyautogui.hotkey("ctrl" , "w")
        time.sleep(0.5)
        pyautogui.hotkey("ctrl" , "w")
        time.sleep(0.5)
        pyautogui.hotkey("ctrl" , "w")
        time.sleep(0.5)
        pyautogui.hotkey("ctrl" , "w")
        time.sleep(0.5)
        pyautogui.hotkey("ctrl" , "w")
        time.sleep(0.5)
        speak("All tabs closed")
        speak("Done sir, do you have any other work")
    else:
        keys = list(dictapp1.keys())
        for app in keys:
            if app in self.query:
                os.system(f"taskkill /f /im {dictapp1[app]}.exe")
                speak("Done sir, do you have any other work")
