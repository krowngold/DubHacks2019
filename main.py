import webapp2
import jinja2
import urllib
import os
import sys
from google.appengine.api import users
from google.appengine.ext import ndb
from google.appengine.api import urlfetch
reload(sys)
sys.setdefaultencoding('utf8')
jinja_env = jinja2.Environment(
    loader = jinja2.FileSystemLoader(os.path.dirname(__file__)))

class CreateProfile(webapp2.RequestHandler): #Allow users access
    def get(self):
        template = jinja_env.get_template("templates/login.html")
        self.response.write(template.render())

    def post(self):
        template_vars = {
            "userName": self.request.get("name"),
            "userPass": self.request.get("password"),
            "userEmail": self.request.get("email"),
        }
        template = jinja_env.get_template("templates/main.html")
        self.response.write(template.render(template_vars))
#
# class LogIn(webapp2.RequestHandler):
#     def get(self):
#         template = jinja_env.get_template("templates/login.html")
#         self.response.write(template.render())
#
#     def post(self):
#         user = auth.sign_in_with_email_and_password(
#                 self.request.get("input_username"),
#                 self.request.get("input_password"),
#                )
#         db = firebase.database()
#         results = db.child("users").push(data, user['idToken'])
#         template = jinja_env.get_template("templates/main.html")
#         self.response.write(template.render(template_vars))

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
    ('/', CreateProfile),
    # ('/login', CreateProfile),
])
