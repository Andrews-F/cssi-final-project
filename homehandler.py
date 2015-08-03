import jinja2
import json
import os
import homehandler
import webapp2
from google.appengine.ext import ndb

jinja_environment = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)


class HomeHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template('html/home.html')
        self.response.out.write(template.render())
