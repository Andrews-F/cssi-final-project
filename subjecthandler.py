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


class SubjectHandler(webapp2.RequestHandler):
    def post(self):
        template_params = {}
        url = "http://www.khanacademy.org"

        topic = ""

        template = jinja_environment.get_template('html/subject.html')
        self.response.out.write(template.render())
