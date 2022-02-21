import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
import subprocess
import psutil, os
from bs4 import BeautifulSoup
import urllib
import random
import sys
import win32com.client


class Kyla:
    welcomeList = ["How may I help you?", "What do you need?", "How can I assist you?",
                   "How can I be of assistance to you?", "Is there anything I can help you with?"]

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
        while True:
            r = sr.Recognizer()
            with sr.Microphone() as source:
                print("Listening... ")
                audio = r.listen(source)
                sr.Recognizer().adjust_for_ambient_noise(source)
                sr.Recognizer().dynamic_energy_threshold = 1000
            try:
                print("Recognizing...")
                speech = r.recognize_google(audio)
                os.system("cls")
            except TypeError:
                pass
                continue
            except sr.WaitTimeoutError:
                continue
            except sr.UnknownValueError:
                pass
                continue
            except sr.RequestError:
                os.system("cls")
                continue
            except:
                continue
            if speech == "wiki":
                Kyla.wake(self)
                break
            else:
                pass
                continue


class apps:
    def __init__(self, path, pid):
        self.path = path
        self.pid = pid


# Creating the search function

def search():
    while True:
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print(Kyla.welcome_selector(Kyla))
            audio = r.listen(source)
            sr.Recognizer().adjust_for_ambient_noise(source)
            sr.Recognizer().dynamic_energy_threshold = 1000

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
        except:
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
        elif "who are you" in question.lower():
            KYLA.say("I am Kyla")
        elif "introduce yourself" in question.lower():
            KYLA.say("Hello, I am Kyla. Your voice assistant")
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
        # Sending speech for analysis
        else:
            speech_analyzer(question)

    return 0


def processes(text):
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
    elif "open microsoft" in text.lower():
        KYLA.say("okay!!! I will do that")
        webbrowser.open(f"https://microsoft.com")
    elif "open wiki" in text.lower():
        KYLA.say("okay!!! I will do that")
        webbrowser.open(f"https://wiki.com")


    # Common computer commands
    elif "close file explorer" in text.lower():
        for process in (process for process in psutil.process_iter() if process.name() == "explorer.exe"):
            process.kill()
        KYLA.say("Done!!!")
    elif "open file explorer" in text.lower():
        KYLA.say("okay!!!")
        subprocess.Popen('explorer ""')
    elif "close my documents" in text.lower():
        for process in (process for process in psutil.process_iter() if process.name() == "explorer.exe"):
            process.kill()
        KYLA.say("Done!!!")
    elif "open my documents" in text.lower():
        KYLA.say("okay!!!")
        subprocess.Popen('explorer "C:\temp"')
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


def speech_analyzer(text):
    if "what is" in text:
        processed_text = text.replace("what is", "")
        what_search(processed_text)
    elif "what are " in text:
        processed_text = text.replace("what are", "")
        where_search(processed_text)
    elif "where is " in text:
        processed_text = text.replace("where is", "")
        where_search(processed_text)
    elif "what is the location of " in text:
        processed_text = text.replace("what is the location of", "")
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
        if splitted_text[0].lower() == "open" or splitted_text[0].lower() == "close":
            processes(text)
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

        elif text == "shut down the computer":
            os.system("shutdown /s /t 1")
        elif text == "restart the computer":
            os.system("shutdown /r /t 1")
        elif text == "sleep the computer":
            os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")
        else:
            general_search(text)
    return 0


app_list = []


def search_computer(app):
    global pids
    dir = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\"
    content = []
    for root, sub, files in os.walk(dir):
        for file in files:
            if app in file.lower():
                shell = win32com.client.Dispatch("WScript.Shell")
                shortcut = shell.CreateShortCut(root + "/" + file)
                file_full = shortcut.Targetpath
                if file_full.endswith(".exe") and "launcher" not in file.lower():
                    content.append(file_full)
                for file_uni in content:
                    if "unins" in file_uni:
                        content.remove(file_uni)
                    elif "launcher" in file.lower():
                        content.remove(file)
    if len(content) > 0:
        print(content)
        process = subprocess.Popen(content[0])
        app_name = content[0]
        pid = process.pid
        app_name_1 = psutil.Process(pid).name()
        app = apps(app_name, pid)
        app_list.append(app)
        print(app_name_1)
    elif len(content) <= 0:
        excl_dirs = {'Default','AppData', 'MicrosoftEdgeBackups'}
        dir = "C:\\Users"
        for root, dirnames, files in os.walk(dir):
            dirnames[:] = [d for d in dirnames if d not in excl_dirs]
            for file in files:
                if app in file.lower() and file.endswith(".exe"):
                    whole_file = root + "/" + file
                    content.append(whole_file)
                    for file in content:
                        if "unins" in file.lower():
                            content.remove(file)
                        elif "launcher" in file.lower():
                            content.remove(file)
                elif app in file.lower() and file.endswith(".lnk"):
                    shell = win32com.client.Dispatch("WScript.Shell")
                    shortcut = shell.CreateShortCut(root + "/" + file)
                    file_full = shortcut.Targetpath
                    content.append(file_full)
        if len(content) > 0:
            process = subprocess.Popen(content[0])
            app_name = content[0]
            pid = process.pid
            app_name_1 = psutil.Process(pid).name()
            app = apps(app_name, pid)
            app_list.append(app)
            print(app_name_1)
        else:
            print("File Not Found")
    return app_name_1


def close(name):
    global app_list
    for application in app_list:
        if name in application.path.lower():
            print(app_name)
        else:
            continue


KYLA = Kyla("Kyla", 1)
#KYLA.idle()
search_computer(input("Please enter the name of the software you are looking for.  "))
# ke = input("press enter")
# if ke == "yes":
#     close(input("Please enter the name of the software you are looking to close.  "))
