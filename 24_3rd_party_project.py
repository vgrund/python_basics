#pip install -U textblob
#python -m textblob.download_corpora lite
#pip install pyttsx3

from textblob import TextBlob
import pyttsx3

engine = pyttsx3.init()
message = "Enter your employee wellness statement: "
engine.say(message)
engine.runAndWait()

print(message)
phrase = input("> ")
blob = TextBlob(phrase)

while blob.sentiment.polarity < 0.5:
    message = "More positive please: "
    print(message)
    engine.say(message)
    engine.runAndWait()
    phrase = input("> ")
    blob = TextBlob(phrase)

message = "We appreciate you too"
print(message)
engine.say(message)
engine.runAndWait()
