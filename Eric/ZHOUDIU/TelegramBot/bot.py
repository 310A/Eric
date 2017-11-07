# -*- coding: utf-8 -*-
import sys
import urllib2
import json
import threading
import random
import logging
import telegram
from telegram.ext import Updater
from telegram.ext import MessageHandler, Filters
from telegram.ext import CommandHandler
from telegram.ext import BaseFilter


reload(sys)
sys.setdefaultencoding('utf-8')
import telepot

# global bot

class FilterAwesome(BaseFilter):
    def filter(self, message):
        return ('hello' in message.text or 'hello' in message.text
                or 'development progress' in message.text
                or '雷电网络' in message.text)


class Reply:
    def __init__(self):
        self.keywords = None
        with open('keywords.txt', 'r') as inf:
            data = eval(inf.read())
            self.keywords = data
        # self.spider = Spider()

    def getReply(self, key):
        msg = self.__getReplyLocal__(key)
        if msg == None:
            return ""
        print msg
        return msg

    def __getReplyLocal__(self, key):
        dickeys = self.keywords.keys()
        # print dickeys
        for dickey in dickeys:
            if dickey in key:
                return self.keywords[dickey]
        return None


bot = telegram.Bot(token='455308483:AAEdTcoUQqELit7bFXkVJtPZKHeXN_qTkQY')
print(bot.get_me())

r = Reply()
filter_awesome = FilterAwesome()

bot.setWebhook()  # unset webhook by supplying no parameter

updater = Updater(token='455308483:AAEdTcoUQqELit7bFXkVJtPZKHeXN_qTkQY')
dispatcher = updater.dispatcher

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)


def start(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="I'm a robot, please talk to me!")


def echo(bot,update):
    msg = update.message.text
    # username = update.message.from_user.username
    reply = r.getReply(msg)
    bot.sendMessage(chat_id=update.message.chat_id, text=reply)


start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

echo_handler = MessageHandler(filter_awesome, echo)
dispatcher.add_handler(echo_handler)

updater.start_polling()