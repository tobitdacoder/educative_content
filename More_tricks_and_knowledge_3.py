""" THIS IS THE CONTINUATION OF THE SECOND FILE ABOUT MORE TRICKS WE ARE LEARNING EVERYDAY IN PYTHON.
REMEMBER THAT, THIS IS A COMPILLATION OF MULTIPLE PROGRAMS. IF YOU WANT TO TRY OUT A SPECIFIC ONE, COPY IT AND PASTE IT IN YOUR ONLINE PYTHON COMPILER OF YOUR CHOICE AND TRY IT OUT !!!!"""

################################################################ 

# DAY 65 CHALLENGE: create a game using Object Oriented Programming


class MyCharacter:
  Name = None  # a string
  Health = None  # an integer
  MagicPoints = None  # an integer

  def __init__(self, Name, Health, MagicPoints):
    self.Name = Name
    self.Health = Health
    self.MagicPoints = MagicPoints

  def CharacterInfo(self):
    print(f"This is {self.Name}, He/she has {self.Health}% of health level and has {self.MagicPoints} magic points")


class PlayerClass(MyCharacter):
  Lives = None  # number of lives remaining (an integer)
  NickName = None  # a string

  def __init__(self, Name, Lives, NickName):
    #super().__init__(Name, 100, 100)  # Initialize the inherited attributes
    self.Name=Name
    self.Health=100
    self.MagicPoints=100
    self.Lives = Lives
    self.NickName = NickName

  def PlayerResume(self):
    print(f"He/she is called {self.Name}, His/her nickname is {self.NickName} and I still have {self.Lives} lives remaining and has the health percentage of {self.Health}")

  def AmIAlive(self):
    if int(self.Lives) <= 0:
      print("You are dead")
      quit()  # this is the same as exit() but is more friendly
    else:
      print(f"\nYou are still alive and you have {self.Lives} lives remaining")


class EnemyClass(MyCharacter):
  Type = None  # type of enemy (a string)
  Strength = None  # his strength (an integer)

  def __init__(self, Name, Type, Strength):
    #super().__init__(Name, 100, 100)  # Initialize the inherited attributes
    self.Name=Name
    self.Health=100
    self.MagicPoints=100
    self.Type = Type
    self.Strength = Strength

  def EnemyDescribe(self):
    print(f"This enemy is called {self.Name}, His/her health is at level {self.Health} and has {self.MagicPoints} Magic points. He/she is of type {self.Type} and has a strength level of {self.Strength}")


class Orc(EnemyClass):
  Speed = None  # has to be an integer

  def __init__(self, Name, Speed):
    #super().__init__(Name, "Orc", 100)  # Initialize the inherited attributes
    self.Name=Name
    self.Type="Orc"
    self.Strength=100
    self.Speed = Speed

  def OrcResume(self):
    print(f"\nI present you {self.Name} the {self.Type}. He has a speed of {self.Speed} and a level of {self.Strength} in strength")


class Vampire(EnemyClass):
  Day = None  # has to be a boolean

  def __init__(self, Name, Day):
    #super().__init__(Name, Type, 100)  # Initialize the inherited attributes
    self.Name=Name
    self.Type="Vampire"
    self.Strength=100
    self.Day = Day

  def VampireResume(self):
    if self.Day:
      print(f"\n{self.Name} is a {self.Type} and since it is day, he is weak. His power is no longer {self.Strength}, but {int(self.Strength)-20}")
    else:
      print(f"\n{self.Name} is a {self.Type} and since it is night, he is stronger. His power is no longer {self.Strength}, but {int(self.Strength)+20}")


# Create player object
PlayerOne = PlayerClass("Zenda", 6, "SwordLord")

PlayerOne.Health=90
PlayerOne.MagicPoints=95

print(PlayerOne.Health)
PlayerOne.PlayerResume()

# Create orc objects
OrcOne = Orc("Orkana", 50)
print(OrcOne.Type)

# Create vampire objects
VampireOne = Vampire("Klaus", True)
VampireTwo = Vampire("Stephan", True)
print(VampireTwo.Type)

# Access object attributes and methods
print(VampireOne.Type)
VampireOne.VampireResume()

################################################################

# JUST A SMALL TRICK TO GET SECRET INPUT FROM USERS AND USE THEM IN OUR PROGRAM
#      EITHER NUMBERS OR STRINGS.
import getpass

task1=int(getpass.getpass("first strenght: "))
task2=int(getpass.getpass("second strenght: "))
print(task1*task2)

#THIS CODE BELLOW JUST GENERATE A RANDOM PASSWORD THAT WILL BE USED ONLY ONCE:
import random 

password=""
listt=["#","!","$","*","|","\\","(",")",'1','2','3','4','5','6','7','8','9']

for i in range(len(listt)+4):
  letter=random.choice(listt)
  password+=(letter)
print(password)

################################################################

#DAY 70: SECRET (Password from the system os)

import os # we are using the os in order to gt the password saved inside the operating system (os);

true_password=os.environ['password1'] # then here we take that password from the system and we store it inside the variable "true_password"; This is basically asking to the system for the password that was stored in it, When you fork a repl, this password will not go with it, they are yours.

while True:
  print()
  user_pass=input("password> ")
  # then get the input from the user, and we will authentify it by comparing it to the true_password that came from the system. 
  
  if user_pass==true_password:
    print("welcom to the adventure my GEEE!!!")
    break
  else:
    print("try latter my brother")
    continue
  
#DAY 70 CHALLENGE:

import os

userList=["luna"]
adminUserList=["toby"]

true_userPass=os.environ['userPass'] 
true_adminPass=os.environ['adminPass']
# these words inside [] are the keys that are soring the password as a value, and in order to access them, we need to use the key name and the os library: os.environ[name of the key storing the value]

while True:
  
  username=input("name > ") # we get the name 
  userpassword=input("pass > ") # we get the password that we are going to compare with the one that we asked for to the system
  
  # now we are just checking the details before to give any access to the program.
  # remember, this is inside the loop, so that we can specify thre trial number etc.
  if username.strip().lower() in userList and userpassword==true_userPass:
    
    print(f"you're welcome {username}, you are our new user")
    
  elif username.strip().lower() in adminUserList and userpassword==true_adminPass:
    print(f"welcome back MR/mrs admin {username}")
    break
  else:
    print("that was wrong, come later")
    
########################################################################

#DAY 71: HASHING PASSWORD 
from replit import db

username='toby' # the one that will be the key in our database
password="tobit1" # here is our naked password that can be easily seen because it is not "hashed"

hashed_password=hash(password)
# here we encrypt the password using the hash function

db[username]=hashed_password # here we are creating a key in the database and store in the hashed_password we've got. 

print(db[username]) # here is how we print the content of the database using the key.
print(hashed_password) # when we print the hashed_password, we will get a suit of numbers that are the encrypted verion of the password we generated.

# here we are basically showing how we can store the hashed_pass in the dstabase and then reuse them for authntification by comparing them to the hashed_version of the user password.
ask=input("pass> ")
hashed_ask=hash(ask)


if hashed_ask==db[username]:
  print('yeeeess')
else:
  print("Noooooo")
