
""" THIS IS THE CONTINUATION OF THE FIRST FILE ABOUT MORE TRICKS WE ARE LEARNING VERYDAY IN PYTHON
REMEMBER THAT, THIS IS A COMPILLATION OF MULTIPLE PROGRAMS. IF YOU WANT TO TRY OUT A SPECIFIC ONE, COPY IT AND PASTE IT IN YOUR ONLINE PYTHON COMPILER OF YOUR CHOICE AND TRY IT OUT !!!!"""

########################################################################

myString='tobit comment ca va ?'
#print(myString[:4]) #here the emplty space before the colomn will be filled by the default value which is 0.
#print(myString[:]) #here we will get the entire string 

#this is cool but it still very manual and can be challenging when strings are bigger

#print(myString[ : :1]) #here we want to add the gap (here is the indexes that will be jumped before to print the next index)

#print(myString[ : :-1]) #here we are going backward
print("welcome back",myString.split()[0]) #this function turns the string into a list of individual strings separated by the space char ... the index there now allows us to use different parts of that whole string

#################################

#this small program helps us to capture any vowel found in the string or the set of strings entered by the user (we give them colors just to differenciate them)

""" this can be used in kids game if we want them to identify the vowels in a sentense or in a paragraph"""

vowels=["a","e","i","o","u"]

striing=input("a string please: ")
print()
for letter in striing:
  if letter.lower() in vowels: 
    print("\033[32m",end='') #these end="" are helping us to eliminate the space in between the letters after the color text is writen
  print(letter,end='') #this end here helps us to print an horizontal sentense by eliminating the default \n 
  print("\033[0m",end='')  #Hehe we comw back to white

  #the if condition here will help us capture any vowel that is found in our string provided by the user. (this is sooo helpful)
  
""" 
THESE ARE THE COLOURS codes to be used in such games 

\033[30m  #BLACK OR GRAY
\033[31m  #RED
\033[32m  #GREEN
\033[33m  #YELLOW
\033[34m  #SKY BLUE
\033[35m  #PINK
\033[00m  #WHITE

"""

########################################################

# this program gets the input from the user and transform that sentense into a rainbow sentense by detecting the conditions of color changing we created 

sentence = input("Enter any sentence you want: \n")

for letter in sentence:
    if letter.lower() == "b":
        print("\033[34m" + letter, end='')
        #here we are basically saying, if the letter is b, set the color to sky blue, then print the letter and eliminate the \n (or eliminate the shift effect in order to print the next letter next to the previous one ... this logic is applied to all the other letters and conditions)
    elif letter.lower() == "r":
        print("\033[31m" + letter, end='')
    elif letter.lower() == "y":
        print("\033[33m" + letter, end='')
    elif letter.lower() == "g":
        print("\033[32m" + letter, end='')
    elif letter.lower() == " ":
        print("\033[0m" + letter, end='')
        #here we are using the empty space to recet the color to the default white color
    else:
        print(letter, end=' ')
        #in case the next letter is not among the listed ones, and it is not coming after an empty space, then the previous color will be applied to it
        
        
    ################################################
    #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    
#         BUILDING THE GAME: HANGMAN

import random
import os, time
#here this is a new function we are learning. this "choice()"" function is another function from the library random ... we already know how to use the randint (random integer) with numbers and indexes, and here we are now using the "choice()" for strings random choices now !!!

answers = [
  "dog", "cat", "lion", "goat", "cow", "insect", "fish", "shark", "bird",
  "snake", "horse", "aigle"
]

Word = random.choice(answers)
# for this .choice() function, we are giving a list as an argument instead of a range of numbers like for the .randint() function

letterUsed = []
OutLetters = 0
lives = 6
progress = "_" * len(
  Word
)  #this is the world we are going to always be printing by adding the letters that has been discovered

GameName = """HANGMAN GAME
  ________
  |      |
  |      💀
  |      ||
  |      /\
  |
  |
  |
############
"""
print(f"{GameName:^60}")

time.sleep(2)
os.system("clear")

print(
  "you will be asked to pick any letter that is contained in a random name of an animal we've created, then if the letter is part of that name, you will get one mark and if you loose, you will have one mark less, IF your marks are equal to zero, then YOU LOOSE!!, so be wise"
)

time.sleep(4)
os.system("clear")

while True:
  #print("\n", Word)
  print("\n")
  letterPick = input("pick a letter of your choice:").lower()

  if letterPick in letterUsed:
    print("\nYou have already used this letter. Choose another one.")
    continue

  letterUsed.append(letterPick)

  if letterPick in Word:
    #FinalWord += letterPick

    print("\nYou found a letter\n")

    time.sleep(0.5)

    #if he/she loses, we decrement the "lives"
    #for i in range (0,len(Word)-1):
    print("\n")
    for i in range(len(Word)):
      if letterPick.lower() == Word[i]:
        progress = progress[:i] + letterPick + progress[i + 1:]

    print("\n")
    print(progress)

    if progress == Word:  #here this is the condition to verify if the word has been fully guessed
      print(
        "CONGRATULATION!! YOU FOUND THE RIGHT WORLD!!!"
      )  #this is the message of success that will be printed once once the whole word has been guessed
      break

    print(f"you still have {lives} lives! use them wisely")
    time.sleep(3)
    os.system("clear")

  elif letterPick not in Word:

    OutLetters += 1
    lives -= 1
    print("No this letter is not in the word")

    if OutLetters < 6:
      print(
        f"now you have used {OutLetters} out of 6 lives remaining! be carefull"
      )
      continue
    elif OutLetters == 6:

      print("""LIVES ARE 0, YOU ARE DEAD""")
      time.sleep(2)
      break

    print("\n")
    print(progress)
    print("\n")

    time.sleep(2)
    os.system("clear")
    continue


  
  """Let's break down the appending for loop in this code step by step:

1. `for i in range(len(word)):`:
   - This line sets up a for loop that iterates through each index ('i') in the range from 0 to the length of the `word` string minus 1.
   - The purpose of this loop is to check each letter in the `word` string.

2. 'if letter == word[i]:':
   - This line checks if the 'letter' guessed by the user is equal to the character at index 'i' in the 'word' string.
   - It compares the guessed letter with each letter in the `word` string to determine if there is a match.

3. 'progress = progress[:i] + letter + progress[i+1:]':
   - This line updates the 'progress' string based on the outcome of the comparison.
   - If the guessed letter matches the letter at index 'i' in the 'word' string, it replaces the corresponding underscore ('_') in the 'progress' string with the guessed letter, preserving the correct guesses made so far.
   - It does this by constructing a new string 'progress' using string slicing.
   - 'progress[:i]' retrieves the substring of 'progress' from the beginning up to (but not including) index 'i'.
   - 'letter' is the guessed letter.
   - 'progress[i+1:]' retrieves the substring of 'progress' starting from index 'i+1' up to the end of the string.
   - By concatenating these three parts together, the line creates an updated 'progress' string with the correct guesses filled in.

4. 'print(progress)':
   - After each iteration of the for loop, this line prints the updated 'progress' string to show the current state of the guessed word.
   - This allows the user to see the progress they have made and any correct letters they have guessed so far.

The for loop iterates through each letter of the 'word' string, checking if the guessed letter matches each letter in the word. If there is a match, it updates the 'progress' string accordingly. After each iteration, the updated 'progress' string is printed to show the current state of the guessed word. This process continues until the user has guessed all the correct letters and 'progress' matches the 'word' string completely."""

  #elif letterPick in FinalWord:
  #print("\nyou've already found this one")
  #continue

  ###the idea that i have here is that, we are going to use the index of letters in order to print them one by one while the word is builded up ... we need some for loop and if statements here for the printing and condition matching

    
      
  #elif letterPick in FinalWord:
    #print("\nyou've already found this one")
    #continue

    ###the idea that i have here is that, we are going to use the index of letters in order to print them one by one while the word is builded up ... we need some for loop and if statements here for the printing and condition matching


