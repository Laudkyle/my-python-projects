import datetime
import importlib
import os
import random
import re
import subprocess
import urllib
import webbrowser
from tkinter import filedialog
from threading import *

import keyboard
from time import sleep
import nltk
import psutil
import pyttsx3
import speech_recognition as sr
import win32com.client
from bs4 import BeautifulSoup

import reload_mod

scrollKey = 1
application_list = {}
application_list_location = {}
app_list = []
song_list = []
song_enquiry_list = ["name it", "what is the title of the song", "name the song", "title please!!!"]


def audio_input():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening... ")
        audio = r.listen(source, timeout = 1.0)
        r.adjust_for_ambient_noise(source, duration = 5)
        r.dynamic_energy_threshold = False
        r.energy_threshold = 1000
    return audio


class Kyla:
    welcomeList = ["How may I help you?", "What do you need?", "How can I assist you?"]

    def welcome_selector(self):
        index = random.randint(0, len(self.welcomeList) - 1)
        selected = self.welcomeList[index]
        return selected

    def __init__(self, name, voice):
        self.search = name
        self.voice = voice

    def wake(self):
        engine = pyttsx3.init()
        voices = engine.getProperty("voices")
        engine.setProperty("voice", voices[self.voice].id)
        engine.setProperty('rate', 150)
        engine.say(self.welcome_selector())
        engine.runAndWait()
        search()

    def say(self, ans):
        engine = pyttsx3.init()
        voices = engine.getProperty("voices")
        engine.setProperty("voice", voices[self.voice].id)
        engine.setProperty('rate', 150)
        engine.say(ans)
        engine.runAndWait()

    def idle(self):
        r = sr.Recognizer()
        while True:
            try:
                with sr.Microphone() as source:
                    os.system("cls")
                    print("Listening... ")
                    audio = r.listen(source, timeout = 1.0)
                    r.adjust_for_ambient_noise(source, duration = 3)
                    r.dynamic_energy_threshold = False
                    r.energy_threshold = 1000
                    print("Recognizing...")
                    speech = r.recognize_google(audio)
                    if speech == "wiki":
                        Kyla.wake(self)
                        break
                    else:
                        pass
            except TypeError:
                pass
            except sr.WaitTimeoutError:
                continue
            except sr.UnknownValueError:
                pass
            except sr.RequestError:
                os.system("cls")
            except Exception as e:
                pass



class apps:
    def __init__(self, app_name, pid):
        self.app_name = app_name
        self.pid = pid


# Psutil functions
# Creating the battery function
def convertTime(seconds):
    minutes, seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    return "%d hours,%02d minutes and %02d seconds " % (hours, minutes, seconds)


battery = psutil.sensors_battery()
percentage = battery.percent
time = convertTime(battery.secsleft)


# Creating the search function

def listening():
    occur = True
    while occur:
        try:
            r = sr.Recognizer()
            with sr.Microphone() as source:
                print("Listening... ")
                audio = r.listen(source, timeout = 2.0)
                sr.Recognizer().adjust_for_ambient_noise(source)
                sr.Recognizer().dynamic_energy_threshold = False
                sr.Recognizer().energy_threshold = 1000
                print("Recognizing...")
                speech = r.recognize_google(audio)
                print(speech)
                occur = False
        except TypeError:
            pass
            continue
        except sr.WaitTimeoutError:
            pass
        except sr.UnknownValueError:
            pass
        except sr.RequestError:
            KYLA.say("I think there is a problem, please check your Internet connection!")
            continue
        except Exception:
            continue

    return speech


