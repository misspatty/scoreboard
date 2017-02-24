

import wsgiref.handlers
from google.appengine.ext import webapp

class Home(weppap.RequestHandler):
    def get(self):
        self.response.out.write('Welcome To Scoreboard')
        
    def main():
        app = webapp.WSGIApplication([(r'.*', Home)], debug=True)
        
    wsgiref.handlers.CGIHandler().run(application)