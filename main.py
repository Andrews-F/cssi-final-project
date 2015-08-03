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
# import subjecthandler
import webapp2
from google.appengine.api import urlfetch
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

class HomeHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template('html/home.html')
        self.response.out.write(template.render())


# class SubjectHandler(webapp2.RequestHandler):
#     def get(self):
#         template = jinja_environment.get_template('html/subject.html')
#         self.response.out.write(template.render())

class SubjectHandler(webapp2.RequestHandler):
    def get(self):
        # subject = self.request.get("button")

        template_params = {}
        khan_links = []
        url = "http://www.khanacademy.org"
        topic_link = "/api/v1/topic/"
        topic_slug = "algebra"   #self.request.get("topic_name")
        # videos = "/videos"

        khan_data_source = urlfetch.fetch(url+ topic_link + topic_slug)
        khan_json_content = khan_data_source.content
        parsed_khan_dictionary = json.loads(khan_json_content)

        # for i in
        video_url= parsed_khan_dictionary['children'][i]['url']

        template_params["link"] = video_url
        # template_params["title"] = topic_slug




        coursera_links = []
        base_url = "https://api.coursera.org/api/catalog.v1/courses?q=search&query="
        search_term = self.request.get("search", "algebra")
        course_data_source = urlfetch.fetch(base_url + search_term)
        course_json_content = course_data_source.content
        parsed_course_dictionary = json.loads(course_json_content)
        coursera_length = len(parsed_course_dictionary['elements'])
        for i in range(coursera_length):
            #course_name = parsed_course_dictionary['elements'][i]['name']
            course_short_name = parsed_course_dictionary['elements'][i]['shortName']
            self.response.write(course_short_name)
            link = "https://www.coursera.org/course/" + course_short_name
            coursera_links.append(link)
        self.response.write(coursera_links)

        # template = jinja_environment.get_template('html/subject.html')
        # self.response.out.write(template.render(template_params))


app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/login', LoginHandler),
    ('/home', HomeHandler ),
    ('/subject', SubjectHandler)        #subjecthandler.SubjectHandler)
], debug=True)