def typing():
    typeMode = 1
    while typeMode == 1:
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening... ")
            audio = r.listen(source)
            sr.Recognizer().adjust_for_ambient_noise(source, duration = 3)
            sr.Recognizer().dynamic_energy_threshold = False
            sr.Recognizer().energy_threshold = 1000
        try:
            print("Recognizing...")
            speech = r.recognize_google(audio)
            if speech.lower() == "next line" or speech.lower() == "start a new line" or speech.lower() == "move to a " \
                                                                                                          "new line" \
                    or speech.lower() == "go to a new line":
                keyboard.press_and_release("enter")
                continue
            elif speech.lower() == "enter" or speech.lower() == "send":
                keyboard.press_and_release("enter")
                continue
            elif speech.lower() == "space" or speech.lower() == "spacebar":
                keyboard.press_and_release("spacebar")
                continue
            elif speech.lower() == "tab":
                keyboard.press_and_release("tab")
                continue
            elif speech.lower() == "full stop":
                keyboard.write(". ")
                continue
            elif speech.lower() == "karma":
                keyboard.write(", ")
                continue
            elif speech.lower() == "open brackets" or speech.lower() == "open bracket":
                keyboard.press_and_release("shift+(")
                continue
            elif speech.lower() == "close brackets" or speech.lower() == "close bracket":
                keyboard.press_and_release("shift+)")
                continue
            elif speech.lower() == "open square brackets":
                keyboard.press_and_release("[")
                continue
            elif speech.lower() == "close square brackets":
                keyboard.press_and_release("]")
                continue
            elif speech.lower() == "question mark":
                keyboard.press_and_release("shift+?")
                continue
            elif speech.lower() == "undo that":
                keyboard.press_and_release("ctrl+z")
                continue
            elif speech.lower() == "exclamation mark":
                keyboard.press_and_release("shift+!")
                continue
            elif speech.lower() == "double exclamation mark":
                keyboard.press_and_release("shift+!")
                keyboard.press_and_release("shift+!")
                continue
            elif speech.lower() == "triple exclamation mark":
                keyboard.press_and_release("shift+!")
                keyboard.press_and_release("shift+!")
                keyboard.press_and_release("shift+!")
                continue
            elif speech.lower() == "open curly braces":
                keyboard.press_and_release("shift+{")
                continue
            elif speech.lower() == "close curly braces":
                keyboard.press_and_release("shift+}")
                continue
            elif speech.lower() == "colon":
                keyboard.press_and_release("shift+:")
                continue
            elif speech.lower() == "semicolon":
                keyboard.press_and_release(";")
                continue
            elif speech.lower() == "backspace":
                keyboard.press_and_release("Backspace")
                continue
            elif speech.lower() == "select all":
                keyboard.press_and_release("ctrl+a")
                continue
            elif speech.lower() == "save this document" or speech.lower() == "save this" or speech.lower() == "save":
                keyboard.press_and_release("ctrl+s")
                continue
            elif speech.lower() == "close tab" or speech.lower() == "close this tab" or speech.lower() == "exit tab":
                keyboard.press_and_release("ctrl+w")
                continue
            elif speech.lower() == "open tab" or speech.lower() == "new tab" or speech.lower() == "open a new tab":
                keyboard.press_and_release("ctrl+t")
                continue
            elif speech.lower() == "switch tab" or speech.lower() == "next tab":
                keyboard.press_and_release("ctrl+tab")
                continue
            elif speech.lower() == "previous tab" or speech.lower() == "reverse tab":
                keyboard.press_and_release("ctrl+shift+tab")
                continue
            elif speech.lower() == "minimise" or speech.lower() == "minimise page" or speech.lower() == "minimise this" or speech.lower() == "minimise this page" or speech.lower() == "minimise this window" or speech.lower() == "minimise window":
                keyboard.press_and_release("windows+down")
                keyboard.press_and_release("windows+down")
                continue
            elif speech.lower() == "move this window to the right" or speech.lower() == "shift window to the right":
                keyboard.press_and_release("windows+right")
                continue
            elif speech.lower() == "move this window to the left" or speech.lower() == "shift window to the left":
                keyboard.press_and_release("windows+left")
                continue
            elif speech.lower() == "maximize this" or speech.lower() == "maximize this window" or speech.lower() == "maximize":
                keyboard.press_and_release("windows+up")
                continue
            elif speech.lower() == "delete all":
                keyboard.press_and_release("ctrl+a")
                keyboard.press_and_release("Backspace")
                continue
            elif speech.lower() == "delete that":
                keyboard.press_and_release("ctrl+shift+left")
                keyboard.press_and_release("Backspace")
                continue
            elif speech.lower() == "stop typing" or speech.lower() == "deactivate typing mode" or speech.lower() == "deactivate typing":
                KYLA.say("Okay")
                break
        except TypeError:
            pass
            continue
        except sr.WaitTimeoutError:
            KYLA.idle()
        except sr.UnknownValueError:
            KYLA.say("Sorry, I didn't get that!")
            pass
            continue
        except sr.RequestError:
            KYLA.say("I think there is a problem, please check your Internet connection!")
            continue
        except Exception:
            continue

        keyboard.write(speech)

    KYLA.wake()
    return 0


