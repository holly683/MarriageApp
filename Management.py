import db
from User import *
class Management():
  def newUser(self,username,password,firstName,lastName,birthday,gender,romanticPreference):
    #adds a user to the dictionary and creates a user object that is returned
    dic = {
      'password': password, 
      'firstName': firstName,
      'lastname': lastName,
      'birthday': birthday,
      'gender': gender,
      'romanticPreference': romanticPreference
    }
    db[username] = dic
    return User(username,password,firstName,lastName,birthday,gender,romanticPreference)
  def findMatches(self,userToMatch):
    #looks through the dictionary to find the users that most closely match with the user looking for matches. returns a dictionary of the 5 top matches ordered by percentage
  
    
  