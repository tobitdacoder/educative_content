""" THIS IS THE CONTINUATION OF THE SECOND FILE ABOUT MORE TRICKS WE ARE LEARNING EVERYDAY IN PYTHON.
REMEMBER THAT, THIS IS A COMPILLATION OF MULTIPLE PROGRAMS. IF YOU WANT TO TRY OUT A SPECIFIC ONE, COPY IT AND PASTE IT IN YOUR ONLINE PYTHON COMPILER OF YOUR CHOICE AND TRY IT OUT !!!!"""

################################################################ 

# DAY 65 CHALLENGE: create a game using Object Oriented Programming. Classes and Objects.
# today we will see how to create a simple game avatar using classes and objects.

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


class PlayerClass(MyCharacter): # here is where inheritence is happening (we inherit from the class <yCharacter).
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
VampireTwo = Vampire("GiGi", True)
print(VampireTwo.Type)

# Access object attributes and methods
print(VampireOne.Type)
VampireOne.VampireResume()

################################################################

# JUST A SMALL TRICK TO GET SECRET INPUT FROM USERS AND USE THEM IN OUR PROGRAM
#      EITHER NUMBERS OR STRINGS.
from getpass import getpass as input

task1=int(input("first strenght: "))
task2=int(input("second strenght: "))
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



# ANOTHER EXAMPLE OF HOW WE ARE USING THE hash() FUNCTION ALONG WITH THE DATABASE STORING METHOD to store the password and the salt that we add to the password to make it even tricky for the hacker to hack. 

from replit import db

password='tobit1'
salt=1433954

salted_pass=password+str(salt)
hashed_salted_pass=hash(salted_pass)

db["tobit"]={"password":hashed_salted_pass,"Salt": salt}
#print(db["tobit"]["password"])

ask=input("password > ")
ask_salt=db["tobit"]["Salt"]

trial_Password=ask+str(ask_salt)
hashed_trial_password=hash(trial_Password)

if hashed_trial_password==db['tobit']['password']:
  print("yeahh")

else: 
  print("nooooo")
  
# DAY 71 CHALLENGE: BUILD A SIMPLE LOGIN SYSTEM USING hash() function and probably os.environ[key] keyword

from replit import db
import os, time
import random

NumberList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
Existing = []

while True:

  print()
  print("1. New User")
  print("2. Log-in")
  print()

  choice = input("> ")

  if choice == '1': # SIGN-UP CASE
    New_username = input("new username > ")
    New_password = input("new password > ")
    Salt = ''

    for i in range(5):
      num = str(random.choice(NumberList))
      Salt += num

    New_strong_password = New_password + Salt
    Hashed_New_strong_password = hash(New_strong_password)
    
    db[New_username] = {
      "hashed_pass": Hashed_New_strong_password,
      "username": New_username,"salt":Salt
    }

    print(
      f"thank you, your hashed password in the database is {db[New_username]}")

    time.sleep(3)
    os.system("clear")
    continue

    if New_username not in Existing:
      Existing.append(New_username)
    else:
      pass

  elif choice == '2': # LOG-IN CASE
    print()
    Username = input("your username > ")
    Password = input("your password please > ")
    Strong_hashed_pass=hash(Password + db[Username]['salt'])

    if Username == db[Username]['username'] and Strong_hashed_pass == db[Username]["hashed_pass"]:
      print()
      print("you belong here")
      time.sleep(3)
      
    else:
      print()
      print("you are nooooooot from heeeeeeere")
      print()

  else:
    print()
    print("wrong choice, try again ")
    time.sleep(4)
    os.system("clear")
    continue

#####################################################

# this is a small program that simply get the input of the
# numerator and the denominator from the user and then return a simplified version of it.

from math import gcd

class Fraction:
    
    def __init__(self,Numerator,Denominator):
        
        self.Numerator=Numerator
        self.Denominator=Denominator
        
        
    def GetNumbers(self):
        
        num1=int(input("num1: "))
        while True:
            num2=int(input("num2: "))
            if num2==0:
                print("not valid")
                continue
            break
        self.Numerator=num1
        self.Denominator=num2
        
        
    def Gcd(self):
        
        common=gcd(self.Numerator,self.Denominator)
        newNumer=self.Numerator/common
        newDeno=self.Denominator/common 
        fraction=str(int(newNumer))+"/"+str(int(newDeno))
        return fraction

if __name__=="__main__":
    
    Objectone=Fraction(0,0)
    Objectone.GetNumbers()
    print(Objectone.Gcd())


#####################################################

from replit import db as database