def search():
    while True:
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening... ")
            audio = r.listen(source)
            sr.Recognizer().adjust_for_ambient_noise(source, duration = 3)
            sr.Recognizer().dynamic_energy_threshold = False
            sr.Recognizer().energy_threshold = 1000
        try:
            print("Recognizing...")
            question = r.recognize_google(audio)
            print(question)
        except TypeError:
            pass
            continue
        except sr.WaitTimeoutError:
            KYLA.idle()
        except sr.UnknownValueError:
            KYLA.say("Sorry, I didn't get that!")
            pass
            continue
        except sr.RequestError:
            KYLA.say("I think there is a problem, please check your Internet connection!")
            continue
        except Exception:
            continue

        # Defining the words for closing the KYLA

        if question.lower() == "close":
            KYLA.say("okay!!!")
            exit()
        elif question.lower() == "shut up":
            KYLA.say("okay!!!")
            exit()
        elif question.lower() == "keep quiet":
            KYLA.say("okay!!!")
            exit()
        elif question.lower() == "fuck off":
            KYLA.say("okay!!!")
            exit()
        elif question.lower() == "exit":
            KYLA.say("okay!!!")
            exit()
        elif question.lower() == "quit":
            KYLA.say("okay!!!")
            exit()
        elif question.lower() == "bye":
            KYLA.say("okay!!!")
            exit()
        elif question.lower() == "bye bye":
            KYLA.say("okay!!!")
            exit()
        elif question.lower() == "alright thanks":
            KYLA.say("okay!!!")
            exit()
        elif question.lower() == "thanks pal":
            KYLA.say("okay!!!")
            exit()
        elif question.lower() == "get out of here":
            KYLA.say("okay!!!")
            exit()

        # Defining the words for sleeping or waiting

        elif question.lower() == "sleep":
            KYLA.idle()
        elif question.lower() == "hold on":
            KYLA.idle()

        # Self introduction

        elif "what is your name" in question.lower():
            KYLA.say("I am Kyla")
        elif "How are you" in question.lower():
            KYLA.say("I'm doing great and you?")
        elif "who are you" in question.lower():
            KYLA.say("I am Kyla")
        elif "introduce yourself" in question.lower():
            KYLA.say("Hello, I am Kyla, Your virtual assistant")
        elif "how old are you" in question.lower():
            KYLA.say("I am a day old chicken")

        # Questions about date and time

        elif "what is the time" in question or "time" in question:
            KYLA.say(datetime.datetime.now().strftime("%I:%M:%S"))
        elif "what is today's date" in question or "date" in question:
            day = int(datetime.datetime.now().day)
            month = int(datetime.datetime.now().month)
            year = int(datetime.datetime.now().year)
            date = (day, month, year)
            KYLA.say(date)


        # Keyboard Shortcut
        elif question.lower() == "select all":
            keyboard.press_and_release("ctrl+a")
            continue
        elif question.lower() == "delete all":
            keyboard.press_and_release("ctrl+a")
            keyboard.press_and_release("Backspace")
            continue
        elif question.lower() == "undo":
            keyboard.press_and_release("ctrl+z")
            continue
        elif question.lower() == "page up" or question.lower() == "scroll up" or question.lower() == "move up":
            keyboard.press_and_release("page up")
            scroll(scrollUp)
            continue
        elif question.lower() == "page down" or question.lower() == "scroll down" or question.lower() == "move down":
            keyboard.press_and_release("page down")
            scroll(scrollDown)
            continue
        elif question.lower() == "okay" or question.lower() == "enter" or question.lower() == "agree" or question.lower() == "i agree" or question.lower() == "ok" or question.lower() == "yes" or question.lower() == "open that" or question.lower() == "open this" or question.lower() == "open" or question.lower() == "yeah" or question.lower() == "sure":
            keyboard.press_and_release("enter")
            continue
        elif question.lower() == "start menu" or question.lower() == "open the start menu" or question.lower() == "open start menu":
            keyboard.press_and_release("windows")
            continue
        elif question.lower() == "close this" or question.lower() == "close that" or question.lower() == "close this window" or question.lower() == "close that window" or question.lower() == "close the current application" or question.lower() == "close application" or question.lower() == "close this application" or question.lower() == "close this app" or question.lower() == "close this up":
            keyboard.press_and_release("Alt+f4")
            continue
        elif question.lower() == "close tab" or question.lower() == "close this tab" or question.lower() == "exit tab":
            keyboard.press_and_release("ctrl+w")
            continue
        elif question.lower() == "open tab" or question.lower() == "new tab" or question.lower() == "open a new tab":
            keyboard.press_and_release("ctrl+t")
            continue
        elif question.lower() == "switch tab" or question.lower() == "next tab":
            keyboard.press_and_release("ctrl+tab")
            continue
        elif question.lower() == "previous tab" or question.lower() == "reverse tab":
            keyboard.press_and_release("ctrl+shift+tab")
            continue
        elif question.lower() == "minimise" or question.lower() == "minimise page" or question.lower() == "minimise this" or question.lower() == "minimise this page" or question.lower() == "minimise this window" or question.lower() == "minimise window":
            keyboard.press_and_release("windows+down")
            keyboard.press_and_release("windows+down")
            continue
        elif question.lower() == "move this window to the right" or question.lower() == "shift window to the right":
            keyboard.press_and_release("windows+right")
            continue
        elif question.lower() == "move this window to the left" or question.lower() == "shift window to the left":
            keyboard.press_and_release("windows+left")
            continue
        elif question.lower() == "maximize this" or question.lower() == "maximize this window" or question.lower() == "maximize":
            keyboard.press_and_release("windows+up")

        elif question.lower() == "move up" or question.lower() == "up":
            keyboard.press_and_release("UP")
            continue
        elif question.lower() == "move down" or question.lower() == "down":
            keyboard.press_and_release("DOWN")
            continue
        elif question.lower() == "move left" or question.lower() == "left":
            keyboard.press_and_release("LEFT")
            continue
        elif question.lower() == "move right" or question.lower() == "right":
            keyboard.press_and_release("RIGHT")
            continue
        # Sending speech for analysis
        else:
            speech_analyzer(question)

    return 0


# Web search category


def web_search(text):
    try:
        splitted_text = text.split(" ")
        if len(splitted_text) == 1:
            txt = ""
            text_splitted = ""
            web = urllib.request.urlopen(f"https://en.wikipedia.org/wiki/{text}").read()
            soup = BeautifulSoup(web, 'lxml')
            for paragraph in soup.find_all("p"):
                txt += paragraph.text
            # Processing the data
            txt = re.sub(r'\[[0-9]*]', ' ', txt)
            txt = re.sub(r'\s+', ' ', txt)
            txt = re.sub(r'\d ', ' ', txt)
            sentences = nltk.sent_tokenize(txt)
            for line in range(3):
                text_splitted += sentences[line]
            text_splitted = text_splitted.replace(".", ". ")
            KYLA.say(f"According to wikipedia, {text_splitted}")

    except IndexError:
        general_search(text)
    return 0

def speech_listening():
    global scrollKey
    speech = listening()
    if speech == "pause" or speech == "wait" or speech == "stop":
        scrollKey = 0
        sleep(5)
        scrollKey = 1
    elif speech == "scroll up" or speech == "move up":
        scrollUp()
    elif speech == "scroll down" or speech == "move down":
        scrollDown()
    else:
        speech_listening()
    return speech


