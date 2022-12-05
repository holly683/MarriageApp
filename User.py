import datetime

class User():
  def __init__(self,username,password,firstName,lastName,birthday,gender,romanticPreference):
    self.__username = username
    self.__password = password
    self.__firstName = firstName
    self.__lastName = lastName
    self.__birthday = birthday #should be in YYYY/MM/DD format
    self.__gender = gender
    self.__romanticPreference = romanticPreference
  def getUsername(self):
    return self.__username
  def getPassword(self):
    return self.__password
  def getFirstName(self):
    return self.__firstName
  def getLastName(self):
    return self.__lastname
  def getBirthday(self):
    return self.__birthday
  def getAge(self):
    birthdayDate = datetime.strptime(self.getBirthday(),"%Y/%m/%d")
    currentDate = datetime.datetime.now()
    age = (currentDate - birthdayDate)/365.25
    return age
  def getGender(self):
    return self.__gender
  def getRomanticPreference(self):
    return self.__romanticPreference
  def changePassword(self,newPassword):
    self.__password = newPassword
  def initializeSurvey(self):
    print('survey')
  def takeSurvey():
    print('You will now take the survey. Please answer these questions to the best of your ability.')
  
    