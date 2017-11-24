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
########### Python 2.7 #############
import httplib, urllib, base64
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer



headers = {
    # Request headers
    'Ocp-Apim-Subscription-Key': 'cba30787e3664a648e2d439f9ad9bee7',
}



####################################


reload(sys)
sys.setdefaultencoding('utf-8')

# chatbot = ChatBot('deepThought')
# chatbot.set_trainer(ChatterBotCorpusTrainer)
# chatbot.train("chatterbot.corpus.chinese")
# chatbot.train("chatterbot.corpus.english.greetings")

# Train based on the english conversations corpus
# chatbot.train("chatterbot.corpus.english.conversations")
# Train based on the english corpus
# chatbot.train("chatterbot.corpus.english")

import telepot

# global bot
reply = ["仕文睡的像条狗", "仕文贱仙", "狗仕文", "仕文确实狗"]

class FilterAwesome(BaseFilter):
    def filter(self, message):
        return message.text

        # print("filter update: ", message.chat_id)
        chat_id = message.chat_id
        print("chat_id: ", chat_id)
        wordToCheck = ['fuck', 'asshole', '操']
        print message.text
        if any(ext in message.text for ext in wordToCheck):
            with open('blacklist.txt', 'w+') as inf:
                print ("writing to blacklist")
                inf.write(str(chat_id)+'\n')
                inf.close()
                message.text = "bad language"
                return message.text

        with open('blacklist.txt', 'r') as inf:
            # print(inf)
            blacklist = inf
            for person in blacklist.readlines():
                if chat_id == int(person):
                    print("black list detected")
                    inf.close()
                    return ""

        inf.close()

        params = urllib.urlencode({
            # Query parameter
            'q': message.text,
            # Optional request parameters, set to default values
            'timezoneOffset': '0',
            'verbose': 'false',
            'spellCheck': 'false',
            'staging': 'false',
        })
        try:
            conn = httplib.HTTPSConnection('westus.api.cognitive.microsoft.com')
            conn.request("GET", "/luis/v2.0/apps/9d99a7d5-2564-4c02-b91e-54d6d9c3c076?%s" % params, "{body}", headers)
            response = conn.getresponse()
            data = response.read()
            print(data)
            conn.close()
        except Exception as e:
            print("[Errno {0}] {1}".format(e.errno, e.strerror))

        score = json.loads(data)['topScoringIntent']['score']
        if(score > 0.6):
            key = json.loads(data)['topScoringIntent']['intent']
            print("key: ", key)
            message.text = key
            if key != 'None':
                return key
            # ('hello' in message.text or 'hello' in message.text
            #     or 'development progress' in message.text
            #     or '雷电网络' in message.text)


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

        # return chatbot.get_response(key)

        print key
        dickeys = self.keywords.keys()
        # print dickeys
        for dickey in dickeys:
            if dickey in key:
                return self.keywords[dickey]
        return reply[random.randint(0, 5)]


bot = telegram.Bot(token='455308483:AAEdTcoUQqELit7bFXkVJtPZKHeXN_qTkQY')
print(bot.get_me())

r = Reply()
filter_awesome = FilterAwesome()
# print ("filter_awesome", filter_awesome)

bot.setWebhook()  # unset webhook by supplying no parameter

updater = Updater(token='455308483:AAEdTcoUQqELit7bFXkVJtPZKHeXN_qTkQY')
dispatcher = updater.dispatcher

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)


def start(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="I'm a robot, please talk to me!")


def echo(bot,update):
    print ("echo update.message.chat_id: ", update.message.chat_id)
    msg = update.message.text
    # username = update.message.from_user.username
    print (r.getReply(msg))
    reply = r.getReply(msg)
    print reply
    bot.sendMessage(chat_id=update.message.chat_id, text=reply)

#'@' + str(update.message.from_user.name) + ' ' +
start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

echo_handler = MessageHandler(filter_awesome, echo)
dispatcher.add_handler(echo_handler)

updater.start_polling()

# 'Greet': 'Welcome to Atmatrix community!👏👏Please speak CHINESE or ENGLISH✔️ & Do not forget to read other Rules at Pinned Message',