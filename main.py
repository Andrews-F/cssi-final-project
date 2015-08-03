#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

# Make sure to run app like so:
# dev_appserver.py --datastore_consistency_policy=consistent [path_to_app_name]
# in order to see changes reflected in the redirect immediately

# To clear the datastore:
# /usr/local/google_appengine/dev_appserver.py --clear_datastore=1 [path_to_app_name]

#Sofie will see this comment and delete it
#screw yourself
#love you *heart emoji*

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

class User(ndb.Model):
    username = ndb.StringProperty(required=True)
    password = ndb.StringProperty(required=True)
    courses = ndb.StringProperty(repeated=True)



class MainHandler(webapp2.RequestHandler):
    def get(self):
        template_vars ={}
        template_vars["title"] = "Title"


        template = jinja_environment.get_template('html/title.html')
        self.response.out.write(template.render(template_vars))

class LoginHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template('html/login.html')

    def post(self):
        template = jinja_environment.get_template('html/login.html')
        username = self.request.get('username')
        password = self.request.get('password')
        new_username = self.request.get('new_username')
        new_password = self.request.get('new_password')
        new_email = self.request.get('new_email')
        #Questions:
        #How do we  authenticate a user?
        self.response.out.write(template.render(template_vars))

<<<<<<< HEAD
=======
class HomeHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template('html/home.html')
>>>>>>> 44061a3d123ff41495a52256769acab397308a72


class SubjectHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template('html/subject.html')


app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/login', LoginHandler),
    ('/home', homehandler.HomeHandler ),
    ('/subject', SubjectHandler)
], debug=True)