# defining the scroll function
def scroll(function):
    thread_1 = Thread(target = function)
    thread_2 = Thread(target = speech_listening)

    thread_1.start()
    thread_2.start()
    thread_1.join()
    thread_2.join()
    return 0


def scrollDown():
    global scrollKey
    while scrollKey == 1:
        keyboard.press_and_release("down")
        keyboard.press_and_release("down")
        sleep(1)
    return 0


def scrollUp():
    global scrollKey
    while scrollKey == 1:
        keyboard.press_and_release("up")
        keyboard.press_and_release("up")
        sleep(1)
    return 0


# Defining the speech analyzer function
def speech_analyzer(text):
    if "open calculator" in text.lower():
        KYLA.say("okay!!!")
        subprocess.Popen("calc.exe")
    elif "close calculator" in text.lower() or "quit calculator" in text.lower() or "exit calculator" in text.lower():
        subprocess.call(["taskkill", "/IM", "calc.exe"])
        KYLA.say("Done!!!")
    elif "open command prompt" in text.lower():
        KYLA.say("okay!!!")
        subprocess.Popen("cmd.exe")
    elif "close command prompt" in text.lower():
        subprocess.call(["taskkill", "/IM", "cmd.exe"])
        KYLA.say("Done!!!")
    elif "open vlc media player" in text.lower() or "open vlc" in text.lower():
        KYLA.say("okay!!!")
        subprocess.Popen("C:\\Program Files (x86)\\VideoLAN\\VLC\\vlc.exe")
    elif "close vlc" in text.lower():
        subprocess.call(["taskkill", "/IM", "vlc.exe"])
        KYLA.say("Done!!!")
    elif "open internet explorer" in text.lower():
        KYLA.say("okay!!!")
        subprocess.Popen("C:\\Program Files (x86)\\Internet Explorer\\iexplore.exe")
    elif "close internet explorer" in text.lower():
        subprocess.call(["taskkill", "/IM", "iexplore.exe"])
        KYLA.say("Done!!!")
    elif "open windows media player" in text.lower():
        KYLA.say("okay!!!")
        subprocess.Popen("C:\\Program Files (x86)\\Windows Media Player\\wmplayer.exe")
    elif "close windows media player" in text.lower():
        subprocess.call(["taskkill", "/IM", "wmplayer.exe"])
        KYLA.say("Done!!!")
    elif "open mozilla" in text.lower() or "open firefox" in text.lower():
        KYLA.say("okay!!!")
        subprocess.Popen("C:\\Program Files\\Mozilla Firefox\\firefox.exe")
    elif "close firefox" in text.lower() or "close mozilla" in text.lower():
        subprocess.call(["taskkill", "/IM", "firefox.exe"])
        KYLA.say("Done!!!")
    elif "close chrome" in text.lower():
        subprocess.call(["taskkill", "/IM", "chrome.exe"])
        KYLA.say("Done!!!")
    elif "what is my battery percentage" in text.lower():
        KYLA.say(f"{percentage} percent")
    elif "battery percentage" in text.lower():
        KYLA.say(f"{percentage} percent")
    elif "check my battery for me" in text.lower() or "how much time is left on my battery" in text.lower() or "how much time do i left on my battery" in text.lower() or "battery time" in text.lower() or "how long before the laptop goes down" in text.lower() or "how much battery time do i have" in text.lower() or "how much time do i have on the battery" in text.lower() or "how long will it take for the battery goes down" in text.lower() or "how long will it take before the battery goes down" in text.lower() or "how long before the battery goes down" in text.lower() or "when will the pc go on low battery" in text.lower():
        KYLA.say("okay")
        KYLA.say(f"you have {time} left")
    elif "check if my battery is charging" in text.lower() or "is my battery charging" in text.lower() or "check if " \
                                                                                                          "my laptop " \
                                                                                                          "is charging" in text.lower() or "is my computer charging" in text.lower() or "is my battery charging" in text.lower() or "check if the laptop is charging" in text.lower() or "check if the machine is charging" in text.lower() or "is my machine charging" in text.lower() or "is the machine charging" in text.lower() or "is my laptop charging" in text.lower() or "is the laptop charging" in text.lower():

        KYLA.say(importlib.reload(reload_mod).battery_status())
    elif "play me a song" in text.lower() or "play a song for me" in text.lower() or "let it roll" in text.lower():
        KYLA.say("hold on a second")
        play()


    # CPU usage

    elif "cpu percentage" in text.lower():
        KYLA.say(f"you are currently using {importlib.reload(reload_mod).cpu_percentage()} percent of your cpu")
    elif "percentage cpu" in text.lower():
        KYLA.say(f"you are currently using {importlib.reload(reload_mod).cpu_percentage()} percent of your cpu")
    elif "what is my cpu usage" in text.lower():
        KYLA.say(f"you are currently using {importlib.reload(reload_mod).cpu_percentage()} percent of your cpu")
    elif "what is my cpu percentage" in text.lower():
        KYLA.say(f"you are currently using {importlib.reload(reload_mod).cpu_percentage()} percent of your cpu")
    elif "what is my cpu usage percentage" in text.lower():
        KYLA.say(f"you are currently using {importlib.reload(reload_mod).cpu_percentage()} percent of your cpu")
    elif "how much cpu am i using" in text.lower():
        KYLA.say(f"you are currently using {importlib.reload(reload_mod).cpu_percentage()} percent of your cpu")
    elif "how much cpu am i using currently" in text.lower():
        KYLA.say(f"you are currently using {importlib.reload(reload_mod).cpu_percentage()} percent of your cpu")
    elif "how much of my cpu am i using" in text.lower():
        KYLA.say(f"you are currently using {importlib.reload(reload_mod).cpu_percentage()} percent of your cpu")
    elif "how much of my cpu is in use" in text.lower():
        KYLA.say(f"you are currently using {importlib.reload(reload_mod).cpu_percentage()} percent of your cpu")
    elif "how much of my cpu is in use currently" in text.lower():
        KYLA.say(f"you are currently using {importlib.reload(reload_mod).cpu_percentage()} percent of your cpu")
    elif "how much of my cpu is in use right now" in text.lower():
        KYLA.say(f"you are currently using {importlib.reload(reload_mod).cpu_percentage()} percent of your cpu")
    elif "how much cpu am i using right now" in text.lower():
        KYLA.say(f"you are currently using {importlib.reload(reload_mod).cpu_percentage()} percent of your cpu")
    elif "how much of my cpu am i using right now" in text.lower():
        KYLA.say(f"you are currently using {importlib.reload(reload_mod).cpu_percentage()} percent of your cpu")
    elif "what is the percentage of cpu i am using right now" in text.lower():
        KYLA.say(f"you are currently using {importlib.reload(reload_mod).cpu_percentage()} percent of your cpu")

    # Ram usage

    elif "ram percentage" in text.lower():
        KYLA.say(f"you are currently using {importlib.reload(reload_mod).ram_percentage()} percent of your ram")
    elif "percentage ram" in text.lower():
        KYLA.say(f"you are currently using {importlib.reload(reload_mod).ram_percentage()} percent of your ram")
    elif "what is my ram percentage" in text.lower():
        KYLA.say(f"you are currently using {importlib.reload(reload_mod).ram_percentage()} percent of your ram")
    elif "what is my ram usage percentage" in text.lower():
        KYLA.say(f"you are currently using {importlib.reload(reload_mod).ram_percentage()} percent of your ram")
    elif "how much ram am i using" in text.lower():
        KYLA.say(f"you are currently using {importlib.reload(reload_mod).ram_percentage()} percent of your ram")
    elif "how much ram am i using currently" in text.lower():
        KYLA.say(f"you are currently using {importlib.reload(reload_mod).ram_percentage()} percent of your ram")
    elif "how much of my ram am i using" in text.lower():
        KYLA.say(f"you are currently using {importlib.reload(reload_mod).ram_percentage()} percent of your ram")
    elif "how much of my ram is in use" in text.lower():
        KYLA.say(f"you are currently using {importlib.reload(reload_mod).ram_percentage()} percent of your ram")
    elif "how much of my ram is in use currently" in text.lower():
        KYLA.say(f"you are currently using {importlib.reload(reload_mod).ram_percentage()} percent of your ram")
    elif "how much of my ram is in use right now" in text.lower():
        KYLA.say(f"you are currently using {importlib.reload(reload_mod).ram_percentage()} percent of your ram")
    elif "how much ram am i using right now" in text.lower():
        KYLA.say(f"you are currently using {importlib.reload(reload_mod).ram_percentage()} percent of your ram")
    elif "how much of my ram am i using right now" in text.lower():
        KYLA.say(f"you are currently using {importlib.reload(reload_mod).ram_percentage()} percent of your ram")
    elif "what is the percentage of ram i am using right now" in text.lower():
        KYLA.say(f"you are currently using {importlib.reload(reload_mod).ram_percentage()} percent of your ram")


    # Force close applications

    elif "force close command prompt" in text.lower():
        for process in (process for process in psutil.process_iter() if process.name() == "cmd.exe"):
            process.kill()
        KYLA.say("Done!!!")
    elif "open vlc media player" in text.lower() or "open vlc" in text.lower():
        KYLA.say("okay!!!")
        subprocess.Popen("C:\\Program Files (x86)\\VideoLAN\\VLC\\vlc.exe")
    elif "force close vlc" in text.lower():
        for process in (process for process in psutil.process_iter() if process.name() == "vlc.exe"):
            process.kill()
        KYLA.say("Done!!!")
    elif "open internet explorer" in text.lower():
        KYLA.say("okay!!!")
        subprocess.Popen("C:\\Program Files (x86)\\Internet Explorer\\iexplore.exe")
    elif "force close internet explorer" in text.lower():
        for process in (process for process in psutil.process_iter() if process.name() == "iexplore.exe"):
            process.kill()
        KYLA.say("Done!!!")
    elif "open windows media player" in text.lower():
        KYLA.say("okay!!!")
        subprocess.Popen("C:\\Program Files (x86)\\Windows Media Player\\wmplayer.exe")
    elif "force close windows media player" in text.lower():
        for process in (process for process in psutil.process_iter() if process.name() == "wmplayer.exe"):
            process.kill()
        KYLA.say("Done!!!")
    elif "open mozilla" in text.lower() or "open firefox" in text.lower():
        KYLA.say("okay!!!")
        subprocess.Popen("C:\\Program Files\\Mozilla Firefox\\firefox.exe")
    elif "force close firefox" in text.lower() or "close mozilla" in text.lower():
        for process in (process for process in psutil.process_iter() if process.name() == "firefox.exe"):
            process.kill()
        KYLA.say("Done!!!")
    elif "force close chrome" in text.lower():
        for process in (process for process in psutil.process_iter() if process.name() == "chrome.exe"):
            process.kill()
        KYLA.say("Done!!!")
    if text.lower() == "activate typing mode" or text.lower() == "activate typing" or text.lower() == "type this":
        KYLA.say("okay, I'm listening!!!")
        typing()



    # Opening of common websites

    elif "open youtube" in text.lower():
        webbrowser.open(f"https://youtube.com")
    elif "open gmail" in text.lower():
        KYLA.say("okay!!! I will do that")
        webbrowser.open(f"https://gmail.com")
    elif "open google" in text.lower():
        KYLA.say("okay!!! I will do that")
        webbrowser.open(f"https://google.com")
    elif "open facebook" in text.lower():
        KYLA.say("okay!!! I will do that")
        webbrowser.open(f"https://facebook.com")
    elif "open twitter" in text.lower():
        KYLA.say("okay!!! I will do that")
        webbrowser.open(f"https://twitter.com")
    elif "open wikipedia" in text.lower():
        KYLA.say("okay!!! I will do that")
        webbrowser.open(f"https://wikipedia.org")
    elif "open baidu" in text.lower():
        KYLA.say("okay!!! I will do that")
        webbrowser.open(f"https://baidu.com")
    elif "open yahoo" in text.lower():
        KYLA.say("okay!!! I will do that")
        webbrowser.open(f"https://yahoo.com")
    elif "open instagram" in text.lower():
        KYLA.say("okay!!! I will do that")
        webbrowser.open(f"https://instagram.com")
    elif "open netflix" in text.lower():
        KYLA.say("okay!!! I will do that")
        webbrowser.open(f"https://netflix.com")
    elif "open whatsapp" in text.lower():
        KYLA.say("okay!!! I will do that")
        webbrowser.open(f"https://whatsapp.com")
    elif "open amazon" in text.lower():
        KYLA.say("okay!!! I will do that")
        webbrowser.open(f"https://amazon.com")
    elif "open live" in text.lower():
        KYLA.say("okay!!! I will do that")
        webbrowser.open(f"https://live.com")
    elif "open zoom" in text.lower():
        KYLA.say("okay!!! I will do that")
        webbrowser.open(f"https://zoom.us")
    elif "open reddit" in text.lower():
        KYLA.say("okay!!! I will do that")
        webbrowser.open(f"https://reddit.com")
    elif "open pinterest" in text.lower():
        KYLA.say("okay!!! I will do that")
        webbrowser.open(f"https://pinterest.com")
    elif "open linkedin" in text.lower():
        KYLA.say("okay!!! I will do that")
        webbrowser.open(f"https://linkedin.com")
    elif "open office" in text.lower():
        KYLA.say("okay!!! I will do that")
        webbrowser.open(f"https://office.com")
    elif "open microsoft.com" in text.lower():
        KYLA.say("okay!!! I will do that")
        webbrowser.open(f"https://microsoft.com")
    elif "open wiki" in text.lower():
        KYLA.say("okay!!! I will do that")
        webbrowser.open(f"https://wiki.com")


    # Common computer commands

    elif "open file explorer" in text.lower():
        KYLA.say("okay!!!")
        subprocess.Popen('explorer ""')
    elif "close file explorer" in text.lower():
        for process in (process for process in psutil.process_iter() if process.name() == "explorer.exe"):
            process.kill()
        KYLA.say("Done!!!")
    elif "open this pc" in text.lower():
        KYLA.say("okay!!!")
        subprocess.Popen('explorer ""')
    elif "close this pc" in text.lower():
        for process in (process for process in psutil.process_iter() if process.name() == "explorer.exe"):
            process.kill()
        KYLA.say("Done!!!")
    elif "open my documents" in text.lower():
        KYLA.say("okay!!!")
        subprocess.Popen('explorer "C:\temp"')
    elif "close my documents" in text.lower():
        for process in (process for process in psutil.process_iter() if process.name() == "explorer.exe"):
            process.kill()
        KYLA.say("Done!!!")
    elif "open my computer" in text.lower():
        KYLA.say("okay!!!")
        subprocess.Popen('explorer "C:\temp"')
    elif "close my computer" in text.lower():
        for process in (process for process in psutil.process_iter() if process.name() == "explorer.exe"):
            process.kill()
        KYLA.say("Done!!!")
    elif "open task manager" in text.lower():
        KYLA.say("okay!!!")
        subprocess.Popen("Taskmgr.exe")
    elif "close task manager" in text.lower():
        for process in (process for process in psutil.process_iter() if process.name().lower() == "taskmgr.exe"):
            process.kill()
        KYLA.say("Done!!!")
    elif "open system settings" in text.lower():
        KYLA.say("okay!!!")
        subprocess.Popen("C:\\Windows\\ImmersiveControlPanel\\SystemSettings.exe")
    elif "close system settings" in text.lower():
        for process in (process for process in psutil.process_iter() if process.name().lower() == "systemsettings.exe"):
            process.kill()
        KYLA.say("Done!!!")
    elif "what is the meaning of the word" in text:
        processed_text = text.replace("what is the meaning of the word ", "")
        web_search(processed_text)
    elif "what is the meaning of this word" in text:
        processed_text = text.replace("what is the meaning of this word ", "")
        web_search(processed_text)
    elif "what is the meaning of" in text:
        processed_text = text.replace("what is the meaning of ", "")
        web_search(processed_text)
    elif "what does this word mean" in text:
        processed_text = text.replace("what does this word mean ", "")
        web_search(processed_text)
    elif "what is" in text:
        processed_text = text.replace("what is ", "")
        what_search(processed_text)
    elif "what are " in text:
        processed_text = text.replace("what are ", "")
        where_search(processed_text)
    elif "where is " in text:
        processed_text = text.replace("where is ", "")
        where_search(processed_text)
    elif "what is the location of " in text:
        processed_text = text.replace("what is the location of ", "")
        where_search(processed_text)
    elif "can you find the location of " in text:
        processed_text = text.replace("can you find the location of", "")
        where_search(processed_text)
    elif "can you find" in text:
        processed_text = text.replace("can you find", "")
        where_search(processed_text)
    elif "can you please find the location of " in text:
        processed_text = text.replace("can you please find the location of", "")
        where_search(processed_text)
    elif "search for this" in text:
        processed_text = text.replace("search for this", "")
        general_search(processed_text)

    else:
        # Adding the WH questions

        splitted_text = text.split(" ")
        if splitted_text[0].lower() == "open":
            search_computer(text)
        elif splitted_text[0].lower() == "close":
            close_app(text)
        elif splitted_text[0].lower() == "how":
            how_search(text)
        elif splitted_text[0].lower() == "who":
            who_search(text)
        elif splitted_text[0].lower() == "which":
            which_search(text)
        # Analysing the search keyword

        elif splitted_text[0].lower() == "search" and splitted_text[1].lower() == "for" and splitted_text[
            2].lower() == "this":
            processed_text = text.replace("search for this", "")
            general_search(processed_text)
        elif splitted_text[0].lower() == "search" and splitted_text[1].lower() == "for":
            processed_text = text.replace("search for", "")
            general_search(processed_text)
        elif splitted_text[0].lower() == "search":
            processed_text = text.replace("search", "")
            general_search(processed_text)

        # Power controls of the computer

        elif text == "shut down the computer" or text == "turn off the computer" or text == "switch off the computer" or text == "off the computer" or text == "turn off the computer":
            os.system("shutdown /s /t 1")
        elif text == "restart the computer" or text == "reboot the computer" or text == "hot boot the computer":
            os.system("shutdown /r /t 1")
        elif text == "sleep the computer":
            os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")
        else:
            web_search(text)
    return 0


