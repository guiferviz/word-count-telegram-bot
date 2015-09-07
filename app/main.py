# encoding=utf-8


import json
import logging
import webapp2

import appengine_config
from google.appengine.api import modules
from google.appengine.api import app_identity

import telegram

import telegram_token
from service import WordCountService


# Creating the bot and getting basic info of it.
BOT = telegram.Bot(token=telegram_token.TOKEN)
BOT_ME = BOT.getMe()

if not appengine_config.DEBUG:
    # Setting the webhook (callback).
    VERSION = modules.get_current_version_name()
    HOST_NAME = app_identity.get_default_version_hostname()
    HOST_URL = 'https://{}-dot-{}/{}'.format(VERSION, HOST_NAME, telegram_token.TOKEN)
    BOT.setWebhook(HOST_URL)

# Text to send back after substitution.
RESPONSE_TEXT = """Letters: %(letters)s
Words: %(words)s
Lines: %(lines)s
"""

RESPONSE_NO_TEXT = "Please, send me some text. " + telegram.Emoji.PAGE_FACING_UP


class MainPage(webapp2.RequestHandler):

    def get(self):
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.write(BOT_ME)
        self.response.write('\n')
        self.response.write(HOST_URL)

    def post(self):
        json_str = self.request.body
        logging.info("POST Body: " + json_str)
        try:
            json_obj = json.loads(json_str)
            update = telegram.Update.de_json(json_obj)
            chat_id = update.message.chat.id
            text = update.message.text.encode('utf-8')
            if text != '':
                logging.info("Message Text: " + text)
                BOT.sendMessage(chat_id=chat_id,
                                text=self.get_response(text))
            else:
                logging.info("No Message Text.")
                BOT.sendMessage(chat_id=chat_id,
                                text=self.get_response())
        except ValueError:
            logging.error('No body or bad JSON body.')
        except AttributeError:
            logging.error('No correct attributes in JSON body.')

    def get_response(self, text=None):
        if text:
            return RESPONSE_TEXT % WordCountService.count(text)

        return RESPONSE_NO_TEXT

app = webapp2.WSGIApplication([
    ('/' + telegram_token.TOKEN, MainPage),
], debug=appengine_config.DEBUG)
