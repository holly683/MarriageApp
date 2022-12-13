from User import *
from Database import *
from MultiFactorAuth import *
        
# print('hello')

database = Database()
root = MultiFactorAuth()

# for x in database.getUserList():
#   print(x.getUsername())

root.mainloop()