def what_search(text):
    webbrowser.open(f"https://google.com/search?q={text}")
    return 0


def who_search(text):
    webbrowser.open(f"https://google.com/search?q={text}")
    return 0


def which_search(text):
    webbrowser.open(f"https://google.com/search?q={text}")
    return 0


def how_search(text):
    webbrowser.open(f"https://google.com/search?q={text}")
    return 0


def general_search(text):
    webbrowser.open(f"https://google.com/search?q={text}")
    return 0


def where_search(text):
    webbrowser.open(f"https://google.nl/maps/place/{text}/&amp;")
    return 0


def song_enquiry_selector():
    index = random.randint(0, len(song_enquiry_list) - 1)
    selected = song_enquiry_list[index]
    return selected


def song_selector():
    index = random.randint(0, len(song_list) - 1)
    selected = song_list[index]
    return selected


def play():
    global pids, song_list
    excl_dirs = {'Default', 'AppData', 'MicrosoftEdgeBackups', 'Public', 'Program Files(x86)', 'Program Files',
                 'Windows', 'PrefLogs', 'ProgramData'}
    dir = "E:\\my music\\"
    for root, dirnames, files in os.walk(dir):
        dirnames[:] = [d for d in dirnames if d not in excl_dirs]
        for music in files:
            if music.endswith(".mp3") or music.endswith(".m4a"):
                whole_file = root + "/" + music
                song_list.append(whole_file)
        if len(song_list) > 0:
            print(song_list)
            process = subprocess.Popen(["C:\\Program Files (x86)\\VideoLAN\\VLC\\vlc.exe",
                                        song_selector()])
            pid = process.pid
            app_name = psutil.Process(pid).name()
            appl = apps(app_name, pid)
            app_list.append(appl)
            print(app_name)
            application_list[app_name] = app_name
            print(application_list)
        elif len(song_list) <= 0:
            dir = "E:\\"
            for root, dirnames, files in os.walk(dir):
                dirnames[:] = [d for d in dirnames if d not in excl_dirs]
                for music in files:
                    if music.endswith(".mp3") or music.endswith(".m4a"):
                        whole_file = root + "/" + music
                        song_list.append(whole_file)
                if len(song_list) > 0:
                    print(song_list)
                    process = subprocess.Popen(["C:\\Program Files (x86)\\VideoLAN\\VLC\\vlc.exe",
                                                song_selector()])
                    pid = process.pid
                    app_name = psutil.Process(pid).name()
                    appl = apps(app_name, pid)
                    app_list.append(appl)
                    print(app_name)
                    application_list[app_name] = app_name
                    print(application_list)
                else:
                    KYLA.say("no file found")
    return 0


