# from flask import Flask, render_template as rt, request
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
import speech_recognition as sr
from threading import Timer
#  app = Flask(__name__)
test_bot = ChatBot("Chatterbot", storage_adapter="chatterbot.storage.SQLStorageAdapter")
trainer = ChatterBotCorpusTrainer(test_bot)
trainer.train("chatterbot.corpus.Denodo")
print("Hello, thank you for contacting Denodo’s live chat service. The scope of this chat is to guide you on the "
      "community website with required technical direction. How can I assist you today?")
usertext="0"
cnt=0
while usertext != "thanks":
    timeout = 15
    t = Timer(timeout, print, ['Are you still here????'])
    t.start()
    usertext = input()
    t.cancel()
    if usertext=="speech":
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("mmm sollunga")
            audio = r.listen(source)
            print("0")
            try:
                print("1")
                out = r.recognize_google(audio)
                print("Did you say:{}??".format(out))
                print(str(test_bot.get_response(out)))
            except:
                print("Sorry come again...")
    elif(usertext!="0"):
        print("bot:"+str(test_bot.get_response(usertext)))