#########################################
#here are some functions we can use for string manipulation:
# .split() to split the string into parts and can print the different parts using the indexing system 

#example:
sentense="we are the guyzz"
print(sentense.split()[2]) #here we are printing the word at the index 2 which is "the"

#you can use this technique to print in pretty maners like greetings, tests, exams, welcome messages or writing emails after getting the full name of the receiver (this function does the task called "STRING SLICING")

#other functions are .upper()
#                    .lower()
#                    .title()
#                    .capitalize()
#                    .strip() this is to erase the empty spaces arround the strings coz epmty space is also an element, so we use .strip() to eliminate those empty spaces.

#we can mix them like this too : print(sentense.split().capitalize()
#########################################

# DICTIONARIES FUNDAMENTALS IN PYTHON 

#today we talk about the core basics of dictionaries. these comes o solve the LIST problems where by, with lists we put elements in an order and that order is accessed numerically by numbers [and that is not always what we want], because we will have to remember the index or the location of the element in the list, WHICH IS A LITTLE CONFUSING... that is why dictionaries comes in useful ... basically we just assign keys to values then those values are accessed by calling the key in the print function.

#simple dictionary:

Users = {"name": "tobit", "age": "23"} # here "name" and "age" are the keys and, respectively, "tobit" and "23" are the values stored inside those keys
Users['age']="21" # here is how we change a value stored in a specific key 
print(Users['age']) #here is how to print the dictionary content
print(f"his name is {Users['name']} and he is {Users['age']}") #here is how to use the f string... it is by making sure the keys are in '' single quotes

##############################

# here is a simple program that gets credentials input from the user, stores them in a dictionary and then use them to output a customized CONTACT CARD

import os, time

title = "CONTACT CARD"
print(f"{title:^80}")

time.sleep(3)
os.system("clear")

# 1# we get the credentials input from the user:
# then we store them into these variables:

name = input("what is your name: ")
DoBirth = input("what is your DoBirth: ")
email = input("what is your email: ")
adress = input("what is your adress: ")

time.sleep(2)
os.system("clear")

# 2# then we now create a dictionary in which the previous variables we created will be used as values of the dictionary's keys

DetailsDic = {
  "Name": name,
  "Date_of_birth": DoBirth,
  "Emails": email,
  "Adress": adress
}

# 3# then we use the keys in the f string to print the inputs from the dictionary directly .. this is how we do access the values:

print("here is your contact card\n")
print(f"Name: {DetailsDic['Name']}")
print(f"Date of birth: {DetailsDic['Date_of_birth']}")
print(f"Email: {DetailsDic['Emails']}")
print(f"Adress: {DetailsDic['Adress']}")
#DICTIONARY  #[KEY]
print()

# those informations can be reused evn after because they are already stored inside the dictionary

########################################

# now dictionaries and how to use loops to iterate into the values inside

myDictionary = {"name" : "Ian", "health": "219", "strength": "199", "equipped": "Axe"}

for i in myDictionary:
  print(i)
  #here is how we print only the keys in a dictionary

print()
for i in myDictionary:
    print(myDictionary[i])
    #here is how we access the values of a dictionary.. if you remember very well, we used previously this syntax 'print(myDictionary[i])'  where i was the nake of a key placed in single quote and the output was the value associated with that key.... the i repressnt the key

  #now, we are replacing the key in quotes by the index which is equal to = key but without quotes 

#ANOTHER WAY TO ACCESS THE VALUES DIRECTLY IS LIKE THIS:
print()
for valueee in myDictionary.values():
                        #  .keys():
  print(valueee)
  if valueee.lower()=="axe":
    print(" THIS IS DANGEROUS")
print()
  #the .values() function picks only the values from the dictionary and returns them ... without using the index

  #the .keys() function picks only the keys from the dictionary and returns them ... without using the index


# if we want to obtain both the key and the value we do like this:
count=0
for key,value in myDictionary.items():
  count+=1
  print(f"{count} {key} : {value}")
  #the .item() function helps to return both the key and the value at the same time ... the .items() function always need two variabes which are both the key and the value (you can name them as you want in the loop)

  #from here we can use the variables to do some stuff like:
  if key=="strength":
    print("you're strong!") 
    
    
############################################

# this is my website rating program !!!:

WebsiteDetails={"Name": None,"Url":None,"Description":None,"Rating": None}
# we will use this kind of values to keep the space for the inputs of the user when wanted

print()
for key in WebsiteDetails.keys(): #here we just want to iterate through the dictionary keys
  print(key,": ",end="") # then here we print those keys
  WebsiteDetails[key]=input("") # then before to print the next key, we ask the user to enter the value for the key we are at before to bring in the next key
print()
  
print("\n____________________\n") 

for keyz,valuez in WebsiteDetails.items(): #now with this loop, we print the keys and the values associated with them at the same time by using the .item() function
  print(f"{keyz} : {valuez}") # then here we simply print both the keys and the values (with different names associated with them)
               
"""name=input(" name of the website: ")
url=input(" url of the website: ")
description=input(" some description of the website: ")
rating=input(" what is the rate of the website out of 5: ")

for key in WebsiteDetails.keys():"""

####################################################

#      MOCKER BEAST GAME (almost like pokemon)

import os, time

# here type is either earth, fire, air, water or spirit
Beast = {
  "Beast name": None,
  "type": None,
  "special move": None,
  "starting HP": None,
  "starting MP": None
}

#here we use this for loop to iterate into the dictionary's keys then for each key we input the value

for key in Beast.keys(): 
  print(key, ": ", end="")
  Beast[key] = input(" ")

print("\n")

# here this IF condition is just for security so that the user can't use another element other than one of the ones inside the dictionary

if Beast["type"].strip().lower() in ["water","fire","air","spirit"]:
  
  #now this FOR loop comes to print both the keys and the values from the dictionary, following a set of basic rules:
  
  for keyz, valuez in Beast.items():
    
    # this is where we use the IF statement to change the color of the output based on the type of brast that has been inputed by the user
        
    if Beast["type"].strip().lower() == "water":
      print("\033[34m", end="")
      print(f"{keyz} : {valuez}")
    elif Beast["type"].strip().lower() == "fire":
      print("\033[31m", end="")
      print(f"{keyz} : {valuez}")
    elif Beast["type"].strip().lower() == "air":
      print("\033[00m", end="")
      print(f"{keyz} : {valuez}")
    elif Beast["type"].strip().lower() == "spirit":
      print("\033[33m", end="")
      print(f"{keyz} : {valuez}")
  
  print("\033[00m", end="")

else:
  print("THIS TYPE DOES NOT EXIST")
""" 
THESE ARE THE COLOURS codes to be used in such games 

\033[30m  #BLACK OR GRAY
\033[31m  #RED
\033[32m  #GREEN
\033[33m  #YELLOW
\033[34m  #SKY BLUE
\033[35m  #PINK
\033[00m  #WHITE

"""
################################################

