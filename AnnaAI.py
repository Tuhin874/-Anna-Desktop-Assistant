import operator
import sys
import pyttsx3
import  requests
import speech_recognition as sr
import datetime
import os                           #some usefull modules
import random
from requests import get
import webbrowser
import pywhatkit as kit
import time
import pyjokes
import datetime
import pyautogui
from bs4 import BeautifulSoup
from pywikihow import search_wikihow
import psutil
import speedtest
import random
from plyer import notification
import mixer
from pygame import mixer

from annagui1 import Ui_MainWindow



from PyQt5 import QtGui
from PyQt5.QtCore import QTimer, QTime, QDate, Qt
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

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


def wish():
    hour = int(datetime.datetime.now().hour)
    tt = time.strftime("%I:%M :%p")

    if hour>=0  and hour<=12:
        speak(f"Good Morning sir, it's {tt}")
    elif hour>12 and hour<18:
        speak(f"Good Afternoon sir, it's {tt}")    #wish function
    else:
        speak(f"Good Evening sir, it's {tt}")

    speak("now i am ready to help you")

def AllTask(self):
        while True:
           
           self.query = self.takecommand().lower()

################################CONVERSATIONS WITH ANNA ###############################
           if "hello anna" in self.query:
                   speak("hello sir,may i help you with something")

           elif "introduce yourself" in self.query or "who are you" in self.query:
               speak("my name is anna. i'm a digital assistant created by Tuhin ")
               time.sleep(0.8)
               speak("Done sir, do you have any other work")

           elif "how are you" in self.query:
               speak("i am fine, thank you sir and what about you")
               time.sleep(0.6)
           elif "not ok" in self.query or "not fine" in self.query:
                   speakwithout("why sir, what happened to you? you can share everything with me.")
                   time.sleep(0.6)
           elif "fine" in self.query:
                   speakwithout("that's good to hear")
                   time.sleep(0.8)
                   speak("sir, do you have any work")
           elif "thank you" in self.query or "thanks" in self.query:
                   speakwithout("you are welcome, sir")
                   time.sleep(0.8)
                   speak("sir, do you have any other work")
           elif "what can you do" in self.query:
                speak("  i  can  open  video , whatsapp , command  prompt , picture  and  i  can  do  calculations  and  much  more. Below  is  a  list  of  what  i  can  do ")
                print('''
               To open video----------------------------SAY-------------------open video
               To open command prompt-------------------SAY-------------------open command prompt
               To open picture--------------------------SAY-------------------open picture
               To hear Time-----------------------------SAY-------------------time
               To do calculation------------------------SAY-------------------do some calculation or can you calculate
               To open camera---------------------------SAY-------------------open camera
               To check battery-------------------------SAY-------------------how much power left or how much power we have
               To play song from folder ----------------SAY-------------------play song from folder
               To see ip address------------------------SAY-------------------ip address  
               To search on wikipedia-------------------SAY-------------------wikipedia(what you want to search)
               To open youtube--------------------------SAY-------------------open youtube
               To open google---------------------------SAY-------------------open google
               To open whatsapp-------------------------SAY-------------------open whatsapp
               To send message--------------------------SAY-------------------send message
               To play song on youtube------------------SAY------------------ play song on youtube
               To email to abhi-------------------------SAY-------------------email to abhi
               To temperature---------------------------SAY-------------------temperature
               To hear a joke---------------------------SAY-------------------tell me a joke
               To switch the window---------------------SAY-------------------switch the window
               To search live location------------------SAY-------------------where i am
               To know how to do something--------------SAY-------------------activate how to do mode
               To check the internet speed--------------SAY------------------ internet speed or data speed
               To sleep the program---------------------SAY-------------------you can sleep now
     ''')

