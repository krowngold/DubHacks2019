import webapp2
import jinja2
import urllib
import logging
import os
import sys
import models
from google.appengine.api import users
from google.appengine.ext import ndb
from google.appengine.api import urlfetch
reload(sys)
sys.setdefaultencoding('utf8')
sys.path.insert(1, '/Users/Noah Krohngold/google-cloud-sdk/platform/google_appengine')
sys.path.insert(1, '/Users/Noah Krohngold/google-cloud-sdk/platform/google_appengine/lib/yaml/lib')
sys.path.insert(1, 'lib')

if 'google' in sys.modules:
    del sys.modules['google']
jinja_env = jinja2.Environment(
    loader = jinja2.FileSystemLoader(os.path.dirname(__file__))
    )

class User(ndb.Model):
  user_name = ndb.StringProperty(required=True)
  user_password = ndb.StringProperty(required=True)
  user_email = ndb.StringProperty(required=True)

class DangerousLocation(ndb.Model):
    location_name = ndb.StringProperty(required=True)
    is_dark = ndb.BooleanProperty(required=True)
    has_suspicious_people = ndb.BooleanProperty(required=True)
    has_violence = ndb.BooleanProperty(required=True)
    has_aggressive_drivers = ndb.BooleanProperty(required=True)

class CreateProfile(webapp2.RequestHandler): #Allow users access
    def checkUser(self, username, password):
        user_list = User.query().fetch()
        for user in user_list:
            if (user.user_name == username and user.user_password == password):
                return True
        return False

    def addUser(self, name, password, email):
        User(user_name=self.request.get("username"), user_password=self.request.get("password"), user_email=self.request.get("email")).put()

    def get(self):
        template = jinja_env.get_template("templates/createprofile.html")
        self.response.write(template.render())

    def post(self):
        if (not self.checkUser(self.request.get("username"), self.request.get("password"))):
            addUser(self.request.get("username"), self.request.get("password"), self.request.get("email"))
            template_vars = {
                "userName": self.request.get("username"),
                "userPass": self.request.get("password"),
                "userEmail": self.request.get("email"),
            }
            template = jinja_env.get_template("templates/main.html")
            self.response.write(template.render(template_vars))
        else:
            template = jinja_env.get_template("templates/createprofile.html")
            self.response.write(template.render())


class LogIn(webapp2.RequestHandler):
    def checkUser(self, username, password):
        user_list = User.query().fetch()
        for user in user_list:
            if (user.user_name == username and user.user_password == password):
                return True
        return False

    def get(self):
        template = jinja_env.get_template("templates/login.html")
        self.response.write(template.render())

    def post(self):
        if (self.checkUser(self.request.get("username"), self.request.get("password"))):
            template = jinja_env.get_template("templates/main.html")
            self.response.write(template.render())
        else:
            template = jinja_env.get_template("templates/login.html")
            self.response.write(template.render())

class MainPage(webapp2.RequestHandler): 
    def get(self):
        template = jinja_env.get_template("templates/main.html")
        self.response.write(template.render())

    def post(self):
        template_vars = {

        }
        template = jinja_env.get_template("templates/main.html")
        self.response.write(template.render(template_vars))

class LocationReportPage(webapp2.RequestHandler):
    def get(self):
        template = jinja_env.get_template("templates/location.html")
        self.response.write(template.render())



app = webapp2.WSGIApplication([
    ('/', CreateProfile),
    ('/create_profile', CreateProfile),
    ('/main', MainPage)
])
