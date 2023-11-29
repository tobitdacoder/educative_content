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

# here the list has to be sorted coz we are performing a binary search.

def BinarySearch(NumList,Target):

    left,right=0,len(NumList)-1
    
    while left <= right:
        
        mid=(left+right)//2

        if Target==NumList[mid]:
            return NumList[mid]

        elif Target< NumList[mid]:
            right=mid-1
            
        elif Target>NumList[mid]:
            left=mid+1

    return f"{Target} is not in this list sorry"

NumList=[12,32,41,56,58,91,97,101,110]
Target=57

res=BinarySearch(NumList,Target)
print(res)

#This works like this:

# first we make sure we provided a sorted list because that is a must when we want to apply a binary search on a list
# then we define our function by setting the two atributes to be used (a list and a targeted number)
# then we define our left and right indexes which will be used to split our list into two at each time by setting boundaries
# we caltulate the middle of the list wich will help us starting the comoarizon, starting by the middle value
# then we comparre the target value to the middle value and if they are equal, then we return the number with the middle index.
# if the target number is not the one at index mid, and the target is less than the middle value, then we split the list into 
# two by seting the new right (top) as the value coming before the mid, or the index mid-1

# BUT if the target number is not the one at index mid, and the target is more than the middle value, then we split the list into
# two by seting the new left (bottom) as the value coming after the mid, or the index mid+1
# then we specify what to return if the value is not in the list, in this case, we will return [ f"{Target} is not in this list sorry" ]


#####################################################

# BUBBLE SORTING:

def BubleSort(arr):
    len_arr=len(arr)
    for j in range(0,len_arr-1): # This outer loop runs from 0 to loop - 1. It
                                #keeps track of the number of passes through the list.
                                # here we are talking about the number of times the loop will pass through the entire list
        swapped=False
        for i in range(0,len_arr-1):# This inner loop runs from 0 to loop - 1. It compares
                                    # adjacent elements in the list and swaps them if they are out of order.
                                    #here we are talking about checking each element to the orevious oi=ne to see if there is 
                                    # a need of a swapp or not. This is done n times fir each pass.
            if arr[i]>arr[i+1]:
                arr[i],arr[i+1]=arr[i+1],arr[i]
                swapped=True
        len_arr=len_arr-1
        if not(swapped): # this condition simply check if we swapped
                         # any elements through the list
            break
arrr=[8,1,3,2,4,9,6,7,5,0]
print(BubleSort(arrr))
print(arrr)



#EXPLANATION: 

#bubble_sort is a function that takes an array arr as input and sorts it in ascending order using Bubble Sort.
#We first determine the length of the array n.
#We have two nested loops. The outer loop runs from 0 to n-1, and it represents the number of passes through the list.
#Inside the outer loop, we initialize swapped to False. This flag helps us determine if any swaps were made during a pass.
#The inner loop runs from 0 to n-i-1. n-i-1 because after each pass, the largest element is already in its correct place at the end, so we don't need to compare it again.
#We compare adjacent elements in the list, and if they are in the wrong order, we swap them.
#After each pass, we check if any swaps were made (swapped is True). If no swaps were made, it means the list is already sorted, and we can break out of the loop early to optimize the algorithm.
#Finally, we print the sorted list.

#####################################################

#OOP : introduction to abstraction
#(more on that later)

from abc import ABC, abstractmethod
  
class Father(ABC):
    def eat(self):
        print("I can eat")
        
    @abstractmethod
    def work(self):
        print("I can work")
        
class Mother:
    def givenBirth(self):
        print("I can give birth OF COURSE")
    def work(self):
        print("I can code")

class Girl(Father,Mother):
    pass
if __name__=="__main__":
    girlOne=Girl()
    girlOne.work()
    #girlOne.work()
    #Mother.work(girlOne)
    #print(Girl.mro())

#####################################################
# I just wrote a simple python program to iterate a given list and count the occurrence of
#each element and created a dictionary to show the count of each element.

count_list=[11,45,8,11,23,45,23,45,89]


finalList=[]
Mydiction={}


for i in range(len(count_list)):
    if count_list[i] not in finalList:
        finalList.append(count_list[i])
print(finalList) # [11, 45, 8, 23, 89]

for i in range(len(finalList)):
    number=0
    for j in range (len(count_list)):
        if finalList[i]==count_list[j]:
            number+=1
    Mydiction[finalList[i]]=number
            
for keys,values in Mydiction.items():
    print(f"{keys}: {values}\t")

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
    
    Objectone=Fraction(0,0) # we have to initiate it like this since we don't 
    #want a mistate, then these two values will be overwritted by the inputs from the use
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

