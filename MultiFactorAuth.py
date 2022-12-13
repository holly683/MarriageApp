import tkinter as tk
import tkinter.messagebox as mb
# import multifactorgui as mfg
# from Database import *
# from User import *

from User import *
from Database import *
from ManagementSystem import *



class MultiFactorAuth(tk.Tk):
    username =""
    password = ""
    
    def __init__(self):
      ''''''
      tk.Tk.__init__(self)
      
      self.frame_main = tk.Frame(self)
      self.title("Home Page")
      self.frame_main.grid(row=0, column=0, sticky="news")

      self.btn_login = tk.Button(self.frame_main, text="RETURNING USER", command=self.login)
      self.btn_login.pack(padx=175, pady=15)

      self.btn_register = tk.Button(self.frame_main, text="NEW USER",command=self.register)
      self.btn_register.pack(padx=175, pady=20)


      


      self.frame_main.tkraise()
      self.database = Database()
      self.ms = ManagementSystem()
  
      
    def getDatabase(self):
      return self.database
      
    def getMS(self):
      return self.ms
    def login(self):
        self.frame_login = tk.Frame(self)
        self.title("Authorize")
        self.frame_login.grid(row=0, column =0, sticky="news")

        self.lbl_username = tk.Label(self.frame_login, text="Username")
        self.lbl_username.pack(pady=5)
        self.ent_username = tk.Entry(self.frame_login, bd=3)
        self.ent_username.pack(pady=7)

        self.lbl_password = tk.Label(self.frame_login, text="Password")
        self.lbl_password.pack(pady=10)
        self.ent_password = tk.Entry(self.frame_login, show="*", bd=3)
        self.ent_password.pack(pady=13)

        self.btn_login = tk.Button(self.frame_login, text="LOGIN", command=self.authorize)
        self.btn_login.pack(padx=175, pady=17)

        # self.btn_change = tk.Button(self.frame_login, text="FORGOT PASSWORD", command=self.forgotPass)
        # self.btn_change.pack(padx=175, pady=20)

        self.frame_login.tkraise()



    def authorize(self):
      entry_username = self.ent_username.get()
      entry_password = self.ent_password.get()
      database = self.getDatabase()

      # if(entry_username == Database.findUserByUsername(entry_username)) and entry_password == Database.findPassByUser(entry_password)):
      if(entry_username == database.findUserByUsername(entry_username).getUsername() and entry_password == database.findPassByUser(entry_username)):
        
        #create authorization frame and widgets
        # tk.Tk.authorize(self)

        self.frame_auth = tk.Frame(self, bg="plum4")
        self.title("Authenticate")
        self.frame_auth.grid(row=0,column=0, sticky="news")

        lbl_msg =tk.Label(self.frame_auth,text="Congratulations!\nYou have been authorized!", bg="sienna2")
        lbl_msg.pack(pady=15)

        lbl_profile = tk.Label(self.frame_auth, text="View your match: ", bg="sienna2")
        lbl_msg.pack(pady=25)

        ms = self.getMS()
        self.btn_match = tk.Button(self.frame_auth, text="Find Your Match!", command=ms.getMatches(database.findUserByUsername(entry_username)))
        self.btn_match.pack(padx=175,pady=30)
        
        # self.btn_profile = tk.Button(self.frame_auth, text="PROFILE", command=self.F)
        # self.btn_profile.pack(padx=175,pady=30)

        self.frame_auth.tkraise()
      else:
        mb.showinfo('Authentication', "We're sorry, but our records do not match your entry.")
  

    def register(self):
      # tk.Tk.register(self)

      self.frame_register = tk.Frame(self)
      self.title("Register")
      self.frame_register.grid(row=0, column=0, sticky="news")


      # self.lbl_firstName = tk.Label(self.frame_register, text="First Name: ")
      # self.lbl_firstName.pack(padx=150,pady=3)
      # self.ent_firstName = tk.Entry(self.frame_register, bd=3)
      # self.ent_firstName.pack(padx=175,pady=3)
      
      # self.lbl_lastName = tk.Label(self.frame_register, text="Last Name: ")
      # self.lbl_lastName.pack(padx=150,pady=7)
      # self.ent_lastName = tk.Label(self.frame_register, bd=3)
      # self.ent_lastName.pack(padx=175,pady=7)
      

      self.lbl_username = tk.Label(self.frame_register,text="Username")
      self.lbl_username.pack(pady=9)
      self.ent_username = tk.Entry(self.frame_register, bd=3)
      self.ent_username.pack(pady=11)

      self.lbl_passwd = tk.Label(self.frame_register,text="Password")
      self.lbl_passwd.pack(pady=15)
      self.ent_password = tk.Entry(self.frame_register, show="*", bd=3)
      self.ent_password.pack(pady=18)

      self.lbl_passwdchk = tk.Label(self.frame_register, text="Confirm Password")
      self.lbl_passwdchk.pack(pady=23)
      self.ent_passwdchk = tk.Entry(self.frame_register, show="*", bd=3)
      self.ent_passwdchk.pack(pady=25)

      # if(ent_passwdchk == ent_password):
      self.btn_register = tk.Button(self.frame_register, text="REGISTER",command=self.newUser)
      self.btn_register.pack(padx=175, pady=40)

      self.frame_register.tkraise()

    def newUser(self):
      ent_username = self.ent_username.get()
      ent_passwdOne = self.ent_password.get()
      ent_passwdchkOne = self.ent_passwdchk.get()
      database = self.getDatabase()

      

  
      if(ent_username == database.findUserByUsername(ent_username)):
        mb.showinfo("Authentication",'Username already taken!\nTry Again')
        self.register()
      
      elif(ent_passwdOne == ent_passwdchkOne):
        newUser1 = self.makeUser(ent_username,ent_passwdOne)
        
        self.frame_newUser = tk.Frame(self, bg="sienna2")
        self.title("Welcome New User!")
        self.frame_newUser.grid(row=0,column=0,sticky="news")

        # database.updateDatabase(newUser1)
        # database.updateUserList(newUser1)
        self.lbl_new = tk.Label(self.frame_newUser, text="Take the entry quiz to find your perfect match!", bg="sienna2")
        self.lbl_new.pack(pady=15)
        command=self.quiz(newUser1)
        
        ms = self.getMS()
        self.btn_quiz = tk.Button(self.frame_newUser, text="Find Your Match!", command=ms.getMatches(database.findUserByUsername(ent_username)))
        self.btn_quiz.pack(pady=30)

        self.frame_newUser.tkraise()
      else:
        mb.showinfo("Authentication", "Your Passwords Don't Match\nTry Again")
        self.register()
      
    # def profile(self):
    #   ent_username = self.ent_username.get()
      
    #   self.frame_profile = tk.Frame(self)
    #   self.title(ent_username + " Profile:")
    #   self.frame_profile.grid(row=0, column=0, sticky="news")

    #   self.lbl_username1 = tk.Label(self.frame_profile, text = "Username: " + user.getUsername())
    #   self.lbl_username1.pack(pady=3)

    #   self.lbl_password1 = tk.Label(self.frame_profile, text="Password: " + user.getPassword())
    #   self.lbl_password1.pack(pady=5)

    #   self.lbl_firstName = tk.Label(self.frame_profile, text = "First Name: "+ user.getFirstName())
    #   self.lbl_firstName.pack(pady=7)
      

    #   # self.lbl_lastName = tk.Label(self.frame_profile, text="Last Name: "+User.getLastName())
    #   # self.lbl_lastName.pack(pady=10)
    #   self.lbl_lastName = tk.Label(self.frame_profile, text="Last Name:"+user.getLastName())
    #   self.lbl_lastName.pack(pady=10)
      

    #   self.lbl_Birthday = tk.Label(self.frame_profile, text="Birthday: "+ user.getBirthday())
    #   self.lbl_birthday.pack(pady=13)

    #   self.lbl_gender = tk.Label(self.frame_profile, text="Gender: "+user.getGender())
    #   self.lbl_gender.pack(pady=15)

    #   self.lbl_romanticPreference = tk.Label(self.frame_profile, text="Romantic Preferences: "+user.getRomanticPreference())
    #   self.lbl_romanticPreference.pack(pady=17)

    #   self.lbl_maritalStatus = tk.Label(self.frame_profile, text="Marrital Status: "+user.getMaritalStatus())
    #   self.lbl_maritalStatus.pack(pady=20)

    #   self.lbl_surveyAnswers = tk.Label(self.frame_profile, text="Survey Answers: "+user.getSurveyAnswers())
    #   self.lbl_surveyAnswers.pack(pady=23)

    #   # sel

      
      
      
      

  
    def quiz(self,user):
      database = self.getDatabase()

      # self.frame_quiz = tk.Frame(self) 
      self.title("Find Your Match Quiz:")
      # self.frame_quiz(row=0, column=0, sticky="news")

      user.takeSurvey()
      database.updateDatabase(user)
      database.updateUserList(user)
      self.user = user

      
      # User.takeSurvey()
      # mb.showinfo(text = User.takeSurvey())
      
    # def forgotPass(self):
    #   self.frame_forgotPass = tk.Frame(self, bg="plum4")
    #   self.title("Forgot Password")
    #   self.frame_forgotPass(row=0, column=0, sticky="news")

    def askForFirstName(self):
      name = input('What is your first name? ')
      return name
    def askForLastName(self):
      name = input('What is your last name? ')
      return name
    def askForBirthday(self):
      ans = input('What is your birthday? Please enter in YYYY/MM/DD format. ')
      return ans
    def askForGender(self):
      ans = input('What is your gender? ')
      return ans
    def askForRomanticPreference(self):
      ans = input('What genders are you interested in romantically? Please enter each seperated by spaces. ')
      return ans.split()

    
    
    def makeUser(self,username,password):
      database = self.getDatabase()
      fName = self.askForFirstName()
      lName = self.askForLastName()
      bDay = self.askForBirthday()
      g = self.askForGender()
      rP = self.askForRomanticPreference()
      u = User(username, password, fName,lName,bDay,g,rP,{},'unmarried')
      return u





# makeUser('Jane123','password123')

      
      

root = MultiFactorAuth()

# root.makeUser('Jane123','password123')

root.mainloop()







