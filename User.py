import datetime

class User():
  def __init__(self,username,password,firstName,lastName,birthday,gender,romanticPreference, surveyDictionary, martialStatus):
    self.__username = username
    self.__password = password
    self.__firstName = firstName
    self.__lastName = lastName
    self.__birthday = birthday #should be in YYYY/MM/DD format
    self.__gender = gender
    self.__romanticPreference = romanticPreference
    self.__martialStatus = martialStatus
    self.__surveyDictionary = surveyDictionary
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
  def getMartialStatus(self):
    return self.__martialStatus
  def getSurveyAnswers(self):
    return self.__surveyDictionary
  def takeSurvey(self):
    print('You will now take the survey. Please answer these questions to the best of your ability.')
    
    userMBTI = input('What is your Myers-Briggs personality type? ')
    surveyQ1 = {'mbti':userMBTI}
    userOpinionAboutPets = input('Do you own or want to own pets?\n Please press Y if you do or N if you do not. ')
    surveyQ2 = {'pets':userOpinionAboutPets}
    userInterest = input('Which one of the following topics are you the most interested in?\n 1) Politics; 2) Music; 3) Sports; 4) Art; 5) Science: ')
    surveyQ3 = {'interest': userInterest}
    userAgeImportance = input('What age difference do you find acceptable?\n 1) Up to a year; 2) Up to three years; 3) Up to five years; 4) Up to seven years; 5) It does not matter. ')
    surveyQ4 = {'age importance': userAgeImportance}
    userLoveLanguage = input('What is your Love Language?\n 1) Quality time; 2) Acts of service; 3) Gift-giving; 4) Words of Affirmation; 5)Physical Touch: ')
    surveyQ5 = {'love language': userLoveLanguage}
    userDesiredTraits = input('What personality trait do you appreciate the most?\n 1) Kindness; 2) Confidence; 3) Intelligence; 4) Bravery; 5) Humor: ')
    surveyQ6 = {'desired trait': userDesiredTraits}
    userPersonalityTraits = input('Which adjective fits your personlaity the most?\n 1) Kind; 2) Confident; 3) Intelligent; 4) Brave; 5) Funny: ') 
    surveyQ7 = {'personality trait': userPersonalityTraits}
    userReligionImportance = input('Is it important that your partner shares your religious viewpoints?\n Please press Y if you do or N if you do not. ')
    surveyQ8 = {'religion':userReligionImportance}
    userReligion = input('Are you religious?\n 1) Atheist; 2) Christian; 3) Muslim; 4) Hindus; 5) Satanist: ')
    surveyQ9 = {'religion': userReligion}
    userFreeTime= input('Would you prefer to spend your free time indoors or outdoors?\n Please press 1 if indoors or 2 if outdoors. ')
    surveyQ10 = {'free time': userFreeTime}
    userOpinionAboutKids = input('Do you have or want to have kids?\n Please press Y if you do or N if you do not. ')
    surveyQ11 = {'kids':userOpinionAboutKids}
    self.__surveyDictionary.update(surveyQ1)
    self.__surveyDictionary.update(surveyQ2)
    self.__surveyDictionary.update(surveyQ3)
    self.__surveyDictionary.update(surveyQ4)
    self.__surveyDictionary.update(surveyQ5)
    self.__surveyDictionary.update(surveyQ6)
    self.__surveyDictionary.update(surveyQ7)
    self.__surveyDictionary.update(surveyQ8)
    self.__surveyDictionary.update(surveyQ9)
    self.__surveyDictionary.update(surveyQ10)
    self.__surveyDictionary.update(surveyQ11)

    return self.__surveyDictionary

firstName = input('Your name: ')
lastName = input('Last name: ') 
birthday = input('Birthday (dd-mm-yy): ')
surveyDictionary = {}
martialStatus = 'Single'

#username and password will be retrieved from the Management System class

user = User(username, password, firstName, lastName, birthday, surveyDictionary, martialStatus, email)