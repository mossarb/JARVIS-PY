import pyttsx3
import time
import os
import speech_recognition as sr
from colorama import Fore, init
init(autoreset=True)
import jarvis as j

def StartResponse():

    engine = pyttsx3.init()
    voices = engine.getProperty("voices")
    engine.setProperty("voice", voices[0].id)
    #print(voices[1].id)

    engine.setProperty("rate", 130)

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
        
    def response2(voice):
        if "hello" in voice or "Hello" in voice:
            speak("hello to you too sir")
            j.StartJarvis()
        if "how are you" in voice or "How are you" in voice:
            speak("I'm fine, how are you?")
            j.StartJarvis()
        if "turn off the lights" in voice or "Turn off the lights" in voice:
            speak("i don't have access to do that sir")
            j.StartJarvis()
        if "exit" in voice or "Exit" in voice:
            speak("Okey Sir.")
            exit()
            
    def speak(string):
        engine.say(string)
        engine.runAndWait()

    print("----------------------------")
    print(Fore.YELLOW + "- Start -")
    print("----------------------------")

    while True:
        voice = record()
        print(voice)
        response2(voice)