
import pyttsx3 #pip install pyttsx3 OR pip install -U pyttsx3=2.71
import speech_recognition as sr #pip install speech Recognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import smtplib
import os

engine = pyttsx3.init('sapi5') # Use to speak AI
voices = engine.getProperty('voices')
#print(voices[0].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):  #speak function
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")
    
    else:
        speak("Good Evening")

    speak("I am Sophia sir. Please tell me how may I help you")

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        #audio = r.listen(source, phrase_time_limit=10)
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print(e)
        print("Say that again please...")
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gamil.com', 587)
    server.ehlo()
    server.starttls()
    server.login('agarwalnav0@gmail.com', 'your-password')
    server.sendmail('agarwalnav0@gmail.com', to, content)
    server.close()

if __name__ == "__main__":
    #speak("Naveen is a good boy")
    wishMe()
    while True:
    #if 1:
        query = takeCommand().lower()
        #logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' is query:
            webbrowser.open("youtube.com")

        elif 'open google' is query:
            webbrowser.open("google.com")
        
        elif 'open stackoverflow' is query:
            webbrowser.open("stackoverflow.com")
        
        elif 'play music' in query:
            music_dir = 'D:\\songs\\hindi'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"sir, the time is {strTime}")

        elif 'open visual studio code' in query:
            codePath = "C:\\Users\\Naveen\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Visual Studio Code"
            os.startfile(codePath)

        elif 'email to harry' in query:
            try:
                speak("what should I say?")
                content = takeCommand()
                to = "gargnaveen96@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent!")
            
            except Exception as e:
                print(e)
                speak("Sorry sir. I'm not able to send this email!")

        elif 'quit' in query:
            speak("Thank you. Have a nice day!")
            print("Thank you. Have a nice day! ")
            exit()