# this is how we calculate the fibonacci number:

def FiboNumber(Numberr):
    
    a=0
    b=1
    
    counter=1
    
    while counter<=Numberr:
        c=a+b
        a=b
        b=c
        
        print(c)
        counter+=1
FiboNumber(39)


###############################################################################

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

# here we are talking about the difference between class variables and instalce variable
# instance variables are unique for each and every instance of the class
# class variables are common to all the instances of the class, are defined outside all the methods
class Car:
    num_wheels = 4
    
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

car1 = Car("Toyota", "Camry", 2020)
car2 = Car("Honda", "Civic", 2019)

print(car1.num_wheels)  # 4
print(car2.num_wheels)  # 4

Car.num_wheels = 6

print(car1.num_wheels)  # 6
print(car2.num_wheels)  # 6

# In the above code, num_wheels is a class variable, shared among all instances of the Car class.
#  When we change the value of num_wheels for the Car class, all instances of the Car class are
#  updated with the new value. This makes class variables a useful way to store information that
#  is common to all instances of a class.

#############################################################################

# here is a simple code to find the maximum and minimum element of a list

def MAxElement(listt):
    
    max=listt[0]
    min=listt[0]
    TheList=[]
    
    for i in range(1,len(listt)):
        if max<listt[i]:
            max=listt[i]
        elif min>listt[i]:
            min=listt[i]
    return f"{max} is the maximum element and {min} is the miimum element"

TheList=[12,43,64,45,56,154,3]

print(MAxElement(TheList))
#############################################################################

# For example, we can define a class “Airplane” with attributes “make”, “model”, “capacity” 
# and a method “add_passenger” that adds a passenger to the plane’s passenger list.

class Airplane:
    # Initialize the attributes for the airplane
    def __init__(self, make, model, capacity):
        self.make = make
        self.model = model
        self.capacity = capacity
        self.passengers = []
        
    # Method for adding a passenger to the passenger list
    def add_passenger(self, name):
        self.passengers.append(name)
        
    # Method for listing the current passengers
    def list_passengers(self):
        print("Passengers:")
        for passenger in self.passengers:
            print(passenger)

# Create an instance of the Airplane class
airplane = Airplane("Boeing", "747", 400)

# Add passengers to the passenger list
airplane.add_passenger("John Doe")
airplane.add_passenger("Jane Doe")

# List the current passengers
airplane.list_passengers()

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

# PIE CHART

# this is how to generate a pie chart in python for data science and data analysis

import matplotlib.pyplot as plt # here we just import the pyplot function from the matplotlib module

Nationalities=["Sudanese","Congolese","nigerians","Others"] # these are the different nationalities 
                                                            # of international students at UCU
StudentsNumber=[123,45,12,34]

# Down here is how we proceed in order to visualize the ploting in a given order (either ascendant or descendant)

pairs=zip(StudentsNumber,Nationalities)  # so first we zip the two lists to form a kind of "number/nationality" tuples
ziped_pair=sorted(list(pairs)) # then we now sort it by first turning it into a list then use on it the sorted function
StudentsNumber,Nationalities=zip(*ziped_pair) #then here we basically unzip the two lists, if we visualize, they will be arenged in order

explode=[0,0,0.2,0] # this will allow to enphaize visualy one nationality out of all the others

plt.pie(StudentsNumber, labels=Nationalities, autopct="%.2f%%",shadow=False,explode=explode,counterclock=False,startangle=90) # and here we now use the pyplot function using the student list 
                             #to know the repartition of different nationalities in the UNIVERSITY, here we have also added the purcentage
                             # so that we can also see more details on the repartition.
                             # the shadow will be added with the shadow turned to True.
                             # the explode will just emphasize on the exploded nationality which was exploded in the explode list (by 20% or 0.2)
plt.tittle("UCU INTERNATIONAL STUDENTS NATIONALITIES")
plt.show() # to now print the chart on the screen.



###################################################################

# HISTOGRAM VISUALIZATION IN PYTHON

import numpy as np
import matplotlib.pyplot as plt

mu,sigma = 170,8  # here the mu is the mean or the average of heigh, and sigma is the variation or standard deviation from the mean.

x = mu + sigma*np.random.randn(10000) # here the 10000 iia the number of people we are working on
plt.hist( x , 100 , facecolor="blue",density=True)
plt.title("the average height")
plt.xlabel("Height")
plt.ylabel("percentage of people")
plt.text(140,0.04,"mu = 170, sigma = 8")
plt.grid(True)
plt.show()


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












  
  
  
  