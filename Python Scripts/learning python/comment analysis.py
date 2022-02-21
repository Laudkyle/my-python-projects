import speech_recognition as sr
import text2emotion as te


keyword_p = ["nice", "cool", "I like it", "I love it", "definitely", "absolutely",
             "definitely", "absolutely", "certainly", "exactly", "completely", "quickly", "fantastic", "great",
             "marvellous", "excellent", "enjoy", "splendid", "essential", "generous", "recommend", "friendly",
             "impressive", "interesting", "brilliant", "exciting", "terrific", "fascinating", "expert", "favourite",
             "ideal"]
reviews = []
positive, negative = 0, 0
r = sr.Recognizer()

with sr.Microphone() as source:
    print("How was the customer service :  ")
    audio = r.listen(source)

    try:
        text = r.recognize_google(audio)
        print(f"You said : {text}")
    except:
        print("Could not recognize your voice, please.try again.  ")


def review(audio_text):
    global keyword_p
    global reviews
    for key in keyword_p:
        if key in audio_text:
            reviews.append(key)
    print(reviews)


# Calling the review
def review_count(lis):
    global positive
    global negative
    for item in lis:
        if item in lis:
            positive += 1



review(text)
review_count(reviews)
mood = te.get_emotion(text)
print(f"The customer was {mood}")
