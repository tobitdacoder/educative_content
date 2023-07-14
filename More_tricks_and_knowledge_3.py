""" THIS IS THE CONTINUATION OF THE SECOND FILE ABOUT MORE TRICKS WE ARE LEARNING EVERYDAY IN PYTHON.
REMEMBER THAT, THIS IS A COMPILLATION OF MULTIPLE PROGRAMS. IF YOU WANT TO TRY OUT A SPECIFIC ONE, COPY IT AND PASTE IT IN YOUR ONLINE PYTHON COMPILER OF YOUR CHOICE AND TRY IT OUT !!!!"""

################################################################ 

# DAY 65 CHALLENGE: create a game using Object Oriented Programming


class MyCharacter:
  # 1. we create our variables to be used in our objects
  Name = None # a string 
  Health = None # an integer
  MagicPoints = None # an integer

  def __init__(self, Name, Health, MagicPoints):
    #now we are innitiating the variables for them to be used on our objects
    self.Name = Name 
    self.Health = Health
    self.MagicPoints = MagicPoints

  # 3. we then create a function that will print for us the Information about the character.
  def CharacterInfo(self):
    print(f" This is {self.Name}, He/she has Got %{self.Health} of health level and has {self.MagicPoints} magic points")

# 4. then we now inherit by creating a new class called PlayerClass, and it is going to help us create the Player object or character
class PlayerClass(MyCharacter):
  
  Lives=None # number of lives remaining
             # an integer
  NickName=None # an integer
    
  def __init__(self,Lives,NickName):
    
    self.Lives=Lives
    self.NickName=NickName

  def AmIAlive(self):
    if int(self.Lives) <= 0:
      print("you are dead")
      quit() # this is the same as exit() but is more friendly

# 5. then we create an Enemy class that will help us create Enemies objects or characters 

class EnemyClass(MyCharacter): # inheritance here !!

  Type=None # type of enemy
            # a string
  Strength=None # his strength
            # an integer
  # and all the other characteristic from the principal class

  def __init__(self,Type,Strength):
    
    self.Type=Type
    self.Strength=Strength

  def EnemyDescribe(self):
    print(f"This enemy is called {self.Name}, His/her health is at level {self.Health} and has {self.MagicPoints} Magic points, He/she is of type {self.Type} and has a strength level of {self.Strength}")

# 6. then we create another class that is inheriting from the EnemyClass class. we will add more informations for it:

class Orc(EnemyClass): # inheritance here !!

  Speed=None # has to be an integer.
             # is an integer
  
  #and all the other above characteristic from the principal class and the EnemyClass class.

  def __init__(self,Speed):
    self.Speed=Speed
    #and automatically all the other characteristic from the previous classes

# 7. then we also create a vampire class that is also inheriting all the characteristics from the EnemyClass class, plus its own characteristics

class Vampire(EnemyClass): # inheritance here !!

  Day=None # has to be a boolean
  
  def __init__(self):
    self.Type=Type
    self.Day=Day

# NOW WE CREATE CHARACTERS OBJECTS!!!!!:

# for the player we have to define: Name,Health,MagicPoints,Lives,NickName
PlayerOne=PlayerClass("Gandalf","80","650","6","SwordLord")

# for the orc we have to define: Name,Health,MagicPoints,Type,Strength,speed
OrcOne=Orc("Orkana","65","460","Orc","70","50")
OrcTwo=Orc("Karag","70","550","Orc","68","56")
OrcThree=Orc("Yintana","69","490","Orc","75","56")

# for the vampires we have to define:Name,Health,MagicPoints,Type,Strength,Day

VampireOne=Vampire("Klaus","76","800","Vampire","84",True)
VampireTwo=Vampire("Stephan","72","751","Vampire","79",True)
