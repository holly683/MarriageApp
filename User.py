import datetime

class User():
  def __init__(self,username,password,firstName,lastName,birthday,gender,romanticPreference, surveyDictionary, maritalStatus):
    self.__username = username
    self.__password = password
    self.__firstName = firstName
    self.__lastName = lastName
    self.__birthday = birthday #should be in YYYY/MM/DD format
    self.__gender = gender
    self.__romanticPreference = romanticPreference
    self.__surveyDictionary = surveyDictionary
    self.__maritalStatus = maritalStatus
  def getUsername(self):
    return self.__username
  def getPassword(self):
    return self.__password
  def getFirstName(self):
    return self.__firstName
  def getLastName(self):
    return self.__lastName
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
  def getMaritalStatus(self):
    return self.__maritalStatus
  def getSurveyAnswers(self):
    # for i in self.__surveyDictionary.keys():
    #   print(self.__surveyDictionary.keys(),':',self.__surveyDictionary[i])
    return self.__surveyDictionary
  def getUserMBTI(self):
    #print('mbti')
    return self.__surveyDictionary['MBTI']
  def getUserOpinionAboutPets(self):
    #print('pets')
    return self.__surveyDictionary['WantPet']
  def getUserInterest(self):
    #print('interests')
    return self.__surveyDictionary['Interests']
  def getUserAgeImportance(self):
    #print('ageim')
    return self.__surveyDictionary['AgeRange']
  def getUserLoveLanguage(self):
    #print('ll')
    return self.__surveyDictionary['LoveLanguage']
  def getUserDesiredTraits(self):
    #print('dtrait')
    return self.__surveyDictionary['DesiredTraits']
  def getUserPersonalityTraits(self):
    #print('ptrait')
    return self.__surveyDictionary['PersonalityTraits']
  def getUserReligionImportance(self):
    #print('relim')
    return self.__surveyDictionary['ReligionImportance']
  def getUserReligion(self):
    return self.__surveyDictionary['Religion']
  def getUserOpinionAboutKids(self):
    #print('kids')
    return self.__surveyDictionary['WantKids']
  def printSurveyAnswers(self):
    for x in self.getSurveyAnswers():
      print(self.getSurveyAnswers()[x])
  def initializeSurvey(self,interests,traits,traitsWanted,mbti,loveLanguages,ageRange,pet,religionImportance,religion,kids):
    self.__surveyDictionary['MBTI'] = mbti
    self.__surveyDictionary['WantPet'] = pet
    self.__surveyDictionary['Interests'] = interests
    self.__surveyDictionary['AgeRange'] = ageRange
    self.__surveyDictionary['LoveLanguage'] = loveLanguages
    self.__surveyDictionary['DesiredTraits']=traitsWanted
    self.__surveyDictionary['PersonalityTraits']=traits
    self.__surveyDictionary['ReligionImportance'] = religionImportance
    self.__surveyDictionary['Religion'] = religion
    self.__surveyDictionary['WantKids'] = kids
  def takeSurvey(self):
    print('You will now take the survey. Please answer these questions to the best of your ability.')
    
    userMBTI = input('What is your Myers-Briggs personality type? ')
    surveyQ1 = {'MBTI':userMBTI.upper()}
    userOpinionAboutPets = input('Do you own or want to own pets?\n Please press Y if you do or N if you do not. ')
    surveyQ2 = {'WantPet':userOpinionAboutPets.lower()}
    userInterest = input('Which topics are you the most interested in?\n 1) Politics\n 2) Music\n 3) Sports\n 4) Art\n 5) Science\n')
    surveyQ3 = {'Interests': userInterest.split(' ')}
    userAgeImportance = input('What age difference do you find acceptable? ')
    surveyQ4 = {'AgeRange': int(userAgeImportance)}
    userLoveLanguage = input('What is your Love Language(s)? Please write them in a decreasing order of importance.\n 1) Quality time\n 2) Acts of service\n 3) Gift-giving\n 4) Words of Affirmation\n 5) Physical Touch\n')
    surveyQ5 = {'LoveLanguage': userLoveLanguage.split(" ")}
    userDesiredTraits = input('What personality trait(s) do you appreciate the most?\n 1) Kindness\n 2) Confidence\n 3) Intelligence\n 4) Bravery\n 5) Humor\n')
    surveyQ6 = {'DesiredTraits': userDesiredTraits.split(' ')}
    userPersonalityTraits = input('Which adjective(s) fits your personlaity the most? Please write them in a decreasing order of importance.\n 1) Kind\n 2) Confident\n 3) Intelligent\n 4) Brave\n 5) Funny\n')
    surveyQ7 = {'PersonalityTraits': userPersonalityTraits.split(' ')}
    userReligionImportance = input('Is it important that your partner shares your religious viewpoints?\n Please press Y if you do or N if you do not. ')
    userReligionImportance.lower()
    surveyQ8 = {'ReligionImportance':userReligionImportance}
    userReligion = input('Are you religious?\n 1) Atheist\n 2) Christian\n 3) Muslim\n 4) Hindus\n 5) Satanist\n')
    surveyQ9 = {'Religion': userReligion}
    userFreeTime= input('Would you prefer to spend your free time indoors or outdoors?\n Please press 1 if indoors or 2 if outdoors. ')
    surveyQ10 = {'InOutDoors': userFreeTime}
    userOpinionAboutKids = input('Do you have or want to have kids?\n Please press Y if you do or N if you do not. ')
    surveyQ11 = {'WantKids':userOpinionAboutKids.lower()}
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
  
  def listToString(self, l):
    s = ""
    for x in l:
      s = s + x + ','
    s = s[:-1]
    return s
  def userToString(self):
    userString = self.getUsername() + " " + self.getPassword() + " " + self.getFirstName() + " " + self.getLastName() + " " + str(self.getBirthday()) + " " + self.getGender() + " " + self.listToString(self.getRomanticPreference()) + " " + self.getMaritalStatus() + " "+self.getUserMBTI()+" "+self.getUserOpinionAboutPets()+" "+self.listToString(self.getUserInterest())+" "+str(self.getUserAgeImportance())+" "+self.listToString(self.getUserLoveLanguage())+" "+self.listToString(self.getUserDesiredTraits())+" "+self.listToString(self.getUserPersonalityTraits())+" "+self.getUserReligionImportance()+" "+str(self.getUserReligion())+" "+self.getUserOpinionAboutKids()
    # if len(self.getSurveyAnswers()) > 0:
    #   for x in self.getSurveyAnswers():
    #     if isinstance(self.getSurveyAnswers()[x], list):
    #       userString = userString + " " + self.listToString(self.getSurveyAnswers()[x])
    #     else:
    #       userString = userString + " " + str(self.getSurveyAnswers()[x])
    return userString
  
          
# firstName = input('Your name: ')
# lastName = input('Last name: ') 
# birthday = input('Birthday (yyyy/mm/dd): ')
# surveyDictionary = {}
# martialStatus = 'Single'

# #username and password will be retrieved from the Management System class

# user = User(username, password, firstName, lastName, birthday, surveyDictionary, martialStatus)
