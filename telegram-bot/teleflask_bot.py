from flask import Flask, request
from flask.wrappers import Response
from telegram import Bot
from telegram.update import Update
from const import BOT_TOKEN, BOT_USERNAME, BOT_URL
import random
import logging


bot = Bot(BOT_TOKEN)
welcome_message = 'ciao sono un bot creato per imparare ad usare docker con flask, nginx e gunicorn'
words = ['mi piacciono gli scale up', 'ciao sono un bot che funziona su docker', 'anche questa volta si prende A', 'british english', 'ominio secchiello']


def send_random(update, bot):
    chat_id = update.message.chat_id
    bot.sendMessage(chat_id= chat_id, text= random.choice(words))

def start_message(update, bot):
    chat_id = update.message.chat_id
    bot.sendMessage(chat_id= chat_id, text=welcome_message)

functions:  'dict[str, callable]' = {'/start' : start_message, '/random': send_random }

def create_flask_bot(token, username) -> Flask:

    logging.basicConfig(filename= "bot.log", level=logging.DEBUG)
    tbot = Flask(__name__)

    @tbot.route('/{}'.format(BOT_TOKEN), methods=['POST'])
    def handle_message():

        #parse json request to telegram object request with python-telegram-bot lib!
        update = Update.de_json(request.get_json(force=True), bot=bot)
        try:
            functions[update.message.text](update, bot)
        except: KeyError

        return Response(status=200)

    @tbot.route('/')
    def set_webhook():
        return 'OK'

    return tbot

appl = create_flask_bot(token= BOT_TOKEN, username= BOT_USERNAME)






