import jinja2
import json
import os
import webapp2
from google.appengine.api import urlfetch

jinja_environment = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)


class SubjectHandler(webapp2.RequestHandler):
    def get(self):
        template_params = {}
        url = "http://www.khanacademy.org"
        topic_link = "/api/v1/topic/"
        topic_slug = "algebra"   #self.request.get("topic_name")
        # videos = "/videos"

        khan_data_source = urlfetch.fetch(url+ topic_link + topic_slug)
        khan_json_content = khan_data_source.content
        parsed_khan_dictionary = json.loads(khan_json_content)
        video_url= parsed_khan_dictionary['children'][0]['url']

        template_params["link"] = video_url
        # template_params["title"] = topic_slug


        template = jinja_environment.get_template('html/subject.html')
        self.response.out.write(template.render(template_params))
