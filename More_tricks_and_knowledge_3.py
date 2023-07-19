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

################################################################

