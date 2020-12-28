import pyttsx3
import datetime
import speech_recognition as sr
import pyaudio
import webbrowser
import wikipedia
import os
import smtplib


engine = pyttsx3.init('sapi5')
voices= engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak('good morning!')
    elif hour>=12 and hour<18:
        speak('good afternoon!')
    else:
        speak('good evening!')
    
    speak('Hey Nayan . how may i help you ')

def takeCommand():
    '''it takes microphone i/p from user and retures string o/p'''
    r= sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening....')
        r.pause_threshold = 1
        audio = r.listen(source)
    
    try:
        print('Recognizing...')
        query = r.recognize_google(audio, language='en-in')
        print(f'User said: {query}\n')

    except Exception as e:
        print(e)
        print('say that again please....')
        return 'None'
    return query

if __name__ == "__main__":
    wishMe()
    while True:
        query=takeCommand().lower()

        if 'wikipedia' in query:
            speak('searching on weikipedia.....')
            query= query.replace('wikipedia','')
            results= wikipedia.summary(query, sentences=2)
            speak('according to wikipedia')
            speak(results)
            print(results)

        elif 'google' in query:
            speak('opening browser...')
            webbrowser.open('www.google.com')

        elif 'youtube' in query:
            speak('opening youtube...')
            webbrowser.open('www.youtube.com')

        elif 'stackoverflow' in query:
            speak('opening browser...')
            webbrowser.open('www.stackoverflow.com')

        elif 'play music' in query:
            speak('playing music...')
            music_dir='E:\\all songs\\marathi s\\Marathi'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir,songs[1]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")
        
        elif "exit" in query:
            break