# this small program helps us to verify if the database is empty by checking the number of keys inside the database. 

"""db.clear() : ceci nous aide lorsque on veut efacer tout le contenu du dictionaire si on le veut"""
#db["username"]={"User":"tobit","age":"18"}

if len(database)==0: # this is where we are checking the number of keys inside the database by checking the length of the database (samething as checking the content of a list, by checking its length)
  print("it is empty")
  
else:
  keys=list(database.keys())
  print("there is something in it")
  for key in keys:
    print(f"""{key} : {database[key]}""")
    

################################################################################



StudentDict={}

while True:
   fname=input("First name: ") # first name
   Lname=input("Last name: ") # last name
   course=input("what course: ") # BSCS 2
   courseUnit=input("the course unit: ") #OOP
   reg=input("your registration number: ") # your registration number
   dep=input("the department: ") # COMPUTING & IT
   Faculty=input("which faculty: ") # SCIENCE AND TECHNOLOGY
   Email=input("your email please: ")
   phone=int(input("your phone numbr please "))
   StudentDict={"fname":fname,"Lname":Lname,"course":course,"courseunut":courseUnit,"regNumber":reg,"department":dep,"faculty":Faculty,"Email":Email,"phone":phone}
   print()
   
   print()
   print(f"hey {fname}, here are your details: ")
   print()
   
   for keys,values in StudentDict.items():
      print(f"{keys} :{values}")
   print()
   
   add=input("wanna add another student? ")
   if add.strip()[0]=="y":
       continue
   else:
       break
     
     
#########################################################################


while True:
    try:
        answer = int(input("Give me an integer between 1 and 9 😃: "))
    except Exception as err:
        print(err)
    
    if 1 <= answer <= 9:
        print()
        for i in range(1, answer + 1):
            for j in range(1, i + 1):
                print(i, end=" ")
            print()
        print("\nwe are done 😁")
        print()
    else:
        print()
        print("The value entered is not in the range 1-9 😢😢😢, try again! 😉")
        print()




#########################################################################


# DAY 72: CHALLENGE, UPDATED DIARY PROGRAM

from replit import db
import os,time,random
import datetime

"""db.clear() : THIS WILL BE USED WHEN WE WANT TO ERASE THE DATABASE CONTENT"""

#db["username"]={"User":"tobit","age":"18"}



if len(db)==0:

  print("you're a new user, please, create an acount: ")
  time.sleep(1)
  print()
  
  Numbers=[1,2,3,4,5,6,7,8,9,0]
  New_Username=input("New Username > ")
  New_Password=input("New password > ")
  Salt=''
  
  for i in range(6):
    num=random.choice(Numbers)
    Salt+=str(num)
    
  Salted_password=New_Password+Salt
  hashed_password=hash(Salted_password)
  db[New_Username]={"Username":New_Username,"salt":Salt,"Hashed_password":hashed_password}
  print()
  print("you now have an acount ... CONGRATULATIONS!!!")
  print()

  time.sleep(1)
  
  

  #NOW WE CAN EASILY PROCEED INTO THE DIARY WITH THE NEW PASSWORD ENTERED:

  # first we ask for the personal password (since it is a personal diary, so the password has to be different)

  #password=101299
  # INFORMATIONS TO HELP:
  # !!!!  db.clear()  this will clear all the database content
  
  while True:
    
    try:
      username_check=input("your username please > ")
      password_check=input("also your password please > ")
      
    except:
      pass
      
    Salted_password_check=password_check+db[username_check]["salt"]
    hashed=hash(Salted_password_check)
    
    if hashed==db[username_check]["Hashed_password"] and username_check==db[username_check]["Username"]:
      
      while True:
        #name="tobit bushenyula kabuya"
        print("\nwelcome back mr/mrs")
        print()
        print("1. view your secrets")
        print("2. add new secret\n")
        
        try: # here we are using the try and except in order to avoid any wrong input from the user while asking for his choice
          choice=input("> ")
        except:
          pass
        if choice.strip().lower()[0]=="a": # here is when we choose to add a new text in the diary
          print("\n you can write:")
          text=input("> ")
          
          timestamps=datetime.datetime.now() # here we are now collecting the time now by using the datetime library.
          timestamp_int=int(timestamps.timestamp()) # then here we turn it into an integerfor it to be used later in the printing proccess.
  
          db[str(timestamp_int)]=text # then herewe use the timestamp_int as our new key to store the text that has been entered.
          print("text added!\n")
  
        
        elif choice.strip().lower()[0]=="v":
          
          keys_int=[]
          keys=list(db.keys()) # here we use the list to turn the dictionary db.keys() into a list so that we can easily use its content.
          
          for key in keys: 
            key_int=int(key)
            keys_int.append(key_int)
            
          sorted_keys_int=sorted(keys_int, reverse=True)  #here we are sorting the keys in the list to get them in order. either Ascendent or decendent.
          print()
          for key in sorted_keys_int:
            key_str=str(key)
            print(f"{key_str} : {db[key_str]}")
            print()
          print()
          continue
  
        else:
          print("this choice does not exist")
          continue
          
      
    else:
      print("wrong password or username, try again later")
      time.sleep(1)
      os.system("clear")
      continue
  