##################################END OF CONVERSATIONS#############################################

           elif "open youtube"  in self.query or "start youtube"  in self.query:
               speak("sure sir....")
               speak("what do you want to search on youtube?")
               self.tt = self.takecommand().lower()
               speak("wait sir i am searching....")
               kit.playonyt(f"{self.tt}")
               time.sleep(2)
               speak("Do you have any other work")

           elif "open video" in self.query:             #you can give command here
               speak("sure sir....")
               vpath = "C:\\Users\\HP\\OneDrive\\Desktop\\video"
               os.startfile(vpath)
               time.sleep(2)
               speak("Do you have any other work")

           elif "picture" in self.query or "pictures" in self.query:
               speak("sure sir....")
               ppath = "C:\\Users\\HP\\OneDrive\\Pictures"
               os.startfile(ppath)
               time.sleep(2)
               speak("Do you have any other work")

##################################SEARCH GOOGLE , YOUTUBE , WIKIPEDIA########################################################################################################         
           elif "google" in self.query:
               from searching import searchGoogle
               searchGoogle(self)
           elif "youtube" in self.query:
               from searching import searchyoutube
               searchyoutube(self)
           elif "wikipedia" in self.query:
               from searching import searchwikipedia
               searchwikipedia(self)


################################## END  OF SEARCH GOOGLE , YOUTUBE , WIKIPEDIA########################################################################################################  

###########################################OPEN AND CLOSE ################################################################################################################################
           elif "open" in self.query:
               from openclose import openappweb
               openappweb(self)
           elif "close" in self.query:
               from openclose import closeappweb
               closeappweb(self)        
           

