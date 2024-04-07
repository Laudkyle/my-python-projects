import speech_recognition as sr
import pyttsx3
#starting the engine
engine = pyttsx3.init()
# Assigning the  voices variable
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate', 150)
engine.say('What is your name?')
r = sr.Recognizer()
with sr.Microphone() as source:
    print("What is your name :  ")
    audio = r.listen(source)


    try:
        name = r.recognize_google(audio)
        print(f"Hello : {name}")
    except:
        print("Could not recognize your voice, please.try again.  ")

engine.say(f'Hello {name}')
engine.runAndWait()