# defining the computer searching function
def search_computer(app):
    app = app.replace("open ", "")
    app = app.lower()
    global pids
    with open("application_list.txt", 'r') as file:
        if file != '':
            for line in file:
                dicline = line.split(',')
                application = dicline[0]
                app_location = dicline[1].replace(' \n', '')
                application_list_location[application] = app_location
        for application in application_list_location:
            if app in application:
                new_app_location = application_list_location[application]
                print(f"Opening {app}")
                process = subprocess.Popen(new_app_location)
                pid = process.pid
                app_name = psutil.Process(pid).name()
                appl = apps(app_name, pid)
                app_list.append(appl)
                application_list[app] = app_name
                application_list_location[app] = new_app_location
                break
        else:
            search_computer_deep(app)
    return 0


def search_computer_deep(app):
    global pids
    dir = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\"
    content = []
    for root, sub, files in os.walk(dir):
        for file in files:
            if app in file.lower():
                shell = win32com.client.Dispatch("WScript.Shell")
                shortcut = shell.CreateShortCut(root + "/" + file)
                file_full = shortcut.Targetpath
                if file_full.endswith(".EXE") or file_full.endswith(".exe"):
                    content.append(file_full)
                for file_uni in content:
                    if "unins" in file_uni:
                        content.remove(file_uni)
    if len(content) > 0:
        print(content)
        process = subprocess.Popen(content[0])
        pid = process.pid
        app_name = psutil.Process(pid).name()
        appl = apps(app_name, pid)
        app_list.append(appl)
        print(app_name)
        application_list[app] = app_name
        print(application_list)
        application_list_location[app] = content[0]
        with open("application_list.txt", "a") as f:
            for app in application_list:
                content = f"{app},{application_list_location[app]} \n"
                f.write(content)
    elif len(content) <= 0:
        dir = "C:\\Users\\Public\\Public Desktop\\"
        for root, dirnames, files in os.walk(dir):
            for file in files:
                if app in file.lower():
                    shell = win32com.client.Dispatch("WScript.Shell")
                    shortcut = shell.CreateShortCut(root + "/" + file)
                    file_full = shortcut.Targetpath
                    if file_full.endswith(".exe") or file_full.endswith(".exe"):
                        content.append(file_full)
                    for file_uni in content:
                        if "unins" in file_uni:
                            content.remove(file_uni)
                elif app in file.lower() and file.endswith(".lnk"):
                    shell = win32com.client.Dispatch("WScript.Shell")
                    shortcut = shell.CreateShortCut(root + "/" + file)
                    file_full = shortcut.Targetpath
                    content.append(file_full)
        if len(content) > 0:
            process = subprocess.Popen(content[0])
            pid = process.pid
            app_name = psutil.Process(pid).name()
            appl = apps(app_name, pid)
            app_list.append(appl)
            print(app_name)
            application_list[app] = app_name
            print(application_list)
            application_list_location[app] = content[0]
            with open("application_list.txt", "a") as f:
                for app in application_list:
                    content = f"{app},{application_list_location[app]} \n"
                    f.write(content)
    elif len(content) <= 0:
        excl_dirs = {'Default', 'MicrosoftEdgeBackups', "Public"}
        dir = "C:\\Users\\LENOVO\\AppData\\"
        for root, dirnames, files in os.walk(dir):
            dirnames[:] = [d for d in dirnames if d not in excl_dirs]
            for file in files:
                if app in file.lower() and file_full.endswith(".exe"):
                    whole_file = root + "/" + file
                    content.append(whole_file)
                    for file in content:
                        if "unins" in file.lower():
                            content.remove(file)
                elif app in file.lower() and file.endswith(".lnk"):
                    shell = win32com.client.Dispatch("WScript.Shell")
                    shortcut = shell.CreateShortCut(root + "/" + file)
                    file_full = shortcut.Targetpath
                    content.append(file_full)
        if len(content) > 0:
            process = subprocess.Popen(content[0])
            pid = process.pid
            app_name = psutil.Process(pid).name()
            appl = apps(app_name, pid)
            app_list.append(appl)
            print(app_name)
            application_list[app] = app_name
            print(application_list)
            application_list_location[app] = content[0]
            with open("application_list.txt", "a") as f:
                for app in application_list:
                    content = f"{app},{application_list_location[app]} \n"
                    f.write(content)
    if len(content) == 0:
        KYLA.say("file not found")
        KYLA.say("please help me to find it")
        file_location = filedialog.askopenfilename()
        process = subprocess.Popen(file_location)
        pid = process.pid
        app_name = psutil.Process(pid).name()
        appl = apps(app_name, pid)
        app_list.append(appl)
        print(app_name)
        application_list[app] = app_name
        application_list_location[app] = file_location
        print(application_list)
        with open("application_list.txt", "a") as f:
            for app in application_list:
                content = f"{app},{application_list_location[app]} \n"
                f.write(content)

    return 0


# Defining the close function


def close_app(app_name):
    app_name = app_name.lower()
    app_name = app_name.replace("close ", "")
    global app_list, application_list
    try:
        for app_key in application_list:
            if app_name in app_key:
                newapp_name = application_list[app_key]
                print(newapp_name)
            else:
                continue
        for application in app_list:
            if newapp_name in application.app_name:
                subprocess.call(["taskkill", "/IM", newapp_name])
            else:
                continue
        KYLA.say("Done!!!")
    except UnboundLocalError:
        KYLA.say(f"you have not opened {app_name}")


KYLA = Kyla("Kyla", 1)
KYLA.idle()
