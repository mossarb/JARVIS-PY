import pyttsx3
import time
import os
import speech_recognition as sr
from colorama import Fore, init
init(autoreset=True)
import JarvisOne as ayj

def StartJarvis():
    engine = pyttsx3.init()
    voices = engine.getProperty("voices")
    engine.setProperty("voice", voices[0].id)
    #print(voices[1].id)

    engine.setProperty("rate", 130)

    key = [
        "jarvis",
        "Jarvis",
        "JARVIS",
        "hey jarvis",
        "Hey jarvis",
        "hey Jarvis",
        "Hey Jarvis",
        "okey jarvis",
        "Okey jarvis",
        "Okey Jarvis",
        "hello jarvis",
        "Hello jarvis",
        "Hello Jarvis"
    ]

    r = sr.Recognizer()

    def record(ask = False):
        with sr.Microphone() as source:
            if ask:
                print(ask)
            audio = r.listen(source)
            voice = ""
            try:
                voice = r.recognize_google(audio, language="en-EN")
            except sr.UnknownValueError:
                speak("I do not understand")
            except sr.RequestError:
                speak("system is not working")
            return voice

    def response(voice):
        if key in voice:
            speak("Yes Sir")
            ayj.StartResponse()
        else:
            print("----")
            
    def speak(string):
        engine.say(string)
        engine.runAndWait()

    print("----------------------------")
    print(Fore.GREEN + "- Speak -")
    print("----------------------------")

    while True:
        voice = record()
        print(voice)
        response(voice)