import webapp2
import jinja2
import urllib
import os
import sys
import models
from google.appengine.api import users
from google.appengine.ext import ndb
from google.appengine.api import urlfetch
reload(sys)
sys.setdefaultencoding('utf8')
jinja_env = jinja2.Environment(
    loader = jinja2.FileSystemLoader(os.path.dirname(__file__)))

class User(ndb.Model):
  user_name = ndb.StringProperty(required=True)
  user_password = ndb.StringProperty(required=True)
  user_email = ndb.StringProperty(required=True)

class CreateProfile(webapp2.RequestHandler): #Allow users access
    def get(self):
        template = jinja_env.get_template("templates/createprofile.html")
        self.response.write(template.render())

    def post(self):
        user = User()
        user.populate(
                user_name = self.request.get("name"),
                user_password = self.request.get("password"),
                user_email = self.request.get("email")
        )
        user.put()
        template_vars = {
            "userName": self.request.get("name"),
            "userPass": self.request.get("password"),
            "userEmail": self.request.get("email"),
        }
        template = jinja_env.get_template("templates/main.html")
        self.response.write(template.render(template_vars))

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
        if (this.checkUser(self.request.get(name), self.request.get(password))):
            template = jinja_env.get_template("templates/main.html")
            self.response.write(template.render(template_vars))
        else:
            template = jinja_env.get_template("templates/login.html")
            self.response.write(template.render(template_vars))

class MainPage(webapp2.RequestHandler): #show map and pins of each unsafe location and why it's unsafe
    # def dataToJSON(self, data):
    #     info = {}
    #     print("placeholder")
    #     with open("data.txt", "w") as outfile:
    #         json.dump(info, outfile)

    def get(self):
        template = jinja_env.get_template("templates/main.html")
        self.response.write(template.render())

    def post(self):
        template_vars = {

        }
        template = jinja_env.get_template("templates/main.html")
        self.response.write(template.render(template_vars))

app = webapp2.WSGIApplication([
    ('/', LogIn),
    ('/create_profile', CreateProfile),
    ('/main', MainPage)
])
