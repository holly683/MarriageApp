import db
from User import *

class ManagementSystem():
  def __init__(self):
    self.__mbtiList = ['INFP','ENFP','INFJ','ENFJ','INTJ','ENTJ','INTP','ENTP','ISFP','ESFP','ISTP','ESTP','ISFJ','ESFJ','ISTJ','ESTJ']
    self.__mbtiChart = []
    f = open("mbtiChart.txt",'r')
    for line in f:
      self.__mbtiChart.append(line.split())
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
  def getMBTIChart(self):
    return self.__mbtiChart
  def findMBTICompatibility(self,mbti1,mbti2):
    #returns the compatibility percentage (from 0-100) between two mbti types
    #this can then be used with other compatibility percentages to calculate an overall average compatibility
    return int(self.getMBTIChart()[self.getMBTIListIndex(mbti1)][self.getMBTIListIndex(mbti2)])
    
    
    
  
    
  