#here we are introducing the concept of 2D list where we have to print the content differently as we were doing with a simple list
My2Dlist = [
  ["toby", 23, "Mac"],  #first row [index 0]
  ["julia", 21, "lenovo"],  #second row [index 1]
  ["nana", 19, "Hp"]
]  #last row [index2]

print(
  My2Dlist[1][1]
)  #here, the first index is the ROW index, and the second is the COLUMN index

My2Dlist[1][
  2] = 'Mac'  #here we are changing the data at row of index 1 and column of index 2 (which is julia's computer, from lenovo to Mac)

#one of the common error done is using an index that is out of bound (for our example, using index 3 or 4 is going out of bound because the limit is index 2)

###############################################

#this is a BINGO GAME 
import random
import os,time


BingoList=[[],
           [],
           []]

used=[0] #we will use this a bit later when we find a way to use it
for list in BingoList: #this loop helps to iterate in the BIG bingolist
  previous_num=0 #this will be used for the acendent order in each list
  
  for i in range (0,3): #this will itterate in each list elements
    randNum=random.randint(previous_num+1,90) #then for each i in the list, a random value (greater then the previous one, will be generated)
    if randNum not in list: #a condition to avoid repetition in the list elements
      list.append(randNum)
      used.append(randNum)
      previous_num=randNum

answer=(BingoList[1][1]) #then here we set the very middle of the BINGO list as the number to guess
#print(answer,"\n") THIS IS THE HIDEN ANSWER !!!
BingoList[1][1]="bingo"

for i in range(0,len(BingoList)): #then here we are printing the full BIG list in order to ask      the user to guess the number.
  print(BingoList[i],"\n")

for i in range(11): #now the QUIZ !!
  final=int(input("what number is behind the world bingo ?: "))
  if final == answer:
    print("yeahhhh")
  
  elif final>answer:
    print("this is bigger than 'bingo', try again\n'")
    continue
  elif final<answer:
    print("this is lower then the 'bingo', try again\n")
    continue
  
###############################################

# this is how we can remove or append a row in a 2D list:  
ListOfShame=[]

def PrettyPrint():
  

  print()
  for row in ListOfShame:
    for element in row:
      print(f"{element:^5}",end=" | ")
    print()
  print()
  
while True:
  name=input("what is your name?: ")
  age=input("what is your age?: ")
  pref=input("what is your computer platform?: ")
  row=[name,age,pref]
  ListOfShame.append(row)
  add=input("new record?: y/n?")
  
  if add.strip().lower()[0]=="y":
    continue
  else:
    remove=input("\n do you want to remove?: y/n")
    if remove.strip().lower()[0]=="y":
      word=input("what name do u want to remove: ")
      for row in ListOfShame:
        if word in row:
          ListOfShame.remove(row)
          
      

PrettyPrint()

############################################

import random


BingoList=[[],
           [],
           []]

used=[0] #we will use this a bit later when we find a way to use it
for list in BingoList: #this loop helps to iterate in the BIG bingolist
  previous_num=0 #this will be used for the acendent order in each list
  
  for i in range (0,3): #this will itterate in each list elements
    randNum=random.randint(previous_num+1,90) #then for each i in the list, a random value (greater then the previous one, will be generated)
    if randNum not in list: #a condition to avoid repetition in the list elements
      list.append(randNum)
      used.append(randNum)
      previous_num=randNum

answer=(BingoList[1][1]) #then here we set the very middle of the BINGO list as the number to guess
#print(answer,"\n") THIS IS THE HIDEN ANSWER !!!
BingoList[1][1]="bingo"

print()
for row in BingoList:
  for element in row:
    str(element)
    print(f"{element:^10}",end=" | ")
  print() #when we do this, it is the same as printing a new line with the \n
  print("---------------------------------------")
print()
   
while True:
  next_num=input("what number comes next: ")
  found=False
  for i in range(len(BingoList)):
    for j in range(len(BingoList[i])):
      if BingoList[i][j]==int(next_num):
        BingoList[i][j]="X"
        found=True
        break
    if found==True:
      break
      
  print()
  for row in BingoList:
      for num in row:
        print(f"{num:^10}", end=" | ")
      print()
      print("---------------------------------------")
  print()    
  
  
####################################################

#  ToDo list advanced: TODOlist MANAGEMENT SYSTEM 
import os, time

ToDo = []

while True:
  counter = 0
  question = input("what do you want to do next: ")

  if question.strip().lower()[0] == "a":

    Task = []  #we will append the elements of the task in this list
    task = input("\nwhat task to add: ")
    due = input("\nwhen is the due time: ")
    importance = input("\nlevel of importance (High, medium, low): ")
    Task = [task, due, importance]
    ToDo.append(Task)  #we append the sub-list into the main list which is ToDO
    print()
    for i in range(len(ToDo)):
      counter += 1
      print(f"{counter}. ", end="")
      for j in range(len(ToDo[i])):
        print(f"{ToDo[i][j]:^12}", end=" | ")
      print()
    print()
    """print()
    for i in range(len(ToDo)):
      print(ToDo[i])
    print()"""
    continue

  elif question.strip().lower()[0] == "r":
    whatToRem = input("\nwhat do you want to remove?: ")
    if whatToRem in ToDo:
      ToDo.remove(whatToRem)
    else:
      print("\ndoes not exist in the list:")
      continue

  elif question.strip().lower()[0] == "v":

    ViewStyle = input("\nview all or priority: ")

    if ViewStyle.strip().lower()[0] == "a":  # a = all
      #now here we are trying to prettyprint each element of the Todo, containing each element we asked for earlier
      print()
      for i in range(len(ToDo)):
        counter += 1
        print(f"{counter}. ", end="")
        for j in range(len(ToDo[i])):
          print(f"{ToDo[i][j]:^12}", end=" | ")
        print()
      print()
      """print()
      for i in range(len(ToDo)):
        print(ToDo[i])
      print()"""
      time.sleep(2)
      os.system("clear")

    elif ViewStyle.strip().lower()[0] == "p":  #priority
      prior = input("\n what priority please (high,medium,low): ")

      if prior.strip().lower()[0] == "h":  # high
        print()
        for i in range(len(ToDo)):

          if "high" in ToDo[i]:
            counter += 1
            print(f"{counter}. ", end="")
            for element in ToDo[i]:
              print(f"{element:^12}", end=" | ")
            print()
        print()

      elif prior.strip().lower()[0] == "m":  # medium
        print()
        for i in range(len(ToDo)):

          if "medium" in ToDo[i]:
            counter += 1
            print(f"{counter}. ", end="")
            for element in ToDo[i]:
              print(f"{element:^12}", end=" | ")
            print()
        print()

      elif prior.strip().lower()[0] == "l":  # low
        print()
        for i in range(len(ToDo)):

          if "low" in ToDo[i]:
            counter += 1
            print(f"{counter}. ", end="")
            for element in ToDo[i]:
              print(f"{element:^12}", end=" | ")
            print()
        print()

    continue
  elif question.strip().lower()[0] == "e":
    word = input("what do you want to edit: ")
    for i in range(len(ToDo)):

      if word == ToDo[i]:
        new = input("what do you want to replace with: ")
        ToDo[i] = new
        print()
        for i in range(len(ToDo)):
          counter += 1
          print(f"{counter}. ", end="")
          for j in range(len(ToDo[i])):
            print(f"{ToDo[i][j]:^12}", end=" | ")
          print()
        print()
        """print()
        for i in range(len(ToDo)):
          print(ToDo[i])
        print()"""
        time.sleep(2)
        os.system("clear")
        continue
      
########################################