################################## END OF OPEN AND CLOSE ################################################################################################################################          



           elif "screenshot" in self.query:
               im = pyautogui.screenshot()
               im.save("ss.jpg")

           elif "click photo" in self.query:
               pyautogui.press("super")
               pyautogui.typewrite("camera")
               pyautogui.press("enter")
               pyautogui.sleep(3)
               speakwithout("SMILE SIR")
               pyautogui.press("enter")


           elif "translate" in self.query:
               from Translator import translategl
               self.query = self.query.replace("Anna","")
               self.query = self.query.replace("translate","")
               translategl(self)

           elif "temperature" in self.query:
               search = "temperature in alipurduar"
               url = f"https://www.google.com/search?q={search}"
               r = requests.get(url)
               data = BeautifulSoup(r.text,"html.parser")
               temp = data.find("div",class_="BNeawe").text
               speak(f"current{search} is {temp}")                                        #1
               time.sleep(2)
               speak("Do you have any other work")    

           elif "weather" in self.query:
               search = "temperature in alipurduar"
               url = f"https://www.google.com/search?q={search}"
               r = requests.get(url)
               data = BeautifulSoup(r.text,"html.parser")
               temp = data.find("div",class_="BNeawe").text
               speak(f"current{search} is {temp}")                                        #1
               time.sleep(2)
               speak("Do you have any other work")    


           elif "time" in self.query:
                   hour = int(datetime.datetime.now().hour)
                   t = time.strftime("%I:%M :%p")
                   speak(f"sir, the time is {t}")                                         #2

           elif "you can sleep" in self.query:
                   speak("i am going to sleep you can call me anytime.")                  #3
                   break
                   # sys.exit()
           
   
           elif "goodbye" in self.query or "good bye" in self.query:
               speak("goodbye sir, thanks for using me, have a good day")                 #4
               sys.exit()

           elif "play a game" in self.query:
               from game import game_play
               game_play(self)




        
           elif "play song" in self.query:
                music_dir = "D:\\music"
                songs = os.listdir(music_dir)
                rd = random.choice(songs)
                os.startfile(os.path.join(music_dir,rd))
                time.sleep(2)
                speak("Do you have any other work")


           elif "pause" in self.query:
               pyautogui.press("k")
               speakwithout("video paused sir")
           elif "play" in self.query:
               pyautogui.press("k")
               speakwithout("video played sir")
           elif "mute" in self.query:
               pyautogui.press("m")                                                        #5
               speakwithout("video muted sir")   
           elif "volume up" in self.query or "increase the volume" in self.query:
               from volumeupdown import volumeup
               speakwithout("Turning volume up, sir")
               volumeup()
           elif "volume down" in self.query or "decrease the volume" in self.query:
               from volumeupdown import volumedown
               speakwithout("Turning volume down, sir")
               volumedown()
               


           elif "remember that" in self.query:
               self.rememberMassage = self.query.replace("remember that","")
               self.rememberMassage = self.query.replace("Anna","")
               speak("you told me to "+self.rememberMassage)
               remember = open("Remember.txt","w")
               remember.write(self.rememberMassage)
               remember.close()
           elif "what do you remember" in self.query or "what I told you to remamber" in self.query or "what i told you to remember" in self.query:
               remember = open("Remember.txt","r")
               speak("you told me to "+remember.read())
              
           elif "tired" in self.query:
               speak("Playing your favourite songs,sir")
               a = (1,2,3)
               b = random.choice(a)
               if b==1:
                   webbrowser.open("https://www.youtube.com/watch?v=ZxpVR7aLrQM")

               elif b==2:
                   webbrowser.open("https://www.youtube.com/watch?v=S-ls2OzWEuI")
               elif b==3:
                   webbrowser.open("https://www.youtube.com/watch?v=CmHfWSxt0UQ")


           elif "tell me news" in self.query:
                   from news import Allnews
                   speak("please wait sir, feteching the latest news")
                   Allnews()


           elif "do some calculations" in self.query or "can you calculate" in self.query:
               r = sr.Recognizer()
               with sr.Microphone() as source:
                   speak("say what you want to calculate, example: 3 plus 3")
                   print("listening....")
                   r.adjust_for_ambient_noise(source)
                   audio = r.listen(source)
               my_string=r.recognize_google(audio)
               print(my_string)
               def get_operator_fn(op):
                   return{
                       '+'  : operator.add,
                       '-'  : operator.sub,
                       'x'  : operator.mul,
                       '/' : operator.__truediv__,              
                       }[op]
               def eval_binary_expr(op1, oper, op2):
                   op1,op2 = int(op1),int(op2)
                   return get_operator_fn(oper)(op1,op2)
               speak("your result is")
               speak(eval_binary_expr(*(my_string.split())))
               time.sleep(2)
               speak("Do you have any other work")

           elif "send message" in self.query:
               from whatsapp import sendmassage
               sendmassage(self)



           elif "shutdown the system" in self.query:
               os.system("shutdown /s /t 1")
           elif "restart the system" in self.query:
               os.system("shutdown -t 0 -r -f")
           elif "sleep the system" in self.query:
               os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")


           elif "schedule my day" in self.query:
               tasks = []
               speak("Do you want to clear old tasks(please speak yes or no)")
               self.query = self.takecommand().lower()
               if "yes" in self.query:
                   file = open("tasks.txt ", "w")
                   file.write(f"{i}. {tasks[i]}\n")
                   file.close()
                   no_tasks = int(input("Enter the no of tasks :- "))
                   i = 0
                   for i in range(no_tasks):
                       tasks.append(input("Enter the task:- "))
                       file = open("tasks.txt","a")
                       file.write(f"{i}. {tasks[i]}\n")
                       file.close()
               elif "no" in self.query:
                   i = 0
                   no_tasks = int(input("Enter the no of tasks :- "))
                   for i in range(no_tasks):
                       tasks.append(input("Enter the task:- "))
                       file = open("tasks.txt","a")
                       file.write(f"{i}. {tasks[i]}\n")
                       file.close()

               else:
                   speak("sorry sir i can't listening to you")
                   
           elif "show my schedule" in self.query:
               file = open("tasks.txt","r")
               content = file.read()
               file.close()
               mixer.init()
               mixer.music.load("notification.mp3")
               mixer.music.play()
               notification.notify(
                   title = "My schedule :-",
                   message = content,
                   timeout = 15
                   )
           elif "internet speed" in self.query or "data speed" in self.query:
               speak("wait , this will take a few seconds ")
               st = speedtest.Speedtest()
               st.get_best_server()
               dl =st.download()
               up =st.upload()
               dl_in_mb = dl/1000000  
               up_in_mb = up/1000000
               d = str(dl_in_mb)
               u = str(up_in_mb)   
               y = d[0:4]
               t = u[0:4]
               speak(f"sir we have {y} megabits per second downloading speed and {t} megabit per second uploading speed")
            
        #    elif "ipl score" in query or "Ipl score" in query:
        #        Funscore()

           elif "change the password" in self.query:
               speakwithout("Enter the new password")
               new_pw = input("Enter the new password:-  ")
               new_password = open("pw.txt","w")
               new_password.write(new_pw)
               new_password.close()
               speak("changing password...")
               speak(f"your new password is {new_pw}")



        #    elif "camera" in self.query:
                # speak("sure sir....")
                # cap = cv2.VideoCapture(0)
                # cap.set(cv2.CAP_PROP_FPS, 60)
                # cap.set(cv2.CAP_PROP_FRAME_WIDTH, 500)
                # cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 500)
                # while True:
                #     ret, img = cap.read()
                #     cv2.imshow('webcam',img)
                #     v = self.takecommand().lower()
                #     if "close camera" in v:
                #         break
                #     if cv2.waitKey(1) & 0xFF == ord('q'):
                #         break
                        
                # cap.release()
                # cv2.destroyAllWindows()
                # time.sleep(2)
                # speak("Do you have any other work")





        



   
   

             
           elif "how much power left" in self.query or "how much power we have" in self.query or "battery" in self.query:
               battery = psutil.sensors_battery()
               percentage = battery.percent
               speak(f"sir our system have {percentage} percent battery")
               if percentage>=75:
                   speak("we have enough power to continue our work")
                   time.sleep(2)
                   speak("Do you have any other work")
               elif percentage>=40 and percentage<=75:
                   speak("we should connect our system to charging point to charge our battery")
                   time.sleep(2)
                   speak("Do you have any other work")
               elif percentage>15 and percentage<30:
                   speak("we don't have enough power to work, please connect to charging")
                   time.sleep(2)
                   speak("Do you have any other work")
               elif percentage<=15:
                   speak("we have very low power, please connect to charging the system will shutdown very soon ")
                   time.sleep(2)
                   speak("Do you have any other work")
   

      
              
      
           elif "ip address" in self.query:
                ip = get('https://api.ipify.org').text
                speak("sure sir....")
                speak(f"your ip address is {ip}")
                time.sleep(2)
                speak("Do you have any other work")

           


 
              
        #    elif "email to abhi" in self.query:
        #        speak("sure sir....")
        #        try:
        #            speak("what should i say?")
        #            content = takecommand().lower()
        #            to = "sarkartuhin489@gmail.com"
        #            sendEmail(to,content)
        #            speak("Email has been send to abhi")
        #            time.sleep(2)
        #            speak("Do you have any other work")
        #        except Exception as e:
        #            print(e)
        #            speak("sorry sir i am not able to send this mail.")

                  
              
      
      
           # elif "close video" in self.query:
           #     speak("okay sir,closing video")
           #     os.system("taskkill /f /im video.exe")
       
           elif "tell me a joke" in self.query:
               joke = pyjokes.get_joke()
               speak(joke)
               time.sleep(2)
               speak("Do you have any other work")
           
      
           elif "switch the window" in self.query:
               speak("sure sir ")
               pyautogui.keyDown("alt")
               pyautogui.press("tab")
               time.sleep(1)
               pyautogui.keyUp("alt")
               time.sleep(2)
               speak("Do you have any other work")
      
      
           elif "where i am" in self.query or "where we are" in self.query:
               speak("wait sir, let me check")
               try:
                   ipAdd = requests.get('https://api.ipify.org').text
                   print(ipAdd)
                   url = 'https://get.geojs.io/v1/ip/geo/'+ipAdd+'.json'
                   geo_requests = requests.get(url)
                   geo_data = geo_requests.json()
                   city = geo_data['city']
                   country = geo_data['country']
                   speak(f"sir i am not sure,but i think we are in {city} city of {country} country")
                   time.sleep(2)
                   speak("Do you have any other work")
               except Exception as e:
                   speak("sorry sir, Due to network issue i am able to find where we are.")
                   time.sleep(2)
                   speak("Do you have any other work")
                   pass 
   
   
           elif "activate how to do mode " in self.query or "activate how to do mod" in self.query:
               speak("How to do mode is activated")
               while True:
                   speak("please tell me what you want to know")
                   self.how = self.takecommand().lower()
                   try:
                       if "exit" in self.how or "close" in self.how:
                           speak("okay sir, how to do mode is closed")
                           time.sleep(2)
                           speak("Do you have any other work")
                           break
                       else:
                           max_results = 1
                           how_to = search_wikihow(self.how,max_results)
                           assert len(how_to) == 1
                           how_to[0].print()
                           speak(how_to[0].summary)
                           speak("Do you have any other work")
                   except Exception as e:
                       speak("sorry sir, i am not able to find this")
                       time.sleep(1)
                       speak("Do you have any other work")

   
