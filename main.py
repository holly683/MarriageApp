from User import *
from Database import *
        
# print('hello')

database = Database()

for x in database.getUserList():
  print(x.getUsername())
