# encoding=utf-8


import webapp2

import appengine_config


class MainPage(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.write('Hello world!')


app = webapp2.WSGIApplication([
    ('/.*', MainPage),
], debug=appengine_config.DEBUG)