else:
  
  while True:

    print()
    print("welcome back")
    print()
    
    try:
      username_check=input("your username please > ")
      password_check=input("also your password please > ")
      
    except:
      pass
      
    Salted_password_check=password_check+db[username_check]["salt"]
    hashed=hash(Salted_password_check)
    
    if hashed==db[username_check]["Hashed_password"] and username_check==db[username_check]["Username"]:
      
      while True:
        #name="tobit bushenyula kabuya"
        print("\nwelcome back mr/mrs")
        print()
        print("1. view your secrets")
        print("2. add new secret\n")
        try:
          choice=input("> ")
        except:
          pass
        if choice.strip().lower()[0]=="a": # here is when we choose to add a new text in the diary
          print("\n you can write:")
          text=input("> ")
          
          timestamps=datetime.datetime.now() # here we are now collecting the time now by using the datetime library.
          timestamp_int=int(timestamps.timestamp()) # then here we turn it into an integer.
  
          db[str(timestamp_int)]=text # then herewe use the timestamp_int as our new key to store the text that has been entered.
          print("text added!\n")
  
        
        elif choice.strip().lower()[0]=="v":
          
          keys_int=[]
          keys=list(db.keys()) # here we use the list to turn the dictionary db.keys() into a list so that we can easily use its content.
          
          for key in keys: 
            key_int=int(key)
            keys_int.append(key_int)
            
          sorted_keys_int=sorted(keys_int, reverse=True) 
          print()
          for key in sorted_keys_int:
            key_str=str(key)
            print(f"{key_str} : {db[key_str]}")
            print()
          print()
          continue
  
        else:
          print("this choice does not exist")
          continue
          
      
    else:
      print("wrong password or username, try again later")
      time.sleep(1)
      os.system("clear")
      continue


#################################################################### 

MaxDays=30


while True:
    print()
    name=input("what is your full name: ")
    Loan=int(input("enter amount of loan: "))
    Days=int(input("Enter days with loan: "))
    
    if Days<=MaxDays:
        interest=Loan*(10/100)
        payment=Loan+interest
        
        
        print()
        print(f"Dear {name.split()[0]} ,after {Days} days, you will pay an amount of {payment}")
        print("thank you!!😁")
    
    else:
        interest=Loan*(10/100)
        
        extraDays=Days-MaxDays
        TotalFine=extraDays*(Loan*(1/100))
        payment=Loan+interest+(TotalFine)
        
        print(f"because of the extra {extraDays} days, you will be charged a fine of {TotalFine} on top of the interest")
        print()
        print(f"So,Dear {name.split()[0]} , after {Days} days, you will pay an amount of {payment} which include the {Loan} of loan , the interest of {interest} plus a fine of {TotalFine}")
        print()
        print("thank you!!😁")


#################################################################### 

    
numberList=[]

count=0
total=0


while True:
    
    try:
        num=input("enter a number: ")
        
        if num.strip().lower()[0]=="d":
            
            for num in numberList:
                total+=num
                
            average=total/count
            print(f"the total is {total}")
            print(f"the count is {count}")
            print(f" and the average is {average}")
            
            print()
            again=input("\n wanna try again ? ")
            
            if again.strip().lower()[0]=="y":
                continue
            else:
                break
        
        else:
            numberList.append(int(num))
            count+=1
    
    except Exception as err:
        print("invalid input")
        #even if the true error is ""invalid literal for int() with base 10: 'r' "
        continue
    
      # here basically, we are telling the program to take the input and verify if 
          # it is not equal to "done" or an integer number. If it is equal to the string "done"
          # then we know what to output, IF it is not "done" and it is an integer, then we also know what to do with it.
          # BUT If it is neither "done" or an integer, then it will be a string by default and it will automatically 
          # being used as an integer and that will generate an error that we capture with the exception.

####################################################################

# this is a small program where we learn how to use "Variable-length argument"
# ... a function where the number of argument or values of the argument can later change without us to modify the function.

