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
    for i in self.__surveyDictionary.keys():
      print(self.__surveyDictionary.keys(),':',self.__surveyDictionary[i])
  def getUserMBTI(self):
    return self.__surveyDictionary['MBTI']
  def getUserOpinionAboutPets(self):
    return self.__surveyDictionary['Want/own a pet']
  def getUserInterest(self):
    return self.__surveyDictionary['Interests']
  def getUserAgeImportance(self):
    return self.__surveyDictionary['Age importance']
  def getUserLoveLanguage(self):
    return self.__surveyDictionary['Love language']
  def getUserDesiredTraits(self):
    return self.__surveyDictionary['Desired trait']
  def getUserPersonalityTraits(self):
    return self.__surveyDictionary['Personality trait']
  def getUserReligion(self):
    return self.__surveyDictionary['Religion']
  def getUserOpinionAboutKids(self):
    return self.__surveyDictionary['Want/have children']
  def takeSurvey(self):
    print('You will now take the survey. Please answer these questions to the best of your ability.')
    
    userMBTI = input('What is your Myers-Briggs personality type? ')
    userMBTI.lower()
    surveyQ1 = {'MBTI':userMBTI}
    userOpinionAboutPets = input('Do you own or want to own pets?\n Please press Y if you do or N if you do not. ')
    userOpinionAboutPets.lower()
    surveyQ2 = {'Want/own a pet':userOpinionAboutPets}
    userInterest = input('Which topics are you the most interested in?\n 1) Politics\n 2) Music\n 3) Sports\n 4) Art\n 5) Science\n')
    userInterest.lower()
    userInterest.split(' ')
    surveyQ3 = {'Interests': userInterest}
    userAgeImportance = input('What age difference do you find acceptable? ')
    surveyQ4 = {'Age importance': int(userAgeImportance)}
    userLoveLanguage = input('What is your Love Language(s)? Please write them in a decreasing order of importance.\n 1) Quality time\n 2) Acts of service\n 3) Gift-giving\n 4) Words of Affirmation\n 5) Physical Touch\n')
    userLoveLanguage.lower()
    userLoveLanguage.split(' ')
    surveyQ5 = {'Love language': userLoveLanguage}
    userDesiredTraits = input('What personality trait(s) do you appreciate the most?\n 1) Kindness\n 2) Confidence\n 3) Intelligence\n 4) Bravery\n 5) Humor\n')
    userDesiredTraits.lower()
    userDesiredTraits.split(' ')
    surveyQ6 = {'Desired trait': userDesiredTraits}
    userPersonalityTraits = input('Which adjective(s) fits your personlaity the most? Please write them in a decreasing order of importance.\n 1) Kind\n 2) Confident\n 3) Intelligent\n 4) Brave\n 5) Funny\n') 
    userPersonalityTraits.lower()
    userPersonalityTraits.split(' ')
    surveyQ7 = {'Personality trait': userPersonalityTraits}
    userReligionImportance = input('Is it important that your partner shares your religious viewpoints?\n Please press Y if you do or N if you do not. ')
    userReligionImportance.lower()
    surveyQ8 = {'Religion importance':userReligionImportance}
    userReligion = input('Are you religious?\n 1) Atheist\n 2) Christian\n 3) Muslim\n 4) Hindus\n 5) Satanist\n')
    surveyQ9 = {'Religion': userReligion}
    userFreeTime= input('Would you prefer to spend your free time indoors or outdoors?\n Please press 1 if indoors or 2 if outdoors. ')
    surveyQ10 = {'Free time': userFreeTime}
    userOpinionAboutKids = input('Do you have or want to have kids?\n Please press Y if you do or N if you do not. ')
    userOpinionAboutKids.lower()
    surveyQ11 = {'Want/have kids':userOpinionAboutKids}
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
birthday = input('Birthday (yyyy/mm/dd): ')
surveyDictionary = {}
martialStatus = 'Single'

#username and password will be retrieved from the Management System class

user = User(username, password, firstName, lastName, birthday, surveyDictionary, martialStatus, email)