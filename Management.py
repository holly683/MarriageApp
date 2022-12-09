from User import *

class ManagementSystem:
  def __init__(self,userList):
    self.__userList = userList
    
  
  def getTraitCompatibilityPercentage(user1,user2):
    pT1 = 0
    for x in user1.getTraitsWanted():
      if x in user2.getTraits():
        pT1 = pT1 + 1
    pT1 = pT1/len(utW)
    pT2 = 0 
    for x in user2.getTraitsWanted():
      if x in user1.getTraits():
        pT2 = pT2 + 1
    pT2 = pT2/len(otW)
    return (pT1 + pT2)*50
  def compareLists(l1,l2):
    longer = max(l1,l2)
    shorter = min(l1,l2)
    pt = 0
    for x in longer:
      if x in shorter:
        pt = pt + 1
    return pt/((len(l1)+len(l2))/2)*100
    
  def selectionSortBestMatches(l):
    for i in range(len(l)):
      max = l[i]
      maxI = i
      for j in range(i,len(l)):
        if l[j][0] > max[0]:
          max = l[j]
          maxI = j
      l[maxI] = l[i]
      l[i] = max
    return l
    
  def findMBTICompatibility(self,user1,user2):
    #returns the compatibility percentage (from 0-100) between two mbti types
    #this can then be used with other compatibility percentages to calculate an overall average compatibility
    return int(self.getMBTIChart()[self.getMBTIListIndex(user1.getMBTI())][self.getMBTIListIndex(user2.getMBTI())])
    
  def getMatches(self,mainUser):
    filteredUserL = list(filter(lambda x: (x.getGender() in mainUser.getRomanticPreference() and mainUser.getGender() in x.getRomanticPreference()), self.getUserList()))
    possibleMatches = list(filter(lambda x: (x.getUsername()!=mainUser.getUsername()),filteredUserL))
    bestMatches = []
    for match in possibleMatches:
      percentages = []
      percentages.append(getMbtiCompatibilityPercentage(mainUser, match))
      percentages.append(getTraitCompatibilityPercentage(mainUser, match))
      percentages.append(compareLists(mainUser.getHobbies(),match.getHobbies()))
      percentages.append(compareLists(mainUser.getLoveLanguages(),match.getLoveLanguages()))
      overallPercentages = sum(percentages)/len(percentages)
      bestMatches.append((overallPercentages,match))
    bestMatches = self.selectionSortBestMatches(bestMatches)
    print('Best matches for '+mainUser.getUsername()+':')
    for match in bestMatches:
      print(match[1].getUsername()+': '+str(round(match[0],2))+'% match')
    
class User(ManagementSystem): 
  def __init__(self, username, password, firstName, lastName, birthday, surveyDictionary, martialStatus, email):
    self.__firstName = firstName
    self.__secondName = lastName
    self.__birthday = birthday
    self.__martialStatus = martialStatus
    self.__surveyDictionary = surveyDictionary
    self.__email = email
    super().__init__(username, password)

  def takeSurvey(self):
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
    userDesiredTraits = input('What personality trait do you appreciate the most?\n 1) Kindness; 2) Confidence; 3) Cleverness; 4) Bravery; 5) Humor: ')
    surveyQ6 = {'desired trait': userDesiredTraits}
    userPersonalityTraits = input('Which adjective fits your personlaity the most?\n 1) Kind; 2) Confident; 3) Clever; 4) Brave; 5) Funny: ') 
    surveyQ7 = {'personality trait': userPersonalityTraits}
    userReligionImportance = input('Is it important that your partner shares your religious viewpoints?\n Please press Y if you do or N if you do not. ')
    surveyQ8 = {'religion':userReligionImportance}
    if userReligionImportance.lower() == 'y':
      userReligion = input('Are you religious?\n 1) Atheist; 2) Christian; 3) Muslim; 4) Buddhist; 5) Satanist: ')
      surveyQ9 = {'religion': userReligion}
      self.__surveyDictionary.update(surveyQ9)
    userFreeTime= input('Would you prefer to spend your free time indoors or outdoors?\n Please press 1 if indoors or 2 if outdoors. ')
    surveyQ10 = {'free time': userFreeTime}
    self.__surveyDictionary.update(surveyQ1)
    self.__surveyDictionary.update(surveyQ2)
    self.__surveyDictionary.update(surveyQ3)
    self.__surveyDictionary.update(surveyQ4)
    self.__surveyDictionary.update(surveyQ5)
    self.__surveyDictionary.update(surveyQ6)
    self.__surveyDictionary.update(surveyQ7)
    self.__surveyDictionary.update(surveyQ8)
    self.__surveyDictionary.update(surveyQ10)

    return self.__surveyDictionary
  