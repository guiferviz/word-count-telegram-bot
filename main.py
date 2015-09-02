# encoding=utf-8


import webapp2

import appengine_config
from google.appengine.api import app_identity

import telegram

import telegram_token


# Creating the bot and getting basic info of it.
BOT = telegram.Bot(token=telegram_token.TOKEN)
BOT_ME = BOT.getMe()

# Setting the webhook (callback).
HOST_URL = 'https://{}/'.format(app_identity.get_default_version_hostname())
BOT.setWebhook(HOST_URL)


class MainPage(webapp2.RequestHandler):

    def get(self):
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.write(BOT_ME)
        self.response.write(HOST_URL)

    def post(self):
        # retrieve the message in JSON and then transform it to Telegram object
        update = telegram.Update.de_json(self.request.get_json(force=True))

        chat_id = update.message.chat.id

        # Telegram understands UTF-8, so encode text for unicode compatibility
        text = update.message.text.encode('utf-8')

        # repeat the same message back (echo)
        BOT.sendMessage(chat_id=chat_id, text=text)


app = webapp2.WSGIApplication([
    ('/.*', MainPage),
], debug=appengine_config.DEBUG)
 