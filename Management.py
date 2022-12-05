import db
from User import *
class Management():
  def newUser(self,username,password,firstName,lastName,birthday,gender,romanticPreference):
    db[username] = [password,firstName,lastName,birthday,gender,romanticPreference]
    return User(username,password,firstName,lastName,birthday,gender,romanticPreference)
    
  