######################################END OF OPEN DO ENYTHING############################################################################################################  


           else:
               time.sleep(0.6)   


# def sendEmail(to,content):
#     server = smtplib.SMTP('smtp.gmail.com, 587')
#     server.ehlo()
#     server.starttls()
#     server.login('your email id','your password')  #send Email function
#     server.sendmail('your mail id', to , content)
#     server.close()

def new_func():
    return QThread

class MainThread(new_func()):
    def __init__(self):
        super(MainThread,self).__init__()
    
    def run(self):
        self.Execution()

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
    
    def Execution(self):
           if __name__ == "__main__":
                 
                 while True:
                     self.Permission = self.takecommand().lower()
                     if ("wake up" in self.Permission):
                         for i in range(3):
                             if (i==0):                 
                               speak("who is this? ")
                               self.gt = self.takecommand().lower()
                               if ("tuhin" in self.gt) :
                                   speakwithout("please Enter the security code  ")
                                   break
                               elif(i==0):
                                   speak("you are not my creator so i can't start my system")
                             else:
                              self.gt = self.takecommand().lower()
                              if ("tuhin" in self.gt) :
                                  speakwithout("please Enter the security code  ")
                                  break
                              elif(i==1):
                                  speak("you are not my creator so i can't start my system")
                              else:
                                  speak("you are not my creator  so good bye")
                                  sys.exit()                 
                         for i in range(3):
                                psw = input("please Enter the security code: ")
                                pw_file = open("pw.txt", "r")
                                pw = pw_file.read()
                                pw_file.close()
                                if (psw==pw):
                                        speak("Admin  Code Activated")
                                        wish()
                                        AllTask(self)
                                        break
                                elif (i==0 and psw!=pw):
                                    speak("wrong security code! try again you have 2 more attempts left")
                                elif(i==1 and psw!=pw):
                                    speak("wrong security code! try again you have 1 more attempts left")
                                else:
                                  speak("wrong security code! you don't have more attempts left")
                                  sys.exit()                 
                     elif "goodbye" in self.Permission or "good bye" in self.Permission:
                         speak("goodbye sir, thanks for using me, have a good day")
                         sys.exit()                 

