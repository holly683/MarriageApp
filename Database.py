from User import *
from replit import db


class Database():

  def __init__(self, userList):
    self.__userList = userList

  def findUserByUsername(self, username):
    for user in db:
      if user.getUsername() == username:
        return user
    return -1

  def deleteUserByUsername(self, username):
    for user in db:
      if user.getUsername() == username:
        del db[username]
    return -1

  def findPassByUser(self, username):
    for user in db:
      if user.getUsername() == username:
        if user.getPassword() == db[user.getUsername()[1]]:
          return db[user.getUsername()[1]]
    return -1

  def listToString(self, l):
    s = ""
    for x in l:
      s = s + x + ','
    s = s[:-1]
    return s

  def stringToBool(self, s):
    if s == "True":
      return True
    else:
      return False

  def getUserFromDB(self, username):
    userSplit = db[username].split()
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
      wantPet = stringToBool(userSplit[9])
      interests = userSplit[10].split(',')
      ageRange = userSplit[11]
      loveLanguages = userSplit[12].split(',')
      traitsWanted = userSplit[13].split(',')
      traits = userSplit[14].split(',')
      religionImportance = stringToBool(userSplit[15])
      religion = userSplit[16]
      wantKids = stringToBool(userSplit[17])
      inOutDoors = userSplit[18]
      newUser = User(username, password, firstName, lastName, birthday, gender, romanticPreference, {}, maritalStatus)
      newUser.initializeSurvey(mbti, wantPet, interests, ageRange,loveLanguages, traitsWanted, traits, religionImportance, religion, wantKids, inOutDoors)
    except:
      newUser = User(username, password, firstName, lastName, birthday, gender, romanticPreference, {}, maritalStatus)
    return newUser

  def populateUserList(self):
    userList = []
    for userString in db:
      userList.append(getUserFromDB(db[userString]))
    return userList


db[newUser.getUsername()] = userString
