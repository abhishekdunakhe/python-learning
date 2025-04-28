import speech_recognition as sr
import pyttsx3
import webbrowser, musicLibrary
import requests
r = sr.Recognizer()
engine = pyttsx3.init()
news_api_key = "671d6e09436d4b2782e11d42a34734ec"

def speak(text):
    engine.say(text)
    engine.runAndWait()

def proccedCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://www.google.com/")
    elif "open youtube" in c.lower():
        webbrowser.open("https://www.youtube.com/")
    elif "open linkedin" in c.lower():
        webbrowser.open("https://www.linkedin.com/")
    elif "open instagram" in c.lower():
        webbrowser.open("https://www.instagram.com/")
    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        link = musicLibrary.music[song]
        webbrowser.open(link)
    elif "news" in c.lower():
        r = requests.get("https://newsapi.org/v2/top-headlines?country=us&apiKey=671d6e09436d4b2782e11d42a34734ec")
        if r.status_code == 200:
            data = r.json()
            articles = data.get("articles", [])
            if articles:
                for index, article in enumerate(articles):
                    title = article.get('title', 'No title available')
                    speak(title)

if __name__ == "__main__":
    speak("Initializing alexa..!")
    while True:
        r = sr.Recognizer()
        print("Recognizing...")
        try:
            with sr.Microphone() as source:
                print("Listening...")
                audio = r.listen(source, timeout=2, phrase_time_limit=10)
            word = r.recognize_google(audio) #  pass the audio to google
            print(word)
            if word.lower() == "alexa":
                speak("yes..")
                with sr.Microphone() as source:
                    print("active alexa...")
                    audio = r.listen(source, timeout=4, phrase_time_limit=10) 
                    command = r.recognize_google(audio)
                    print(command)
                    proccedCommand(command)
                    
        except Exception as e:
            print(e)