#2D dictionary notions

clue = {}


def PrettyPrint():
  print()
  for key, value in clue.items():
    print(
      key, end=": "
    )  #here the key is the "name" we add after each itteration of the loop
    for subkey, subvalue in value.items():
      #here we can use this value.item because the value is another sub-dictionary
      print(subkey, subvalue, end=" | ")
    print()


while True:
  name = input("Name: ")
  location = input("Location: ")
  weapon = input("weapon: ")
  clue[name] = {"Location": location, "weapon": weapon}
  #here name is the key, clue[name] is the variable to contain the value, and the rest is the value (which is a dictionary)

  #here we are implementing the @d aspect by creating a key containing another dictionary...  "name" is the name of the dictionary ... it can be a person name wth his characteristic beibg the content of the sub-dictionary

  # THIS IS HOW WE APPEND a dictionary IN A DICTIONARY, we furst give it a key then we assign a sub-dictionary to that key as the value of it.

  PrettyPrint()

########################################

# 2D dictionary: other way that it can be represented

john = {"daysCompleted": 46, "streak": 22} # 1st sub-dictionary
janet = {"daysCompleted": 21, "streak": 21} # 2nd sub-dictionary
erica = {"daysCompleted": 75, "streak": 6} # 3rd subdictionary

# these above are jus the values of the main dictionaries and they are the subdictionaries we are trying to access. (don't be confused with the assigment above)
courseProgress = {"John":john, "Janet":janet, "Erica":erica}
print(courseProgress["John"]["daysCompleted"])

######################################################

#      MOCKER BEAST GAME (almost like pokemon) UPDATE, USING 2D LIST NOTION

import os, time

# here type is either earth, fire, air, water or spirit
"""Beast = {
  "Beast name": None,
  "type": None,
  "special move": None,
  "starting HP": None,
  "starting MP": None
}"""

Mokedex={}
def PrettyPrint():
  print()
  print("----------------------")
  print()
  for key,value in Mokedex.items():
    print(key,end="\t: ")
    for subkeyz,subvaluez in value.items():
      print(subkeyz,":",subvaluez,end="\t| ")
    print()

#here we use this for loop to iterate into the dictionary's keys then for each key we input the value

while True:
  print("\nadd your beast: \n")
  print()
  Name=input("name > ")
  Type=input("type> ")
  Special_move=input("Special move > ")
  HP=input("HP > ")
  MP=input("MP > ")

  Mokedex[Name]={"Type":Type,"Special move":Special_move,"Starting HP":HP,"Starting MP":MP}
  PrettyPrint()

#########################################

# NEW GAME:  Top Trumps

import os, time
import random


def prettyPrint():
  for key, value in OurObjects.items():
    print(key, ": ", end="\t")
    for subkey, subvalue in value.items():
      print(subkey, subvalue, end="|\t")
    print()


OurObjects = {}
while True:
  print()
  Name = input("what is the name of your avatar: ")
  Intelligence = int(input("what is the % of intelligence 0-100: "))
  Speed = int(input("what is your speed 100-300: "))
  Strength_lev = int(input("what is your strength level in % 0-100: "))

  OurObjects[Name] = {
    "intelligence": Intelligence,
    "speed": Speed,
    "strength": Strength_lev
  }
  another = input("\nanother character? (y/n): ")
  if another.strip().lower()[0] == "y":
    continue
  else:
    prettyPrint()
    time.sleep(1)
    os.system("clear")
    break

while True:
  print()
  print("here are the characters: ")
  print()
  for key, value in OurObjects.items():
    print(key)
  print()

  choice = input("choose your character: ")
  #for key,value in OurObjects.items():
  if choice.strip().lower() in OurObjects.keys():
    print("\nyou picked", choice)

    choice2 = random.choice(list(OurObjects.keys()))
    print("The computer has chosen", choice2)

    stat = input("\nchoose your stat to use: ")
    
    #1st STAT CHOICE
    if stat.strip().lower()[0:3] == "int":
      #here we have to compare the intelligence of choice and choice2
      if int(OurObjects[choice]["intelligence"]) > int(OurObjects[choice2]["intelligence"]):
        print("\n",choice,",your choice is the SMARTEST 🧠")
        
      elif int(OurObjects[choice]["intelligence"]) == int(OurObjects[choice2]["intelligence"]):
        print("\nthe fight is though, you are equal !!!")
        #continue
        
      elif int(OurObjects[choice]["intelligence"]) < int(OurObjects[choice2]["intelligence"]):
        print("\n",choice2,", the computers choice is the SMARTEST 🧠")
        
    #2nd STAT CHOICE  
    elif stat.strip().lower()[0:3] == "spe":
      #here we have to compare the speed of choice and choice2
      if int(OurObjects[choice]["speed"]) > int(OurObjects[choice2]["speed"]):
        print("\n",choice,",your choice is the FASTEST ⏩⏩")
        
      elif int(OurObjects[choice]["speed"]) == int(OurObjects[choice2]["speed"]):
        print("\nthe fight is though, you are equal !!!")
        
      elif int(OurObjects[choice]["speed"]) < int(OurObjects[choice2]["speed"]):
        print("\n",choice2,", the computers choice is the FASTEST ⏩⏩")
        
    #3rd STAT CHOICE  
    elif stat.strip().lower()[0:3] == "str":
      #here we have to compare the strength of choice and choice2
      if int(OurObjects[choice]["strength"]) > int(OurObjects[choice2]["strength"]):
        print("\n",choice,",your choice is the STRONGEST 💪🏾💪🏾")
        
      elif int(OurObjects[choice]["strength"]) == int(OurObjects[choice2]["strength"]):
        print("\nthe fight is though, you are equal !!!")
        
      elif int(OurObjects[choice]["strength"]) < int(OurObjects[choice2]["strength"]):
        print("\n",choice2,", the computers choice is the STRONGEST 💪🏾💪🏾")
    else:
      print("\n this statistic name does not exist, try again")
      continue
  else:
    print("\ndoes not exit, pick again")
    continue
  
#######################################

# WRITE TO A FILE AND READ IT

f = open("SavedFile.txt", "w") #this "f" variable is the one which point to a copy of the file in which we have to save content.
f.write("hello there, am tobit")  #anything inside this bracket will be
#  pushed into the file

# this "write" will write to the file, each time it is called it will add to the bottom and can be called as many times as you want

#the data should be a string, idealy, so cast it with str() if you get error

#WE CAN USE MULTIPLE OF THESE "f.write" if we want too
# te inforation we are adding here is going into the RAM
f.close() # this is the line that will help us save our file after we've added new content to it. if we don't use this f.cloe(), the new content will  dissapear once we stop. 
# THIS f.close() is the function that will send back the information to the file. it is the just oposite of "open()", which we started with.

#########################################

"""THIS IS A SMALL PROGRAM THAT STORES scores and innitials in a local file so that they can be used later, hre we are using the 3 spets for using a local file (open the file, write in the file, and close the file to save the content)"""
 
FilePointer=open("HighScore.txt","a+")

while True:
  initt=input("INITIALS (3) > ")
  FilePointer.write(f"{initt} ")
  score=int(input("SCORE |0-100,000| > "))
  FilePointer.write(f"{score} \n")
  print()
  print("ADDED")
  quit=input("\n finish?: ")
  if quit.strip().lower()[0]=="y":
    break
  else:
    print("\n")
    continue
  
FilePointer.close()



# SO, here we are now reading the content of a file once it has been created:

