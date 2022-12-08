from replit import db
from User import *

class ManagementSystem():
  def __init__(self,userList):
    self.__userList = userList
    self.__mbtiList = ['INFP','ENFP','INFJ','ENFJ','INTJ','ENTJ','INTP','ENTP','ISFP','ESFP','ISTP','ESTP','ISFJ','ESFJ','ISTJ','ESTJ']
    self.__mbtiChart = []
    f = open("mbtiChart.txt",'r')
    for line in f:
      self.__mbtiChart.append(line.split())
    f.close()
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
  def getMBTIListIndex(self,mbti):
    return self.__mbtiList.index(mbti)
  def getUserList(self):
    return self.__userList
  def getMBTIChart(self):
    return self.__mbtiChart
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
    
    
    
  
    
  