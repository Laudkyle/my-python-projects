import nltk
import speech_recognition as sr
import pyttsx3
from bs4 import BeautifulSoup
from nltk.corpus import stopwords
import urllib
import re
#nltk.download('punkt')

def speak(ans):
	engine = pyttsx3.init()
	voices = engine.getProperty('voices')
	engine.setProperty('voice', voices[1].id)
	engine.setProperty('rate', 150)
	engine.say(ans)
	engine.runAndWait()


def search():
	r = sr.Recognizer()
	with sr.Microphone() as source:
		print("Record :  ")
		audio = r.listen(source)

		try:
			text = r.recognize_google(audio)
		except:
			speak("Could not recognize your voice, please try again.  ")
	txt = ""
	text_splitted = ""
	web = urllib.request.urlopen(f"https://en.wikipedia.org/wiki/{text}").read()
	soup = BeautifulSoup(web, 'lxml')
	for paragraph in soup.find_all("p"):
		txt += paragraph.text
	# Processing the data
	txt = re.sub(r'\[[0-9]*\]',' ',txt)
	txt = re.sub(r'\s+',' ',txt)
	txt = re.sub(r'\d ', ' ', txt)
	sentences = nltk.sent_tokenize(txt)
	for line in range(3):
		text_splitted += sentences[line]
	text_splitted = text_splitted.replace(".", ". ")
	print(sentences)
	print()
	print(text_splitted)
	speak(f"According to wikipedia, {text_splitted}")




search()