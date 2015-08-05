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

#Uploading to app engine
# in terminal:  appcfg.py --oauth2 -A cssi-final-project-2015 update .

import jinja2
import json
import os
import webapp2
from google.appengine.api import users, urlfetch
from google.appengine.ext import ndb

jinja_environment = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

def UserExists(some_user):
    #does user exist in our database?
    some_email = some_user.email()
    user_query = UserInfo.query() #Could've filtered
    all_users = user_query.fetch()
    for individual in all_users:
        if individual.our_user_email == some_email:
            return True
    return False

def CreateUser(some_user):
    #put new user into our database
    some_email = some_user.email()
    courses = ["Calculus", "Physics", "Computer Science"] #temporarily hardcoded
    name = UserInfo(our_user_email=some_email, courses=courses)
    name.put()

def GetCourseList(some_user):
    #returns list of courses saved by user
    some_email = some_user.email()
    user_query = UserInfo.query()
    filtered_query = user_query.filter(UserInfo.our_user_email == some_email)
    list_user = filtered_query.fetch()
    this_user = list_user[0]
    courses = this_user.courses
    return courses



class UserInfo(ndb.Model):
    our_user_email = ndb.StringProperty(required=True)
    courses = ndb.StringProperty(repeated=True)


class MainHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template('html/title.html')
        self.response.out.write(template.render())


class HomeHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template('html/home.html')
        self.response.out.write(template.render())


class LoginHandler(webapp2.RequestHandler):
    def get(self):
        new_user = users.get_current_user()
        if new_user:
            if not UserExists(new_user):
                greeting = "Welcome {}, looks like you're new here.".format(new_user.nickname())
                CreateUser(new_user)
            else:
                greeting = "Welcome back {}!".format(new_user.nickname())
            logout = users.create_logout_url('/')
            link1 = "/personal"
            tag1 = "Go to your personal page"
            link2 = logout
            tag2 = "Sign out"
        else:
            greeting = "Welcome to our page! To keep track of your favorite courses, sign in with your Google account:"
            login = users.create_login_url('/login')
            link1 = "/"
            tag1 = "Go back to home"
            link2 = login
            tag2 = "Sign in"
        template = jinja_environment.get_template('html/newlogin.html')
        template_vars = {'home_or_personal': link1, 'h_or_p': tag1, 'login_or_out': link2, 'in_out_tag': tag2, 'greeting': greeting}
        self.response.out.write(template.render(template_vars))


class PersonalHandler(webapp2.RequestHandler):
    def get(self):
        current_user = users.get_current_user()
        if current_user:
            nickname = current_user.nickname()
            if not UserExists(current_user):
                CreateUser(current_user)
            course_list = GetCourseList(current_user)
            logout = users.create_logout_url('/')
            template_vars = {'nickname': nickname, 'courses': course_list, 'logouturl': logout}
            template = jinja_environment.get_template('html/mypage.html')
            self.response.out.write(template.render(template_vars))

        else:
            #greeting = ('<a href="%s">Sign in</a>.'%users.create_login_url('/'))
            login = users.create_login_url('/')
            template_vars = {'loginurl': login}
            template = jinja_environment.get_template('html/newlogin.html')
            self.response.out.write(template.render(template_vars))


class SubjectHandler(webapp2.RequestHandler):
    def get(self):
        template_vars = {}
        template_vars['subject'] = self.request.get("search", "algebra")

        template_vars['khan_courses'] = {}
        khan_links = []
        khan_base_url = "http://www.khanacademy.org/api/v1/topic/"
        topic_slug = template_vars['subject']
        khan_data_source = urlfetch.fetch(khan_base_url + topic_slug)
        khan_json_content = khan_data_source.content
        parsed_khan_dictionary = json.loads(khan_json_content)
        khan_length = len(parsed_khan_dictionary['children'])

        for i in range(khan_length):
            khan_course_name = parsed_khan_dictionary['children'][i]['title']
            link= parsed_khan_dictionary['children'][i]['url']
            khan_links.append([khan_course_name,link])

        for i in range(len(khan_links)):
            #puts the info [course name, link] into the template_vars to pass to html
            name = khan_links[i][0]
            link = khan_links[i][1]
            course_info = {name: link}
            template_vars['khan_courses'].update(course_info)


        template_vars['coursera_courses'] = {}
        coursera_links = [] #a list of [name, link]
        coursera_base_url = "https://api.coursera.org/api/catalog.v1/courses?q=search&query="
        search_term = template_vars['subject'].replace("-", "+")
        course_data_source = urlfetch.fetch(coursera_base_url + search_term + "&languages=en")
        course_json_content = course_data_source.content
        parsed_course_dictionary = json.loads(course_json_content)
        coursera_length = len(parsed_course_dictionary['elements'])

        for i in range(coursera_length):
            #makes list of [course name, link]
            coursera_course_name = parsed_course_dictionary['elements'][i]['name']
            course_short_name = parsed_course_dictionary['elements'][i]['shortName']
            link = "https://www.coursera.org/course/" + course_short_name
            coursera_links.append([coursera_course_name, link])

        for i in range(len(coursera_links)):
            #puts the info [course name, link] into the template_vars to pass to html
            name = coursera_links[i][0]
            link = coursera_links[i][1]
            course_info = {name: link}
            template_vars['coursera_courses'].update(course_info)


        template_vars['itunes_courses'] = {}
        itunes_links = []
        itunes_base_url1 = "http://ax.itunes.apple.com/WebObjects/MZStoreServices.woa/wa/wsSearch?term="
        itunes_base_url2 = "&media=iTunesU&entity=podcast"
        itunes_data_source = urlfetch.fetch(itunes_base_url1 + search_term + itunes_base_url2)
        itunes_json_content = itunes_data_source.content
        parsed_itunes_dictionary = json.loads(itunes_json_content)
        itunes_length = len(parsed_itunes_dictionary['results'])

        for i in range(itunes_length):
            #makes list of [course name, link]
            itunes_course_name = parsed_itunes_dictionary['results'][i]["collectionName"]
            link = parsed_itunes_dictionary['results'][i]["collectionViewUrl"]
            itunes_links.append([itunes_course_name, link])

        for i in range(len(itunes_links)):
            #puts the info [course name, link] into the template_vars to pass to html
            name = itunes_links[i][0]
            link = itunes_links[i][1]
            itunes_info = {name: link}
            template_vars['itunes_courses'].update(itunes_info)

        template = jinja_environment.get_template('html/subject.html')
        self.response.out.write(template.render(template_vars))


class CreditHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template('html/credits.html')
        self.response.out.write(template.render())

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/login', LoginHandler),
    ('/home', HomeHandler ),
    ('/subject', SubjectHandler),
    ('/credits', CreditHandler),
    ('/personal', PersonalHandler)
], debug=True)