# first, here bellow, we create a filelist called filenames.list and we choose the mode to append and create file in it does not exist...

"""f=open("finenames.list","a+")
while True:
  file=input("add file > ")
  f.write(f"{file} \n")
  quit=input("quit ?")
  if quit.strip().lower()[0]=="y":
    break
f.close()"""

# then here we are now reading the filename.list content by using the mode read ="r" ... inside the code we are using a loop to help us print the content of the file in a pretty way ... we can use f.read() to read the entire content, or f.readline() to read one line after another until the next content is a blank space so that the loop can stop.

f=open("finenames.list","r")

while True:
  content=f.readline().strip() #this strip helps us remove the \n hided in the print function
  
  if content=="": #here we are just basically making sure that, while the loop will be readint the content of ou list, once the content reaches the last file in the list, instead of taking the emplty space as the next file to print and keep printing empty spaces, we tell it to break once the content is the empty space
    break
  
  print(content) # we print here just to make sure we don't print even the blank space
  
#content=f.readline().strip()
#print(content)
#content=f.readline().strip()
#print(content)
f.close()




# WRITE TO A FILE AND READ IT

f = open("SavedFile.txt", "w") #this "f" variable is the one which point to a copy of the file in which we have to save content.
f.write("hello there, am tobit")  #anything inside this bracket will be
#  pushed into the file

# this "write" will write to the file, each time it is called it will add to the bottom and can be called as many times as you want

#the data should be a string, idealy, so cast it with str() if you get error

#WE CAN USE MULTIPLE OF THESE "f.write" if we want too
# te inforation we are adding here is going into the RAM
f.close() # this is the line that will help us save our file after we've added new content to it. if we don't use this f.cloe(), the new content will  dissapear once we stop. 
# THIS f.close() is the function that will send back the information to the file. it is the just oposite of "open()", which we started with.


#########################################

"""THIS IS A SMALL PROGRAM THAT STORES scores and innitials in a local file so that they can be used later, hre we are using the 3 spets for using a local file (open the file, write in the file, and close the file to save the content)"""
 
"""FilePointer=open("HighScore.txt","a+")

while True:
  initt=input("INITIALS (3) > ")
  FilePointer.write(f"{initt} ")
  score=int(input("SCORE |0-100,000| > "))
  FilePointer.write(f"{score} \n")
  print()
  print("ADDED")
  quit=input("\n finish?: ")
  if quit.strip().lower()[0]=="y":
    break
  else:
    print("\n")
    continue
  
FilePointer.close()"""

#after created the file, now, bellow, we are reading the content and do some printing magic with it  

f=open("HighScore.txt","r")
lists=[]
highest=0 #to store the highest num

while True: #this loop will go through the file and print each line of content that we created
  content=f.readline() #using this .readline() function, we will take one line at the time 
  if content=="":
    break
  print(content.split()) #then we print that line after splitting it to make that line a small list
  lists.append(content.split()) #then we append that small list in a bigger one to use later.
print()
print(lists) #here we print that filal big list containing the other sub-lists... THIS IS OPTIONAL

for list in lists: #then now we are introducing the comparison to find the highest of the three scores in each of the lines of the file
  if int(list[1]) > highest:
    highest=int(list[1])
print("\n")
print(highest,"is the highest score, so") #then we print the innitials of the person with the highest score

for list in lists:
  if highest==int(list[1]):
    print(list[0],"has the highest score")

f.close()

######################################################

myEvents = [] #this is the i=one in the program

# NOW THIS IS THE AUTO-LOAD (So, we load the content of the file into the myEvents list by using the eval())

f = open("myEvents.txt", "r")
myEvents = eval(f.read())  #here we are using the reading method we learned, but here we are basiclly taking the list created before and read after it is alredy converted back into code (here, back into list) and is then re-assigned to myEvents so that, even after the end of the program, the content will already be saved in myEvents... so that it cnnot be erased. NOW THE 2D LIST IS ASSIGNED TO "mtEvents" and can later be prettyPrinted. 
f.close()

def prettyPrint(): #this is our simple prety printing subroutine
  print()
  for row in myEvents:
    print(f"{row[0] :^15} {row[1] :^15}")
  print()
  
while True:
  menu = input("1: Add, 2: Remove\n")
  if menu == "1":
    event = input("What event?: ").capitalize()
    date = input("What date?: ")
    row = [event, date]
    myEvents.append(row)
    prettyPrint()
  else:
    criteria = input("What event do you want to remove?: ").title()
    for row in myEvents:
      if criteria in row:
        myEvents.remove(row)
    prettyPrint()
  """ !!!!!! here is where we automatically save the changes into our file by always overwriting the content of the file and replace it with the new content if the "myEvents" list """

# THIS IS THE AUTO SAVE, RIGHT AT THE END OF THE LOOP (inside the loop)
  
  f = open("Myevents.txt", "w")  #here we use "w" coz we want to allways fully replace the previous content and put there the new one.
  f.write(str(myEvents))  #always turn the array into a string by casting it with the str() function
  f.close()

################################################

#THIS IS OUR ToDo LIST MANAGEMENT ADVANCED ( with auto-load and auto-save inside to make it even more safe and save the content in a local file)
import os, time
#from random import randint as rd

ToDoLiiist = []
debugMode=False #this is just to help us decide wether we want to print the traceback or not.

###here is THE AUTO-LOADING of the text file content###

try:
  f=open("MyToDo.txt","r")
  ToDoLiiist=eval(f.read()) #here we are passing the content of the text file to the ToDo list we created above
  f.close()
except Exception as err: #here, this Exception means "every kind of error"
  print("ERROR: Unable to load, try again")
  print(err) #then we print that error here, just after the warning that there is ab error
  if debugMode: #here we say, if debugMode is true, then print the traceback message without breaking the code
    print(traceback) #here the traceback will print many error info we want as software devellopers, we can turn the debugMode manually to false if we don't want the users to see it at their side.

def ToDo():
  title = "ToDo list manager"
  print(
    f"{title:^60}" 
  )  #here we re just using the previous knowledge we got from how to print a title in a specific position on the screen

  time.sleep(3)
  os.system("clear")

  print("what do you want to do: ")
  time.sleep(1)
  print()

  while True:
    menu = input("\nDo you want to view, add, remove,exit or edit the todo list?: ")
    
    if menu.strip().lower()[0] == "a":
      item = input("\nwhat do you want to add?: ")
      if item in ToDoLiiist:
        print("this already exist\n")
        continue
      else:
        ToDoLiiist.append(item)

    elif menu.strip().lower()[0] == "v":
      for item in ToDoLiiist:
        print(item)
      time.sleep(2)
      os.system("clear")

    elif menu.strip().lower()[0] == "r":
      item = input("\nwhat do you want to remove?: ")
      if item in ToDoLiiist:
        ToDoLiiist.remove(item)
        
    elif menu.strip().lower()[0:2] == "ex":
      f=open("MyToDo.txt","r")
      content=f.read()
      print(content)
      f.close()
      break
      
    elif menu.strip().lower()[0] == "e":
      for item in ToDoLiiist:
        print(item)
      time.sleep(3)

      item_to_edit = input("what element do you want to edit:")
      if item_to_edit in ToDoLiiist:

        index = ToDoLiiist.index(
          item_to_edit
        )  #this is how we can store an index in a variable to use it later when we need to maybe, modify the list
        newItem = input("what do you want to replace it with?")
        ToDoLiiist[index] = newItem
        #as you can see, here we have changed the element at the index we stored into something new or into a new task

        for item in ToDoLiiist:
          print(item)
        time.sleep(3)
        os.system("clear")
    elif menu == "erase":

      for item in ToDoLiiist:
        ToDoLiiist.remove(item)
      print("the ToDolist is empty now")

    else:
      print("invalid choice, try again")
      continue

    # here is our AUTO-SAVE code, we are erasing the content of the text file and replace it with the newuly edited list "the edited ToDoLiiist"
    f=open("MyToDo.txt","w")
    f.write(str(ToDoLiiist))
    f.close()

