from google.appengine.ext import ndb

class User(ndb.Model):
  user_name = ndb.StringProperty(required=True)
  user_password = ndb.StringProperty(required=True)
  user_email = ndb.StringProperty(required=True)