def printinfo(arg1,*vartuple):
    print(arg1)
    for var in vartuple:
        print(f"{var}")
    return
printinfo(123,12,65,34,54,34,3)


##### Anonymus functions:

sum=lambda arg1,arg2: arg1+arg2
print("Value Total: ",sum(10,20))

# this kind of function does not need to be defined and we are using "lambda" 


###################################################################

Fname=input("your first name please: ")
Lname=input("your last name please: ")

def Names(NameOne,NameTwo):
    
    return NameOne+" "+NameTwo
print(Names(Fname,Lname))

###################################################################


# HERE WE ARE LEARNING THE BASICS OF MODULE CREATION AND HOW TO REUSE 
# THE FUNCTIONS IN THAT MODULE IN ANOTHER MODULE OR FILE

# THIS IS THE MODULE STORING OUR FUNCTIONS:

def add(Num1,Num2):
    return Num1+Num2

def substract(Num1,Num2):
    return Num1-Num2

def multiply(Num1,Num2):
    return Num1*Num2

def divide(Num1,Num2):
    if Num2==0:
        return("invalid input for division")
    else:
        return Num1/Num2
def Maximum(listTemplate):
   res=max(listTemplate)
   return res
    
# AND HERE IS THE PROGRAM IN WHICH WE REUSED THE FUNCTIONS FROM THE OTHER MODULE:

import docc # THIS IS THE NAME OF THE PYTHON FILE WHERE WE STORED THE FUNCTIONS WE ARE USING

listt=[12,54,72,223,65,45,65,767,32]

numOne=int(input("first number: "))
numTwo=int(input("second number: "))

print(docc.add(numOne,numTwo))
print(docc.Maximum(listt))


#################################################################### 

lisst=[12,32,6545,532,72,35,443,76,45,643]
#this list above is just used to demonstrate how the function is working, but we can use any list or array.

def maxi(ListDemo):
    max=0
    for element in ListDemo:
        if element>max:
            max=element
    return max

# STEPS OF THIS ALGORITHM:

# to use this function, you need to provide any list of numbers(either float or integers) to the function maxi() and print that function like this "print(maxi([name of the list]))"
# example: print(maxi(lisst))   here lisst is the list we are using to find the maximum number in it. 

#################################################################### 

# TASK: python program creting a class called person, containing name, sex and proffesion
#  as states or (attributes) and working study and live as its behavious. 
# Demonstrate with examples the uses of classes and objects.


class person:
    
    Name=None
    Sex=None
    Profession=None
    
    def __init__(self,Name,Sex,Profession):
        
        self.Name=Name
        self.Sex=Sex
        self.Profession=Profession
    
    def behaviours(self):
        
        if self.Profession!=None and self.Profession!="student":
            print(f"{self.Name} is working as a {self.Profession}")
        elif self.Profession!=None and self.Profession=="student":
            course=input("what course: ")
            print(f"{self.Name} is a student and pursuing {course}")
        else:
            print(f"{self.Name} is neither a student or a worker")
    
personOne=person("tobit","Male","Photographer")

print(personOne.Sex)
personOne.behaviours()


####################################################################

# this program is just introducing us in how to allocate multiple ...
# ... to a single variable which is converted initialy into a list with the symbole *

def Average(*varlist): 
    total=0
    validNum=[]
    for num in varlist:
        if 1<=num<=50:
            total+=num
            validNum.append(num)
            
    average=total/len(validNum)
    result=(f"the average of all the number of the list which are valid or between 1-50 is {average}")
    return result
    
print(Average(1,4,2,7,12,82,26,-34,-4,5,73,-3,52))


#################################################################### 

#this is The OOP version of our average function. Basically here we have 
# created a function for every task to be done in order to get the average number. 
# First we collect the valid numbers with the AddNum() function, Then we use the 
# collected values in our second function called CalculateAv(). THEN we initiate 
# our Object so that we can use it to access all the functions of the class. 
# Then at the end we are printing the average by using the name of the object 
# then the name of the calculator function CalculateAv().
class CalculateTheAverage:
    
    
    def __init__(self):
        self.total=0
        self.ValidNum=[]
        self.NonValid=[]

    def AddNumber(self,num):
        self.num=num
        
        if 1<=num<=50:
            self.total+=num
            self.ValidNum.append(num)           
            
    def CalculateAv(self):
        if len(self.ValidNum)==0:
            return "No available number to calculate average with"
        else:
            Average=float(self.total)/len(self.ValidNum)
            return f"the average of those {len(self.ValidNum)} numbers is {Average}"
        


