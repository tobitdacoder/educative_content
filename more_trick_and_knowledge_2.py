
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

###here is THE AUTO-LOADING of the text file content###

try:
  f=open("MyToDo.txt","r")
  ToDoLiiist=eval(f.read()) #here we are passing the content of the text file to the ToDo list we created above
  f.close()
except Exception as err: #here, this Exception means "every kind of error"
  print("ERROR: Unable to load, try again")
  print(err) #then we print that error here, just after the warning that there is ab error

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





















  



    