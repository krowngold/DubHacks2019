import webapp2
import logging
import jinja2
import os
import sys
import json
import simplejson
import googlemaps
import urllib
from datetime import datetime
from google.appengine.api import users
from google.appengine.ext import ndb
from google.appengine.api import urlfetch
reload(sys)
sys.setdefaultencoding('utf8')
jinja_env = jinja2.Environment(
    loader = jinja2.FileSystemLoader(os.path.dirname(__file__)))

class MainPage(webapp2.RequestHandler):
    def get(self):
        template_vars = {
            "location": getLocation(),
            "food": getFoodType(),
            "selection": randomSelection(),
        }
        print("placeholder")
        template = jinja_env.get_template("templates/main.html")
        self.response.write(template.render(template_vars))

    def post(self):
        template_vars = {
            "location": self.request.get("search"),
            "food": self.request.get("food"),
            "radius": self.request.get("radius"),
            "selection": randomSelection(location, food, radius)
        }
        template = jinja_env.get_template("templates/main.html")
        self.response.write(template.render(template_vars))

app = webapp2.WSGIApplication([
    ('/', MainPage),
])
