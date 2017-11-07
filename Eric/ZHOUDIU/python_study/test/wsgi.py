# -*- coding: utf-8 -*-

import os

import leancloud
from wsgiref import simple_server
from flask import Flask
from flask import  request
import BaseHTTPServer, SimpleHTTPServer, telegram
import ssl

from app import app
from cloud import engine
from telegram.ext import Updater

# APP_ID = os.environ['LC_APP_ID']
# MASTER_KEY = os.environ['LC_APP_MASTER_KEY']
# PORT = int(os.environ['LC_APP_PORT'])


leancloud.init("9h2X2bVBPEjbsPclAkA4Wdtn-gzGzoHsz", "vrelQEhlgsMeugfjxE9SYYOF")

application = engine


# if __name__ == '__main__':
#     # 只在本地开发环境执行的代码
#     app.debug = True
#     httpd = BaseHTTPServer.HTTPServer(('localhost', 80), SimpleHTTPServer.SimpleHTTPRequestHandler)
#     httpd.socket = ssl.wrap_socket(httpd.socket, keyfile="./server.key", certfile="./server.crt", server_side=True)
#     httpd.serve_forever()

#
# if __name__ == '__main__':
#     # 只在本地开发环境执行的代码
#     app.debug = True
#     server = simple_server.make_server('localhost', 80, application)
#     server.serve_forever()
TOKEN = 'test'
HOST = 'localhost' # Same FQDN used when generating SSL Cert
PORT = 80
CERT = './server.crt'
CERT_KEY = './server.key'

bot = telegram.Bot(token='455308483:AAEdTcoUQqELit7bFXkVJtPZKHeXN_qTkQY')
app = Flask(__name__)
context = (CERT, CERT_KEY)

# updater.start_webhook(listen='0.0.0.0',
#                       port=8443,
#                       url_path='TOKEN',
#                       key='private.key',
#                       cert='cert.pem',
#                       webhook_url='https://example.com:8443/TOKEN')
updater = Updater(token='455308483:AAEdTcoUQqELit7bFXkVJtPZKHeXN_qTkQY')
updater.start_webhook(listen='0.0.0.0',
                     port=8443,
                     url_path='455308483:AAEdTcoUQqELit7bFXkVJtPZKHeXN_qTkQY',
                     key='private.key',
                     cert='cert.pem',
                     webhook_url='https://localhost:8443/455308483:AAEdTcoUQqELit7bFXkVJtPZKHeXN_qTkQY')

# @app.route('/')
# def hello():gb]

#     return 'Hello World!'
#
# @app.route('/' + TOKEN, methods=['POST'])
# def webhook():
#     update = telegram.update.Update.de_json(request.get_json(force=True))
#     bot.sendMessage(chat_id=update.message.chat_id, text='Hello, there')
#
#     return 'OK'
#
#
# def setWebhook():
#     print("=======start========")
#     bot.setWebhook(url='https://%s:%s/%s' % (HOST, PORT, TOKEN),
#                    certificate=open(CERT, 'rb'))
#     print("=======end========")
#
# if __name__ == '__main__':
#     setWebhook()
#
#     app.run(host='0.0.0.0',
#             port=PORT,
#             ssl_context=context,
#             debug=True)