# first we initiate the object so that we can use it to access the functions inside the class
calculator= CalculateTheAverage()

# then we ask for inputs by using the AddNumber() function from the class
for i in range(5):
    num=int(input("give me valid numbers: "))
    calculator.AddNumber(num)

# then at the end we print the result using the CalculateAv() function inside the class
print(calculator.CalculateAv())



####################################################################

# this is the html code of the DAY 73 lesson, we are going to learn how to use flask by integrating these web pages inside the flask code in the comming lessons
 
#this is the first step to create a website using slack.

"""<!DOCTYPE html>
<html>

<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width">
  <title>My portfolio</title>
  <link href="style.css" rel="stylesheet" type="text/css" />
</head>

<body>
  
  <script src="script.js"></script>
  <h1>Tobit's Portfolio</h1>
  <p>go to <a href="about.html">this page</a>, in case you want to know me more</p>
    <br> </br>
  <h2>SOME OF THE MANY PROGRAM I'VE CREATED SO FAR</h2>
    <br> </br>
  <h3>Day 72 Solution</h3>
  
    </p>So, Day 72, This was the final version of the secret Diary I've created, I added the feature to create an account in case it was a new person who want to create his/her personal Diary. If they already have an account, then they will be asked to LOG IN. The features that has been aded to this program (comparing to the DAY 62 Diary program), is that if a user is opening the program for the first time, it will ask him/her to create a new password and user name, and will store them inside the database. We will first hash the password to make it unusable for hackers</p>

<h4>These are the features for that program</h4>
  <ol>
    <li>Create your secret diary</li>
    <li>Add new text to your diary whenever you want</li>
    <li>View the content of your diary</li>
    <li>a secret pass is always needed before any action is taken on th diary</li>
  </ol>

  <img src="images/Day72.png" width=80%>
 <!--
  This script places a badge on your repl's full-browser view back to your repl's cover
  page. Try various colors for the theme: dark, light, red, orange, yellow, lime, green,
  teal, blue, blurple, magenta, pink!
  -->
  <script src="https://replit.com/public/js/replit-badge.js" theme="blue" defer></script> 
</body>

</html>"""



########### 

# this is the second page of the web app we are creating, we will use both of them in the coming days in flask

"""<!DOCTYPE html>
<html>
  <head>
    <title>About me</title>
    <link href="style.css" rel="stylesheet"></link>
  </head>
  <body>
    <h2>INTRODUCTION</h2>
    <br> </br>
    <p>Hey, I am Tobit BUSHENYULA, a computer science student. This is my portfolio website where you will find all my projects and see what am currently working on as a student. I am interested to work remotely. Thanks in advance</p>
                      
  </body>
</html>"""


################################################################

#DAY 76: we are introduced to flask, the tool that will help us create our web server. This web server will help us make our website dynamic (can change, based on the person or even based on what the person what it to show ). Now this is the introduction to flask and how to start using it. 

from flask import Flask # here we are first importing Flask from the flask library 
import datetime

app = Flask(__name__) # here we are now creating our web server with the variable name "app", here is where we start the flask aplication up. we will need this later on 

""" we will always be taken on the messsage wrotten inside the subroutine below each @app.route()"""

@app.route('/') # the page adress inside the parenthesis, this describes where on your domain this code refers.
def index():
  today=datetime.date.today()
  return f"""<html>
    <body> <p> Hello from Tobit! todaay is {today}
      <a href="/home"> click here to Go home</a>
    </p></body>
  </html>""" # here is the message that will b retourned or sent to the web browser page once the adress has been opened.
  # you can also notice that we used "f" like the one we use in the print function to allow us to use variables between 
  # a set of printed strings.

@app.route('/home') # Creates the path to the home page
def home(): # Subroutine to create the home page
  page = """ <html>
    <body> <h1> HERE IS YOUR HOME</h1></body>
  </html>"""
  # Three quotes - I'm going to write or paste my HTML code here. The HTML gets assigned to the page variable
  return page # returns the contents of the page variable


app.run(host='0.0.0.0', port=81) # this is the line that should always come last. This is the line that starts the web server, after this line is run, you can access your website through th web view or the repl.co web address

""" above here is the update of our flask introduction code. Here you can see that we have modified a bit what is suposed to be returned and we returned full web pages, Here you can see that we can BUILD A COMPLETE WEBSITE INSIDE ONE PYTHON FILE WHERE WE CAN BRING VARIABLES ALSO USING THE "f string method on the quotes and variables containing the web pages to be returned. DON'T forget to use the { } inside the HTML code by putting them inside tags."""












  
  
  
  