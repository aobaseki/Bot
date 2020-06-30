from flask import Flask, request as req
import telegram
from config import *
from helpers import getReponse,selectCommand
from database import database

bot = telegram.Bot(token=botToken)

print(botURL)

app = Flask(__name__)


@app.route("/{}".format(botToken), methods=["post"])
def response():
    #Passing the update to telegram readable obj
    update = telegram.Update.de_json(req.get_json(force=True), bot)
    
    """ EXTRACT UPDATE PARAMS"""
    chat =  update.message.chat # the chat object
    user = update.message.from # the user object
    message = update.message # the message object
    # Extract important information about the chat
    chatId = update.message.chat.id
    msgId = update.message.message_id
    
    # PULL THE USERS CONVERSATION HISTORY #
    lastChat = database.get("conversations", user.id)
    if not lastChat:
        selectCommand(message.text[1:])
    else:
        continueConversation(lastChat)



    
    text = update.message.text.encode("utf-8").decode()
    user = update.message
    print("Recieved: {}".format(text))
    

    response  = getReponse(text, user = user)
    
    bot.send_message(chat_id=chatId, text=response, reply_to_message_id=msgId)
    return "ok"


@app.route('/setwebhook', methods=['GET', 'POST'])
def set_webhook():
   
    s = bot.setWebhook(botURL)
    
    if s:
        return "webhook setup ok"
    else:
        return "webhook setup failed"


@app.route("/")
def home():
    return "<h1>Hey, we are live</h1>"



if __name__ == "__main__":
    app.run(debug=True, threaded=True)