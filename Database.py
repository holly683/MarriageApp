from User import *
from replit import db


class Database():
  def __init__(self):
    self.__userList = self.populateUserList()

  def findUserByUsername(self, username):
    for user in self.getUserList():
      if user.getUsername() == username:
        return user
    return -1

  def deleteUserByUsername(self, username):
    for user in self.getUserList():
      if user.getUsername() == username:
        del db[username]
    return -1

  def findPassByUser(self, username):
    for user in self.getUserList():
      if user.getUsername() == username:
        return user.getPassword()
    return -1
  
  def stringToBool(self, s):
    if s == "True":
      return True
    else:
      return False
  def updateDatabase(self,userToUpdate):
    userString = userToUpdate.userToString()
    db[userToUpdate.getUsername()] = userString
  
  def getUserFromDB(self, userString):
    userSplit = userString.split()
    username = userSplit[0]
    password = userSplit[1]
    firstName = userSplit[2]
    lastName = userSplit[3]
    birthday = userSplit[4]
    gender = userSplit[5]
    romanticPreference = userSplit[6].split(',')
    maritalStatus = userSplit[7]
    try:
      mbti = userSplit[8]
      wantPet = self.stringToBool(userSplit[9])
      interests = userSplit[10].split(',')
      ageRange = userSplit[11]
      loveLanguages = userSplit[12].split(',')
      traitsWanted = userSplit[13].split(',')
      traits = userSplit[14].split(',')
      religionImportance = self.stringToBool(userSplit[15])
      religion = userSplit[16]
      wantKids = self.stringToBool(userSplit[17])
      inOutDoors = userSplit[18]
      newUser = User(username, password, firstName, lastName, birthday, gender, romanticPreference, {}, maritalStatus)
      newUser.initializeSurvey(mbti, wantPet, interests, ageRange, loveLanguages, traitsWanted, traits, religionImportance,religion, wantKids, inOutDoors)
    except:
      newUser = User(username, password, firstName, lastName, birthday, gender, romanticPreference, {}, maritalStatus)
    return newUser
    
  def populateUserList(self):
    userList = []
    for username in db:
      userList.append(self.getUserFromDB(db[username]))
    return userList

  def getUserList(self):
    return self.__userList

  def updateUserList(self,userToAdd):
    self.__userList.append(userToAdd)