ToDo()

#######################################
import os, time

debugMode = False
MyOrder = []

#OUR TRY AND EXCEPT CODE
try:
  #HERE IS OUR AUTO-LOAD
  f = open("ORDERS.txt", "r")  #here we are reading the whole txt file
  MyOrder = eval(f.read()) #here we are assigning the .txt file content to our list
  f.close()
except Exception as err:
  print("ERROR: the list does not exist, come later")
  print()
  print(err)
  time.sleep(2)


#OUR PRETTY PRINTING CODE
def PrettyPrint():
  print()
  print("name    pizzaSize   topping   quantity   TotCost\n",end="\t") #just for the table printing
  for row in MyOrder:
    print(f"{row[0]}        {row[1]}        {row[2]}        {row[3]}        {row[4]} \n",end="\t")
  print()


#HERE WE ARE JUST PRINTING OUR PIZZARIA SHOP NAME
title = "\nPIZZA SHOP 🍕"
print(f"{title:^12}")
time.sleep(2)
os.system("clear")

#THEN, THIS-p[[]] IS OUR LOOP WHERE EVERY THING IS DONE
while True:
  print()
  print("1. add pizza command")
  print("2. view pizza command list")
  try:
    choice=int(input("> "))
  except Exception as err:
    print("an integer please")
    print(err)
    continue
  
  if choice==1:
    
    name = input("your name please > ")
    pizzaSize = input("what size (s,m,l) > ")
    if pizzaSize.strip().lower()[0]=="s":
      price=30000
    elif pizzaSize.strip().lower()[0]=="m":
      price=40000
    elif pizzaSize.strip().lower()[0]=="l":
      price=55000
    else:
      print("does not exist, try again")
      time.sleep(1)
      os.system("clear")
      continue
    topping=input("pizza toping > ")
    
    try:
      quantity = int(input("how many pizza please > "))
    except Exception as err:
      print("this is not the right data type, please put a number")
      print(err)
      
    TotCost=price*quantity #the total cost
    order = [name, pizzaSize,topping, quantity,TotCost]
    MyOrder.append(order)
    another = input("\nanother order?: ")
    #THEN HERE WE TAKE THE LIST WITH ALL THE UPDATES AND WRITE IT IN THE .txt file
    f = open("ORDERS.txt", "w")
    f.write(str(MyOrder))
    f.close()
  
    if another.strip().lower()[0] == "y":
      continue
    else:
      thanks = "THANK YOU FOR THE ORDER"
      print(f"\n{thanks:^12}")
      
  elif choice==2:
    PrettyPrint()
    time.sleep(5)
    os.system("clear")
    
    continue
  else:
    print("wrong choice, try again")
    time.sleep(1) 
    continue

###############################################

# TODAY WE ARE AT DAY 53 AND IT IS A CHALLENGE DAY!!!
# WE ARE CREATING AN INVENTORY SYSTEM

# INVENTORY SYSTEM

import os, time, random

Inventory = [] # this is our main inventory system, it contains 
count=0 # this will keep counting the repeated element of the list (it stores the .count() function aplied on a specific element of a list
UniqueInventory=[] # this list will store the unique items.

#this down here is our AUTO-LOAD feature, that helps us to load the content of the .txt file from the local file to the "Inventory=[] list"
try:
  f = open("Inventory.txt", "r")
  Inventory = eval(f.read())
  f.close()
except Exception as err: # this is our exception handler that will handle any error coming from the text file creation or opening.
  print("ERROR: you made an error\n")
  print(err)
  
title1 = "INVENTORY"
title2="========="

print(f"\n{title1:^60}")
print(f"\n{title2:^60}")
time.sleep(4)
os.system("clear")

while True: #this is where our program stars ... here we are just making sure to ask to the user what action to do and depending on his choice, a cycle of automated actions will start as a loop until we stop it. 
  print()
  print("1. Add")
  print("2. View")
  print("3. Remove")
  print("4. Done")
  print()
  try:
    choice = int(input("\n> "))
  except Exception as err:
    print("ERROR: only an integer in the range: 1-3")
    print(err)
    time.sleep(2)
    
  
  if choice == 1: # add
    Item = input("what item do you want to add: ").capitalize() 
    Inventory.append(Item)

    for Item in Inventory:
      count=Inventory.count(Item)
      if count<=1:
        UniqueInventory.append(Item)
    
    #here we deliberatelly allow duplicate of items
  elif choice == 2: # view
    
    print("Inventory with Counts:\n")
    
    for item in UniqueInventory: 
      count=Inventory.count(item)
      print(f"{item} : {count}")
    print()
    print(UniqueInventory) #this is the list we created to contain only the element once, not repeated ones.
    time.sleep(3)
    os.system("clear")  #we are just printing the content of the list
    
    continue
  elif choice == 3: # remove 
    
    print()
    iitem = input("what item do you want to remove: ")
    if iitem in Inventory:
      print(iitem, "has been removed from the inventory")
      Inventory.remove(iitem)
    print()
    time.sleep(3)
    os.system("clear")
    continue
  #elif choice == 4:
    #pass
  f = open("Inventory.txt", "w")
  f.write(str(Inventory)) #here we are now resending the content of the list in the text file after casting it into string. this is very important.
  f.close()
  
  
#####################################################

# this is the new topic we are learning on day 54/100 of REPLIT 
# here we are learning how to access, to print the content of a CSV file
"""
import csv

with open("January.csv") as file:
  reader=csv.reader(file)
  for row in reader:
    print(",\t".join(row)) # this .join() function helps us to combine lists in a more interesting way. Here the \t is the tab, in order to print them in a nice way
""" 


import csv

total=0.0

with open("January.csv") as file:
  reader = csv.DictReader(file)  # here we are now changing it into a dictionary so that we can print only the wanted column using the column name (which is the key for our dictionary)

  # this DictReader() read the file content and turn each row into a dictionary.
  for row in reader:
    print(row["Net Total"])  # here we are now treating each row as a dictionary, and "Net Total" is a key that holds values for each day. so here we are printing the Net total for each.
    #in the csv file, the key is the heading of each column (each value in the column Net Total) is a net total of that specific day (that is why, each day we are picking only the Net Total key to print one after another for each day of the January month)
    total+=float(row["Net Total"])
  print()
  print("the Total is:",total,"and this is the benefit you made this month")
  
  ####################################################
  
#DAY REVENUE COUNTER FROM .csv files

import csv #here we are basically importing the csv library in order to use it ( it allows us to interpret and deal with files having a csv extention.)

DayRevenue=0.0 

with open("Day54Totals.csv") as file: # here we open the csv file we were given
  reader=csv.DictReader(file) #then here we store the content of that file into a file (after we turned eac row of the file into a small dictionary)
  for row in reader: #then we are now computing the result by using the key names for each row
    ProductRevenue=float(row["Cost"])*int(row["Quantity"])
    DayRevenue+=ProductRevenue
print(f"The total for this day is: ${DayRevenue:.2f}")

###############################################################

