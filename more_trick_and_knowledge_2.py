
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

# those informtions can be reused evn after because they are already stored inside the dictionary



    