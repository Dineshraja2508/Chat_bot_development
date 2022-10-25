# from flask import Flask, render_template as rt, request
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

#  app = Flask(__name__)
test_bot = ChatBot("Chatterbot", storage_adapter="chatterbot.storage.SQLStorageAdapter")
trainer=ChatterBotCorpusTrainer(test_bot)
trainer.train("chatterbot.corpus.hindi")
print(" Hello, thank you for contacting Denodo’s live chat service. The scope of this chat is to guide you on the community website with required technical direction. How can I assist you today?")
usertext ="0"
while usertext!="thanks":
    usertext = input()
    print(str(test_bot.get_response(usertext)))



"""
@app.route("/bottest")
def home():
    return rt("dummy.html")


@app.route("/bottext")
def get_bot_response():
    

if __name__=='__main__':
    app.run(debug=True)"""