#DAY 55: The os library
import os 


print (os.listdir()) #we are going to use os.listdir() to print all the files in the directory or folder you are curently in. this is to check if a file is in a directory we think it is in.

# this is saved as a list and can be accessed as a list after we stored os.listdir() in a variable (a list variable)
listt = os.listdir() #here we are storing the conent in a list variable name
if "rere.py" not in listt:
  print("\nERROR: file not found")

os.mkdir("hello") #here we are creating a new folder with this command os.mkdir("{name of folder}")

os.rename("{name of file to rename}","{the new name here}") #here is when we want to rename a file


filename=os.path.join(" DirectoryX "," FileX.txt ")
#filename=os.path.join(" name of folder or path "," file  name ")

#here we are storing the text file in thew filename variable, and to reach it, we need to open the folder "like ours, "the DirectoryX" .. here, we are joining the directory and the file, using the os.path.join(" "," "), thi will join the folder and the file in a chronological way (just the way we see in the terminal)
f=open(filename,"w")
f.write("hi") # here we are basicaly addinng "hi" to the file FileX.txt which is in the drectory DirectoryX 
              # then we can now write something in it  
f.close()

###########################################

import os
import time
import ast

ToDoLiiist = []

###here is THE AUTO-LOADING of the text file content###

if not os.path.exists("backupFolderr"):
  os.mkdir("backupFolderr")
  #now, our folder has been created, now let us create the file using the os
filename = os.path.join("backupFolderr", "NewFile.txt")
#this is the filenae that we will use as our text file to write in using the auto-save feature at the end of the code ... here NewFile.txt is the one which is used everytime we will use "filename" the os.path.join just shows the path to use

try:
  with open(
      filename, "r"
  ) as f:  #this is the easiest way to open and automatically close a local file
    ToDoLiiist = ast.literal_eval(
      f.read()
    )  # By using ast.literal_eval() in stead of eval(), it ensures that only safe Python literals are evaluated, preventing the execution of potentially harmful code. It provides a safer alternative for evaluating the content of the file as compared to using eval()
except Exception as err:
  print(err)


def ToDo():
  title = "ToDo list manager"
  print(f"{title:^60}")
  time.sleep(3)
  os.system("clear")

  print("What do you want to do:")
  time.sleep(1)
  print()

  while True:
    menu = input(
      "\nDo you want to view, add, remove, exit, or edit the todo list?: ")

    if menu.strip().lower()[0] == "a":
      item = input("\nWhat do you want to add?: ")
      if item in ToDoLiiist:
        print("This already exists.\n")
        continue
      else:
        ToDoLiiist.append(item)

    elif menu.strip().lower()[0] == "v":
      for item in ToDoLiiist:
        print(item)
      time.sleep(2)
      os.system("clear")

    elif menu.strip().lower()[0] == "r":
      item = input("\nWhat do you want to remove?: ")
      if item in ToDoLiiist:
        ToDoLiiist.remove(item)

    elif menu.strip().lower()[0:2] == "ex":
      with open("NewFile.txt", "r") as f:
        content = f.read()
      print(content)
      break

    elif menu.strip().lower()[0] == "e":
      for item in ToDoLiiist:
        print(item)
      time.sleep(3)

      item_to_edit = input("What element do you want to edit:")
      if item_to_edit in ToDoLiiist:
        index = ToDoLiiist.index(item_to_edit)
        newItem = input("What do you want to replace it with?")
        ToDoLiiist[index] = newItem

        for item in ToDoLiiist:
          print(item)
        time.sleep(3)
        os.system("clear")
    elif menu == "erase":
      ToDoLiiist.clear()
      print("The ToDo list is empty now.")

    else:
      print("Invalid choice, try again")
      continue

  # Here is our AUTO-SAVE code. We are erasing the content of the text file and replacing it with the newly edited list "ToDoLiiist"

  with open(filename, "w") as f:
    f.write(str(ToDoLiiist))


ToDo()


###########################################################

#DAY 56 challenge: 

import csv
import ast
import os
import time

songs=[] # we will store our song playlist in this
artists=[] 
Directories=[] # this will be used to store the artists names in order to use them as sub-playlists folders
artistSongs=[] 

#first, we open the csv file in order to get what is inside

with open("100MostStreamedSongs.csv") as Songs:
  songs=csv.DictReader(Songs)
  for row in songs:
    #print(row,end="\n")
    #artists.append(row["Artist(s)"])

    if not os.path.exists(row["Artist(s)"]):
      os.mkdir(row["Artist(s)"])
    Directories.append(row["Artist(s)"])
    #artistSongs.append(row["Song"])
  extension=".txt"
  for Artist in Directories:
    for rows in songs:
      if rows["Artist(s)"]==Artist:
        if not os.path.exists(os.path.join(Artist,rows["Song"]+extension)):
          rows["Song"]= os.path.join(Artist,rows["Song"]+extension)
    
    #if os.path.exists(row["Artist(s)"]):
      #os.rmdir(row["Artist(s)"])
    # also os.rmdir(name of directory in "") if you ... 
    # ... want to remove a directory
    
############################################

# DAY 57: recursive function (we call a function in itself)

def reverse(value):
  if value <=0: # first we check if the number is allowed
    print("done! ")
    return
  else:
    for i in range(value):
      print("🥳", end="")
    print() # here we just go to another line before we call the function with a new value
    reverse(value-1) # here is where the fuction calls itself
reverse(30)

# ITERATION COMES IN WHEN WE WANT TO USE THE SAME PROGRAM BUT WITH A DIFFERENT NUMBER. IT ALSO COMES TO SOLVE MATH PROBLEMS IN A MUCH HUMAN WAY.

# COMMON ERROR

# when dealing with recursion, NEVER FORGET THE CONDITION THAT WILL INSURE THE RECURSION ( the "if statement" to check if our value is still usable, like <=0)

###################################################

#here is the DAY 57: challenge, calculating the factorial of a number of

def factorial(value):
  if value == 1:
    return 1
  else:
    return value*factorial(value-1) # = 6*5! and so on until it reaches 1!
print(factorial(6))

# this program works in this way: first, it takes the value we provided and multiply it by the factorial of the same value minius 1. By calling the function inside the function, it will automatically redo the function after multiplying the current value by the function (factorial of the value -1) 

###############################################

import random

totalAttempts = 0

def game():
    global totalAttempts  # Use the global keyword to access the totalAttempts variable

    attempts = 0
    number = random.randint(1, 100)
    while True:
        guess = int(input("Pick a number between 1 and 100: "))
        attempts += 1  # Move the attempts increment statement outside the if-elif conditions

        if guess > number:
            print("Too high")
        elif guess < number:
            print("Too low")
        elif guess == number:
            print("Just right!")
            print(f"{attempts} attempts this round")
            totalAttempts += attempts  # Increment the totalAttempts variable
            break

while True:
    menu = int(input("\n1: Guess the random number game\n2: Total Score\n3: Exit\n> "))

    if menu == 1:
        game() #here is where the recusrsionis happening. We are calling the function if the condition is met, we can call it anywhere to do a specifoic action that has been created inside its body
    elif menu == 2:
        print(f"You've had {totalAttempts} attempts")
    else:
        break

#################################################