startExecution = MainThread()

class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton_2.clicked.connect(self.startTask)
        self.ui.pushButton_3.clicked.connect(self.close)
    def startTask(self):
        self.ui.movie = QtGui.QMovie("..//T8bahf.gif")
        self.ui.label_3.setMovie(self.ui.movie)
        self.ui.movie.start()
        self.ui.movie = QtGui.QMovie("..//1689245822005.gif")
        self.ui.label_4.setMovie(self.ui.movie)
        self.ui.movie.start()
        self.ui.movie = QtGui.QMovie("..//200w.webp")
        self.ui.label_5.setMovie(self.ui.movie)
        self.ui.movie.start()
        self.ui.movie = QtGui.QMovie("..//1681295275020.gif")
        self.ui.label_9.setMovie(self.ui.movie)
        self.ui.movie.start()
        timer = QTimer(self)
        timer.timeout.connect(self.showTime)
        timer.start(1000)
        startExecution.start()
    
    def showTime(self):
        current_time = QTime.currentTime()
        current_date = QDate.currentDate()
        label_time = current_time.toString('hh:mm:ss')
        label_date = current_date.toString(Qt.ISODate)
        self.ui.textBrowser.setText(label_date)
        self.ui.textBrowser_2.setText(label_time)

app = QApplication(sys.argv)
anna = Main()
anna.show()
exit(app.exec_())