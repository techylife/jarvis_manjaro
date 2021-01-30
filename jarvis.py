import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
from playsound import playsound
import smtplib

engine = pyttsx3.init('espeak')
voices = engine.getProperty('voices')
print(len(voices))
print(voices[11].id)
engine.setProperty('voice',voices[11].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    
    if hour<12 & hour>=0:
        speak('Good Morning !')
    
    elif hour>=12 & hour <18:
        speak('Good Afternoon')
    
    else:
        speak('Good Evening')

    

    speak("I am a bot. Tell me how may I help you.")

def takeCommands():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening...\n')
        r.pause_threshold=1
        audio = r.listen(source)
    
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said {query}\n")
    
    except Exception as e :
        # print(e)
        print("Sorry, couldn't get it, please repeat...")
        return "Sorry, couldn't get it, please repeat..."

    return query

def sendEmail(to, content):    
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('your@email.com', 'yourPassword') '''<<<<<----------------------Please fill the 'your@email.com' by putting your email from where u want to send the mail and its
                                                                                 password in 'yourPassword'  '''
    server.sendmail('your@email.com', to, content)'''<<<<<----------------------Please fill the 'your@email.com' by putting your email from where u want to send the mail '''
    server.close()

if __name__ == "__main__":
    wishMe()

    while True:
        query = takeCommands().lower()
        speak(query)
        if "wikipedia" in query:
            query = query.replace("wikipedia", "")
            print("Searching wikipedia...")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)
        
        elif "open youtube" in query:
            webbrowser.open('youtube.com')
        
        elif "open google" in query:
            webbrowser.open('google.com')
        
        elif "open console" in query:
            webbrowser.open('https://gp.falixnodes.net/')
        
        elif "open classroom" in query:
            webbrowser.open('meet.google.com')
        
        elif "open facebook" in query:
            webbrowser.open('facebook.com')

        elif "play music" in query:
            path = #put the music directory path here <<<<_----------------------------------------------Change this...
            songs = os.listdir(path)
            song = path+songs[0]
            webbrowser.open(song)
        
        elif "the time" in query:
            strtime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time now is {strtime}")

        elif "send mail" in query:
            try:
                
                speak("Please enter the email of the person, sir.")
                to=input("Enter the email\n")
                speak("What do you want me to say in the mail?")
                content = takeCommands()
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry, I couldn't send the mail. There seems to be an error. Please check the console")
        
        elif 'exit' in query:
            exit()
