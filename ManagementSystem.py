from User import *
from Database import *
import math

class ManagementSystem:
  def __init__(self):
    self.__database = Database()
  def selectionSortBestMatches(self,l):
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
  def getDatabase(self):
    return self.__database
  def getMbtiCompatibilityPercentage(user1, user2):
    data = self.getDatabase()
    mbtiList = data.getMBTIList()
    mbtiChart = data.getMBTIChart()
    return float(mbtiChart[mbtiList.index(user1.getMBTI())][mbtiList.index(
      user1.getMBTI())])
    
  def compareLists(l1, l2):
    pts1 = 0
    possiblePts1 = math.factorial(len(l1))
    for i in range(len(l1)):
      if l1[i] in l2:
        pts1 = pts1 + len(l1) - i
    pts2 = 0
    possiblePts2 = math.factorial(len(l2))
    for i in range(len(l2)):
      if l2[i] in l1:
        pts2 = pts2 + len(l2) - i
    return ((pts1 + pts2) / (possiblePts1 + possiblePts2)) * 100

  
  def getTraitCompatibilityPercentage(user1, user2):
    pts1 = 0
    possiblePts1 = math.factorial(len(user1.getTraitsWanted()))
    for i in range(len(user1.getTraitsWanted())):
      if i in user2.getTraits():
        pts1 = pts1 + len(user1.getTraitsWanted()) - i
    pts2 = 0
    possiblePts2 = math.factorial(len(user2.getTraitsWanted()))
    for i in range(len(user2.getTraitsWanted())):
      if i in user1.getTraits():
        pts2 = pts2 + len(user2.getTraitsWanted()) - i
    return ((pts1 + pts2) / (possiblePts1 + possiblePts2)) * 100
    
  def getMatches(self,mainUser):
    userL = self.getDatabase().getUserList()
    possibleMatches = list(filter(lambda x: (x.getGender() in mainUser.getRomanticPreference() and mainUser.getGender() in x.getRomanticPreference()), userL))
    possibleMatches = list(filter(lambda x: (x.getUsername()!=mainUser.getUsername()),possibleMatches))
    #possibleMatches = list(filter(lambda x: (x.getUserOpinionAboutKids()==mainUser.getUserOpinionAboutKids() and x.getUserOpinionAboutPets()==mainUser.getUserOpinionAboutPets()),possibleMatches))
    #possibleMatches = list(filter(lambda x: (x.getAge()<mainUser.getAge()+mainUser.getUserAgeImportance() and x.getAge()>mainUser.getAge()-mainUser.getUserAgeImportance()),possibleMatches))
    if mainUser.getReligionImportance():
      possibleMatches = list(filter(lambda x: (x.getUserReligion()==mainUser.getUserReligion()),possibleMatches))
    else:
      possibleMatches = list(filter(lambda x: (x.getUserReligion()==mainUser.getUserReligion() or x.getReligionImportance()==False),possibleMatches))
    
    #get percentage from remaining possible matches
    bestMatches = []
    for match in possibleMatches:
      percentages = []
      percentages.append(self.getMbtiCompatibilityPercentage(mainUser, match))
      percentages.append(self.getTraitCompatibilityPercentage(mainUser, match))
      percentages.append(self.compareLists(mainUser.getInterests(),match.getInterests()))
      percentages.append(self.compareLists(mainUser.getLoveLanguages(),match.getLoveLanguages()))
      overallPercentages = sum(percentages)/len(percentages)
      bestMatches.append((overallPercentages,match))
    bestMatches = self.selectionSortBestMatches(bestMatches)
    print('Best matches for '+mainUser.getUsername()+':')
    for match in bestMatches:
      print(match[1].getUsername()+': '+str(round(match[0],2))+'% match')
    


