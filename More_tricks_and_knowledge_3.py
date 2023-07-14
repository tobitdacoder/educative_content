""" THIS IS THE CONTINUATION OF THE SECOND FILE ABOUT MORE TRICKS WE ARE LEARNING EVERYDAY IN PYTHON.
REMEMBER THAT, THIS IS A COMPILLATION OF MULTIPLE PROGRAMS. IF YOU WANT TO TRY OUT A SPECIFIC ONE, COPY IT AND PASTE IT IN YOUR ONLINE PYTHON COMPILER OF YOUR CHOICE AND TRY IT OUT !!!!"""

################################################################ 

# DAY 65 CHALLENGE: create a game using Object Oriented Programming


class MyCharacter:
  # 1. we create our variables to be used in our objects
  Name = None
  Health = None
  MagicPoints = None

  def __init__(self, Name, Health, MagicPoints):
    # 2. now we are innitiating the variables for them to be used on our objects
    self.Name = Name
    self.Health = Health
    self.MagicPoints = MagicPoints
    
  # 3. we then create a function that will print for us the Information about the character.
  def CharacterInfo(self):
    print(f" This is {self.Name}, He/she has Got %{self.Health} of health level and has {self.MagicPoints} magic points")
    
# 4. then we now inherit by creating a new class called PlayerClass, and it is going to help us create the Player object or character.
class PlayerClass(MyCharacter):

  def __init__(self,Lives):
    
    self.Lives=Lives

  def AmIAlive(self):
    if int(self.Lives) <= 0:
      print("you are dead")
      quit() # this is the same as exit() but is more friendly
