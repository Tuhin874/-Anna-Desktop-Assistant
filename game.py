import pyttsx3
import speech_recognition as sr
import random


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

def game_play(self):
     speak("Let's Play ROCK PAPER SCISSOR !! ")
     i = 0
     my_score = 0
     com_score = 0

     while(i<5):
          choose = ("rock","paper","scissor")
          com_choose = random.choice(choose)
          speak("choose one from  rock , paper and scissors")
          self.query = self.takecommand().lower()
          if (self.query == "rock"):
               if(com_choose == "rock"):
                    speak("rock")
                    speak("it's a tie")
                    print(f"Your Score is :- {my_score} :Computer Score is :-  {com_score}")
               elif(com_choose == "paper"):
                    speak("paper")
                    speak("i won , one point for me")
                    com_score += 1
                    print(f"Your Score is :- {my_score} :Computer Score is :-  {com_score}")
               else:
                    speak("scissor")
                    my_score +=1
                    speak("you won , one point for you")
                    print(f"Your Score is :- {my_score} :Computer Score is :-  {com_score}")

          elif (self.query == "paper"):
               if(com_choose == "rock"):
                    speak("rock")
                    speak("you won , one point for you")
                    my_score +=1
                    print(f"Your Score is :- {my_score} :Computer Score is :-  {com_score}")
               elif(com_choose == "paper"):
                    speak("paper")
                    speak("it's a tie")
                    print(f"Your Score is :- {my_score} :Computer Score is :-  {com_score}")
               else:
                    speak("scissor")
                    speak("i won , one point for me")
                    com_score +=1
                    print(f"Your Score is :- {my_score} :Computer Score is :-  {com_score}")

          elif (self.query == "scissors" or self.query == "scissor"):
               if(com_choose == "rock"):
                    speak("rock")
                    speak("i won , one point for me")
                    com_score +=1
                    print(f"Your Score is :- {my_score} :Computer Score is :-  {com_score}")
               elif(com_choose == "paper"):
                    speak("paper")
                    speak("you won , one point for you")
                    my_score +=1
                    print(f"Your Score is :- {my_score} :Computer Score is :-  {com_score}")
               else:
                    speak("scissor")
                    speak("it's a tie")
                    print(f"Your Score is :- {my_score} :Computer Score is :-  {com_score}")
          i +=1
     print(f"FINAL SCORES ARE :- {my_score} : com :-  {com_score}")
     if (my_score>com_score):
          speak("you won the final")
     elif(my_score<com_score):
          speak("you lose , try again")


     # elif "no" in gt:
     #      speak("so what you want to play sir")
     #    #   speak("i can play .........this games only") 