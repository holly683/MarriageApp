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
    return self.__surveyDictionary['MBTI']
  def getUserOpinionAboutPets(self):
    return self.__surveyDictionary['WantPet']
  def getUserInterest(self):
    return self.__surveyDictionary['Interests']
  def getUserAgeImportance(self):
    return self.__surveyDictionary['AgeRange']
  def getUserLoveLanguage(self):
    return self.__surveyDictionary['LoveLanguage']
  def getUserDesiredTraits(self):
    return self.__surveyDictionary['DesiredTraits']
  def getUserPersonalityTraits(self):
    return self.__surveyDictionary['PersonalityTraits']
  def getReligionImportance(self):
    return 
  def getUserReligion(self):
    return self.__surveyDictionary['Religion']
  def getUserOpinionAboutKids(self):
    return self.__surveyDictionary['WantKids']
  def initializeSurvey(self,interests,traits,traitsWanted,mbti,loveLanguages,ageRange,pet,religionImportance,religion,kids,inOutDoors):
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
    self.__surveyDictionary['InOutDoors']=inOutDoors
  def takeSurvey(self):
    print('You will now take the survey. Please answer these questions to the best of your ability.')
    
    userMBTI = input('What is your Myers-Briggs personality type? ')
    userMBTI.lower()
    surveyQ1 = {'MBTI':userMBTI}
    userOpinionAboutPets = input('Do you own or want to own pets?\n Please press Y if you do or N if you do not. ')
    userOpinionAboutPets.lower()
    surveyQ2 = {'WantPet':userOpinionAboutPets}
    userInterest = input('Which topics are you the most interested in?\n 1) Politics\n 2) Music\n 3) Sports\n 4) Art\n 5) Science\n')
    userInterest.lower()
    userInterest.split(' ')
    surveyQ3 = {'Interests': userInterest}
    userAgeImportance = input('What age difference do you find acceptable? ')
    surveyQ4 = {'AgeRange': int(userAgeImportance)}
    userLoveLanguage = input('What is your Love Language(s)? Please write them in a decreasing order of importance.\n 1) Quality time\n 2) Acts of service\n 3) Gift-giving\n 4) Words of Affirmation\n 5) Physical Touch\n')
    userLoveLanguage.lower()
    userLoveLanguage.split(' ')
    surveyQ5 = {'LoveLanguage': userLoveLanguage}
    userDesiredTraits = input('What personality trait(s) do you appreciate the most?\n 1) Kindness\n 2) Confidence\n 3) Intelligence\n 4) Bravery\n 5) Humor\n')
    userDesiredTraits.lower()
    userDesiredTraits.split(' ')
    surveyQ6 = {'DesiredTraits': userDesiredTraits}
    userPersonalityTraits = input('Which adjective(s) fits your personlaity the most? Please write them in a decreasing order of importance.\n 1) Kind\n 2) Confident\n 3) Intelligent\n 4) Brave\n 5) Funny\n') 
    userPersonalityTraits.lower()
    userPersonalityTraits.split(' ')
    surveyQ7 = {'PersonalityTraits': userPersonalityTraits}
    userReligionImportance = input('Is it important that your partner shares your religious viewpoints?\n Please press Y if you do or N if you do not. ')
    userReligionImportance.lower()
    surveyQ8 = {'ReligionImportance':userReligionImportance}
    userReligion = input('Are you religious?\n 1) Atheist\n 2) Christian\n 3) Muslim\n 4) Hindus\n 5) Satanist\n')
    surveyQ9 = {'Religion': userReligion}
    userFreeTime= input('Would you prefer to spend your free time indoors or outdoors?\n Please press 1 if indoors or 2 if outdoors. ')
    surveyQ10 = {'InOutDoors': userFreeTime}
    userOpinionAboutKids = input('Do you have or want to have kids?\n Please press Y if you do or N if you do not. ')
    userOpinionAboutKids.lower()
    surveyQ11 = {'WantKids':userOpinionAboutKids}
    self.__surveyDictionary['MBTI'] = surveyQ1
    self.__surveyDictionary['WantPet'] = surveyQ2
    self.__surveyDictionary['Interests'] = surveyQ3
    self.__surveyDictionary['AgeRange'] = surveyQ4
    self.__surveyDictionary['LoveLanguage'] = surveyQ5
    self.__surveyDictionary['DesiredTraits']=surveyQ6
    self.__surveyDictionary['PersonalityTraits']=surveyQ7
    self.__surveyDictionary['ReligionImportance'] = surveyQ8
    self.__surveyDictionary['Religion'] = surveyQ9
    self.__surveyDictionary['WantKids'] = surveyQ11
    self.__surveyDictionary['InOutDoors']=surveyQ10
    return self.__surveyDictionary
  
  def listToString(self, l):
    s = ""
    for x in l:
      s = s + x + ','
    s = s[:-1]
    return s
  def userToString(self):
    userString = self.getUsername() + " " + self.getPassword(
  ) + " " + self.getFirstName() + " " + self.getLastName(
  ) + " " + self.getBirthday() + " " + self.getGender(
  ) + " " + self.listToString(
    self.getRomanticPreference()) + " " + self.getMaritalStatus()
    if len(self.getSurveyAnswers()) > 0:
      for x in self.getSurveyAnswers():
        if isinstance(self.getSurveyAnswers()[x], list):
          userString = userString + " " + self.listToString(self.getSurveyAnswers()[x])
        else:
          userString = userString + " " + str(self.getSurveyAnswers()[x])
    print(userString)
    return userString
  
          
# firstName = input('Your name: ')
# lastName = input('Last name: ') 
# birthday = input('Birthday (yyyy/mm/dd): ')
# surveyDictionary = {}
# martialStatus = 'Single'

# #username and password will be retrieved from the Management System class

# user = User(username, password, firstName, lastName, birthday, surveyDictionary, martialStatus)
