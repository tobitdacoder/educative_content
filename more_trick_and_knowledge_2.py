
""" THIS IS THE CONTINUATION OF THE FIRST FILE ABOUT MORE TRICKS WE ARE LEARNING VERYDAY IN PYTHON"""

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
#here this is a new function we are learning. this "choice()"" function is another function from the library random ... we already know how to use the randint (random integer) with numbers and indexes, and here we are now using the "choice()" for strings random choices now !!!

answers = [
  "dog", "cat", "lion", "goat", "cow", "insect", "fish", "shark", "bird",
  "snake", "horse", "aigle"
]

Word = random.choice(answers)
FinalWord = ""
lives = 15
while True:
  letterPick = input("pick a letter of your choice:")

  if letterPick in Word:
    FinalWord += letterPick
    print("\nYou found a letter")
    print()
    for letter in Word:
      print()
  elif letterPick in FinalWord:
    print("\nyou've already found this one")
    continue

"""  The idea that i have here is that, we are going to use the index of letters in order to print them one by one while the word is builded up ... we need some for loop and if statements here for the printing and condition matching ... CONTINUE CODE AFTER
"""

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

#we can mix them like this too : print(sentense.split().capitalize()
#########################################


    