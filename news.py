import json
import pyttsx3
import requests



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









def Allnews(self):
    api_dict = {"business":"https://newsapi.org/v2/top-headlines?country=in&category=business&apiKey=a6196c481ea74d638dbe904c141539f0",
                "entertainment":"https://newsapi.org/v2/top-headlines?country=in&category=entertainment&apiKey=a6196c481ea74d638dbe904c141539f0",
                "health":"https://newsapi.org/v2/top-headlines?country=in&category=health&apiKey=a6196c481ea74d638dbe904c141539f0",
                "science":"https://newsapi.org/v2/top-headlines?country=in&category=science&apiKey=a6196c481ea74d638dbe904c141539f0",
                "sports":"https://newsapi.org/v2/top-headlines?country=in&category=sports&apiKey=a6196c481ea74d638dbe904c141539f0",
                "technology":"https://newsapi.org/v2/top-headlines?country=in&category=technology&apiKey=a6196c481ea74d638dbe904c141539f0"
                }
    content = None
    url = None
    speak("Which field news do you want, [business] , [health] , [technology] , [sports] , [entertainment] , [science]")
    field = input("Type field news that you want:- ")
    for key , value in api_dict.items():
        if key.lower() in field.lower():
            url = value
            print(url)
            print("url was found")
            break
        else:
            url = True
    if url is True:
         print("url not found")
    
    news = requests.get(url).text
    news = json.loads(news)
    speak("Here is the first news.")

    arts = news["articles"]
    for articles in arts:
        article = articles["title"]
        print(article)
        speak(article)
        news_url = articles["url"]
        print(f"For more info visit:- {news_url}")

        a = input("[press 1 to count] and [press 2 to stop]")
        if str(a) == "1":
           pass
        elif str(a)== "2":
          break
    speak("Thats all")