# CHALLENGE DAY 59: PALYNDROME DETECTOR
while True:
  welcome="\ntry to see if you know a palindrome word or sentense\n"
  print(f"{welcome:^12}")
  sentense1 = input("> ") # this is our sample sentense (but we can get one from the user with the input feature)
  
  list1 = []  # this is the list that will store the first sentense form (first order)
  list2 = []  # then this list will store the reversed list of the same sentense ( we used the [::-1] to reverse our sentense)
  for char in sentense1:
    if char == " ": # condition 1: here we use this condition to remove the space between the words of the sentense so that it will be easy to cpmpare the two sentenses
      continue
    list1.append(char)
  print(list1)
  
  sentense2 = sentense1[::-1]  # this is how we read backward from the last charcter to the first ... this was learned in the string splitting course.
  for chars in sentense2:
    if chars == " ": # this condition 2 works the same as condition 1
      continue # if the char is a space, then we remove it with the continue in the loop, means (skip it)
    list2.append(chars)
  print(list2)
  
  # here we will use a boolean to define wether it is or not a palindrome:
  
  is_palindrome=True # we set it to True by default
  for i in range (len(list1)): # this will loop in the two lists we have
    #print(letter1,end='')
    if list1[i]!=list2[i]:
      is_palindrome=False
      break
      
  if is_palindrome:
    print("\nthis is a palyndrome")
    continues=input("\nwanna play again😃?")
    if continues.strip().lower()[0]=="y":
      continue
    else:
      break
  else:
    print("\nthis is not a palyndrome, try again")
    continue
    
    
##################################################

#DAY 60: TIME LIBRARY .. datetime etc
import datetime 

holiday=datetime.date(year=2023, month=12, day=10)
todays=datetime.date.today()

difference=datetime.timedelta(days=365) 
newDate=todays+difference
# means, current date plus the time deltat to get the date after the days of difference exactly after (timeDelta) days. 

# we can also use IF statement to compare two dates or more

print(myDate)
print(todays) # this can be used in the to do list in a way that it defines the day an action has been taken.
print(newDate) # here we will get the date after 14 days, that is because we added the todays date with the time delta.

# WE CAN ALSO USES IF STATEMENTS TO COMPARE THE DATES:

if holiday>todays: # as you can see, we can also use if statements to check wether what date comes after the other and act according to the results.
  print("Am coming soon")
elif holiday<todays: 
  print("ohh noo, i missed it")
else:
  print("HOLIDAY TIME!!")
  
  
######################################################

#DAY 60 CHALLENGE: EVENT COUNTDOWN TIMER

import datetime

todaysDate = datetime.date.today()
name=input("what is the event's name please: ")

year=int(input("which year > "))
month=int(input("which month > "))
day=int(input("which day > "))

eventDate=datetime.date(year,month,day)
if eventDate>todaysDate:
  remainingDays=eventDate-todaysDate
  print(f"{remainingDays} days REMAINING to the {name} EVENT🥳")
elif eventDate<todaysDate:
  passedDays=todaysDate-eventDate
  print(f"ohhh, the {name} event has passed {passedDays} days ago😥")
else:
  print("IT IS TODAYYYY🥳🥳🥳🥳🥳")
  


############################################################

#DAY 61 REPLIT: DATABASE

#first, this is how we store data in a dictionary    


BigDict={}

while True:
  name=input("name > ")
  genre=input("genre > ")
  age=input("age > ")

  BigDict[name]={"Genre":genre,"Age":age}
  add=input("add?: ")
  if add.strip().lower()[0]=="y":
    continue
  else:
    break

print(BigDict)

print(BigDict["tobit"]["Genre"])

#     NOW NOW NOW, LET US DIVE INTO THE MAIN TOPIC OF DATABASE

from replit import db

#   db["key"]="value"

db["test"]="hello there"
#here, behind the scenes, what happened is that we saved "hello there" to the key "test"

#to print the content we do almost like dictionaries
keys=db.keys() # this "keys" is a dictionary that stores the keys in the DB and can be used later.
print(keys)

for key in keys:
  print(f"{key}: {db[key]}") # here we print the key and the value from the database

value=db["test"]
print(value) # this is how we can also access and print only the value stored inside a DB key

del db["test"] # this is how we delete a key in the database.

# WE CAN ALSO ACCESS ALL THE KEYS WHICH HAS A CERTAIN PREFIX:
#     this is when we have a bunch of keys that look similar or start with similar text but have diferent last text or value ... like certain topics or messages

db["login1"]='david'
db["login2"]='dando'
db["login3"]='martina'
db["login4"]='malaika'

keys=db.keys()
if "test" in keys:
  del db["test"]

print(keys)

matches=db.prefix("log")
print(matches) # this will print a dictionary containing the keys names that have the same prefix ... in this case it is "log"

# NEXT: keys and dictionaries...................

# in the database, we can store in a database key, a dictionary or a list, here is how we do:

db["toby"]={"pseudo": "DaMan","psssword":"DaMan1999"}
keys=db.keys()
print(keys)
value=db["toby"]
print(value) # to print the value (which is a dictionary) of the key "toby"
print(value["pseudo"]) # here we access the sub-dictionary and print some value rom it

# NOW YOU CAN TELL THAT, THE POINT OF USUNG 2D DICTIONARIES IS WE USE IT TO BUILD A PERSISTENT DATABASE THAT IS ALWAYS THERE AND DOES NOT DISSAPEAR WHILE THE REPL IS OFF... so we can store dictionary values in it !!!!

# you can only store 5000 different items 😥,however, THOSE CAN BE 5000 DICTIONARIES 😊


# DAY 61 CHALLENGE: TWEETS RECORDING IN DA TABASE, USING TIMESTAMPS 

from replit import db
import datetime



while True:
  try: # this try and except close was to manually remove the data inside the database usind the del db["name on key"] 
    del db["login4"]
    del db["login3"]
    del db["login2"]
    del db["login1"]
    del db["toby"]
  except:
    pass  # we used this pass here in order to just tell to the code, don't do any thing, just pass to the next of the code.
  #archiveKeys=[]
  option=input("\nadd tweet or view tweets? > ")
  
  if option.strip().lower()[0]=="a":
    print("\ntype your tweet please: \n")
    print()
    tweet=input("> ")
    
    timestamps=datetime.datetime.now()#this is how we find the timestamp by using the datetime library
    timestamp_int=int(timestamps.timestamp())
    #this turn the time stamp into the number of seconds since 1968 (universal timestamp)
    
    db[str(timestamp_int)]=tweet # here we automatically turn our timestamp into a string that will be used as the key to store the tweet.
    continue
    
  elif option.strip().lower()[0]=="v":
    keys_int=[] #this will store the keys transformed in integer
    keys=list(db.keys()) # here is a list of the timestamps_int turned back into integer
    for key in keys: #here keys is already a list containing strings
      key_int=int(key)
      keys_int.append(key_int)
      
    sorted_keys=sorted(keys_int,reverse=True) # descendent order, to start from the latest tweet with the highest timestamps_int, to the oldest tweet with the lowest timestamps_int.THE LATEST IS THE ONE WITH THE HIGHER timestamps_int (the highest number of seconds)
    print()
    for key in sorted_keys:
      key_str=str(key)
      #smallest=min(int(db.keys()))
      print(f"{key_str}: {db[key_str]}")
      
  
    
  # here is a list of the timestamps_int turned back into integer

      
"""elif option.strip().lower()[0]=="v":
    keys=list(db.keys())
    print(int(keys[0]))"""  
    
    
#################################################################### 

# DAY 62 CHALLENGE: CREATE A PERSONNAL DIARY

from replit import db
import datetime

# first we ask for the personal password (since it is a personal diary, so the password has to be different)
    

      



    

    
 
  




























  



    