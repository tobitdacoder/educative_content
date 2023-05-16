''' here lets use the "match" which is a syntax used to implement the same idea of conditional'''

#to use it, let us create a file where it promps the user name and display in which house of harry potter that persons name belongs:


name=input("what is your name: ")

if name =="harry":
   print("you're from gryffindor")
elif name=="hermione":
   print("gryffindor is your home")
elif name=="Ron":
   print("you're from gryffindor")
elif name=="draco":
   print("stythelin is where you belong")
else:
   print("who?")
   


#here we can write:
if name=="harry" or name=="hermione" or name=="ron":
   print("you're from gryffindor")





#here to avoid big work when we have a lot pf name to compare too we use another method called "match"


#IT IS DONE LIKE THIS: 
name=input("what is your name: ")
match name:
   case "harry":
      print("gryffindor")
   case "hermione":
      print("gryffindor")
   case "ron":
      print("gryffindor") 
   case "draco":
      print("slytherin")
   #here instead of default, we use "case_"
   case _:
      print("who the hell are you?!?!")
      
#but to condence it we can still use this form down here:

name=input("what is your name: ")
match name:
   case "harry"| "hermione"|"ron":
      print("gryffindor")
   case "draco":
      print("slytherin")
   #here instead of default, we use "case_"
   case _:
      print("who the hell are you?!?!")
#this 👆 is how we can use the match statement in stead of using the same "if statement"

   
def password(): 
   pass_list=["tobit","me","myself"]
   names=str(input("enter the password: "))
   if names in pass_list:
      print("you're allowed")
   else:
      print("GO OUT!!!!")
password()


times=int(input("enter the number of time u want the word 'me' have to be printed: "))
print("me\n"*times,end="")
#this end in the print statement will help us eliminate the space after the "side effect"






while True:
   
   n=int(input("enter the n: "))
   if n<=0:
      print("a positive number please")
      continue
   else:
      break
   
for _ in range(n):
   print("great")
#this will first oblige the user to enter a positive number also diferent to zero so that it can print the word "n" times depending on the users absolute positive input 




#this 👆 same code can be writen like this too👇(HERE IS WHEN WE WANT TO DO THE ACTION AGAIN AND AGAIN AND AGAIN, UNTIL THE USER GIVES US THE EXPECTED TYPE OF INPUT 👇:

while True:
   
   n=int(input("enter the n: "))
   if n>0:
      break
      #this break has got the power of breaking the loop at the moment that the condition (if statement) will be met
   
for _ in range(n):
   print("great")
   
#we can even go ahead and create our "meow" function:

def main():
   times=int(input("enter the number of times: "))
   meow(times)
def meow(n):
   for _ in range(n):
      print("meow")
main()


#we can also devellop the way of getting the input in this same main function by creating another function called "get_number()"

def main():
   number=get_number()
   meow(number)


def get_number():
   while True:
      n=int(input("enter the number of times u want to print the world: "))
      if n>0:
         return n
         #here we are use "return" instead of break because the return statement not only break the loop but also returns our n when the user gave us the wanted input type 
         
         #we can also still use the "break", then use the "return n" outside of the while loop
def meow(n):
   for _ in range(n):
      print("meow")
main()


"""this is a small game creared only using lists"""

question=["un type de fleur: ","une marque de voiture: ","une industrie d'avion: "]
answers=["rose","audi","boeing"]

totale=0

for i in range(len(question)):
   print(question[i])
   ans=str(input("what is the answer: "))
   for j in range(len(answers)):
      if ans==answers[j]:
         totale+=1
print(f"the final score is {totale}/3")



###########################################

#here we are usng the concept of NESTING

question=input("what TV show do you like: ")
if question=="infosport":
  reason=input("ohh cool.. why? ")
  if reason =="it is cool":
    print("cool 😃😃")
  elif reason=="don't know":
    Sreason=input("hohh ... how come?")
    if Sreason=="not good":
      print("OKAY")
    else:
      print("it is also okay")
  else:
    print("we don't agree on that at all")
elif question=="digitalTV":
  reason2=input("why this choice: ")
  if reason2=="because am congolese":
    print("GREAAAT")
  else:
    print("that is not bad at all")

##############################################

# THS IS AN APP FOR DAYLY AFFIRMATION AND POSITIVITY SHARING
name=input("what's your name: ")


if name=="tobit":
  scale=int(input("on a scale of 1-4, how good your day is?"))
  if scale==1:
    print("oh... sorry, you gonna be okay today, something amazing will happen to you")
  elif scale==2:
    print("oh.. a 50/50 day right ?! don't worry, something great will happen today ")
  elif scale==3:
    print("a kinda good day right? cool, keep going")
  elif scale==4:
    print("wooooow")
else:
  print("go out, you're not the one")
  
  
  
  
#####################################################

name=input("what is the name of the test? ")
print("       in",name,":")

max=float(input("what is the max score possible: "))
#score_out_of_max= max*(34/max)
score=float(input("what was your score: "))

if score > max:
  print("out of the range, the score has to be at most",max)
  
else:
  score2=score/max
  score2=round(score2,2)
  percentage=score2*100
  percentage=round(percentage,2)
  if 40.0 <= percentage < 50.0:
    print("you got",percentage,"% which is a U")
  if 50.0 <= percentage < 60.0:
    print("you got",percentage,"% which is a D")  
  if 60.0 <= percentage < 70.0:
    print("you got",percentage,"% which is a C")
  if 70.0 <= percentage < 80.0:
    print("you got",percentage,"% which is a B")
  if 80.0 <= percentage < 90.0:
    print("you got",percentage,"% which is a A-")
  if 90.0 <= percentage <= 100.0:
    print("you got",percentage,"% which is a A+")
    
    
#####################################################

from getpass import getpass as input

#THIS LIBRARY'S FUNCTION WILL HELP US TO HIDE THE INPUTS UNTIL THE ARE USED FOR COMPARISON

#Rock, paper, scisors "game"

#this will help us to hide the input between the two users to make it equal
score1=0 #alsways remember to declare the variables outside the while loop. This will ensure that the values of these variables are retained between iterations of the loop. (this will avoid the values to be returned to zero, each time when the loop is restarted)
score2=0

while True:
  

  
  print("ROCK 🪨, PAPER 📄, SCISSORS ✂️\n")
  print(""" Choose the leter you want to use:
  R: rock 🪨
  P:paper 📄
  S: scissors ✂️\n""")


  
  
  player1=input("player one enter your choice: ")
  player2=input("player two enter your choice: ")


  
  
  if player1 == "R" or player1 == "r":
    
    if player2=="R" or player2 == "r":
      print("\n the game is a tie 🪨 vs 🪨 \n")
      
      print(score1)
      print(score2,"\n")
      if score1==3 or score2==3:
        
        break
      else:
        
        continue
      
    elif player2=="P" or player2=="p":
      
      
      print("\n player2 📄 is the looser, player1 won 🪨\n")
      
      score1+=1
      print(score1)
      print(score2,"\n")
      
      if score1==3:
        break
      else:
        continue
      
    elif player2=="S" or player2=="s":
      print("\n player2 ✂️ is the looser, player1 won 🪨\n")
      
      score1+=1
      print(score1)
      print(score2,"\n")
      
      if score1==3:
        break
      else:
        continue
        
    else:
      print("\n invalid choice ... \n")
      continue
      
  elif player1 == "P" or player1 == "p":
    
    if player2=="R" or player2=="r":
      
      score2+=1
      print("\n player2 🪨 is the winner, player1 is the looser 📄\n")
      print(score1)
      print(score2,"\n")
      
      if score2==3:
        break
      else:
        continue 
        
    elif player2=="P" or player2=="p":
      print("\n the game is a tie 📄 vs 📄\n")
      
    elif player2=="S" or player2=="s":
      print("\n player2 ✂️ is the winner, player1 is the looser 📄\n")
      
      score2+=1
      print(score1)
      print(score2,"\n")
      
      if score2==3:
        break
      else:
        continue 
      
    else:
      print("\n invalid choice ... \n")
      continue
      
  elif player1 == "S" or player1 == "s":
    
    if player2=="R" or player2=="r":
      print("\n player2 🪨 is the winner, player1 is the looser ✂️\n")
      
      score2+=1
      print(score1)
      print(score2,"\n")
      
      if score2==3:
        break
      else:
        continue 
        
    elif player2=="P" or player2=="p":
      print("\n player2 📄 is the looser, player1 is the winner ✂️\n")

      score1+=1
      print(score1)
      print(score2,"\n")
      
      if score1==3:
        break
      else:
        continue 
        
    elif player2=="S" or player2=="s":
      print("\n the game is a tie ✂️ vs ✂️\n")
    else:
      print("\n invalid choice ... \n")
      continue
  
  else:
    print("\n choice not valid\n") 
    continue

if score1==3:
  print(f"the player one has got {score1} and the player two has got {score2}, PLAYER ONE IS THEIS THE WINNER")
elif score2==3:
  print(f"the player two has got {score2} and the player one has got {score1}, PLAYER TWO IS THE WINNER")
  
############################################################

#here is a guessing_game as the result of the day 18/100 of replit:

import random

guesses=0
number=random.randint(1,1000000)

print("Choose the right number between 0 and 100: ")


while True:
  guessNum=int(input("try a number: "))
  
  if guessNum<number and guessNum>=0:
    print("\ntoo low, try again")
    guesses+=1
    continue #this will go and restart the loop again
    
  elif guessNum>number and guessNum<=1000000:
    print("\ntoo high please")
    guesses+=1
    continue 
    
  elif guessNum>1000000:
    
    print("\nwe said, between 0 and 100 and not out of the range please, try again")
    continue 
    
  elif guessNum<0:
    print("we said, no less than 0 please")
    continue
  else:
    print(f"\nyeahh you are right,{guessNum} is the right number")
    break
print(f"\nit took you {guesses} guesses to get the right Number!!")   
  
#############################################################

def rollDice(): #here we are creating a function or a "subroutine" and this plays
  import random #   the game of rolling a dice and getting a random value between 1 and 6
  diceNum=random.randint(1,6)
  print(f"you rolled {diceNum}")
rollDice()

#############################################################
  
print("""LOAN CALCULATOR""") # Challenge from day 19 on replit

loan=1200
loan2=loan
apr=0.05*loan
for year in range(10):
  loan+=apr
  print("for year",year+1,"you owe",loan)
interest=loan-loan2
print(f"\n {interest} is the interest ")

#############################################################

print("LIST GENERATOR\n") #challenge from day 20 from replit

start=int(input("what is your start number: "))
end_before=int(input("what number to end before: "))
increment_value=int(input("what number do you want to increment with: \n"))

for i in range(start,end_before,increment_value):
  print(i)            

#############################################################

def Cakes(ingredient,base,coating):  #here this "ingredient" is a variable which can contain different values given at the end of the subroutine


  if ingredient == "chocolate":
    print("ohhh, I LIKE CHOCOLATE CAKES!!")
  elif ingredient == "broccoli":
    print("hummm, not so much but its okay!!")
  else:
    print("\nI don't know that but i think it is great too\n")
    print("So you want a \033[31m",ingredient,"\033[0m cake on a \033[31m",base,"\033[0m base with \033[31m",coating,"\033[0m on top?")
    

userIngredient=input("what is the ingredient you chosed: ")
userBase=input("what is the base you want: ")
userCoating=input("what do you want on top: ")

Cakes(userIngredient,userBase,userCoating)

###################################################

#challenge day 24: AN INFINITE DICE!!


def infiniteDice():
  while True:
    num=int(input("\nhow many sides do you want to use: "))
    
    rolling=rollDice(num) #this will store the value that will be rolled (the side whoch was randomly rolled)
    print("\nyou rolled the ",rolling,"th side\n")
    again=input("roll again?: ")
    if again=="no":
      break
    

def rollDice(n): #this is a subroutine we created to be used in the main function, as you can see, we are importing the random librarie coz we want to use the randint function which will help us generate random values to compose the for the dice rolling 
  from random import randint as rdt
  roll=rdt(1,n)
  return roll #this returns the random value that is passed to roll at each iteration of the loop

  
infiniteDice()

###################################################


#here we have created a pin generator which generates random pins which can be used later on
num = int(input("how many characters: "))

def RandomPin(number):
  from random import randint as rdt
  pin = ""
  for i in range(num):
    pin += str(rdt(0, 9))
  return pin ##this return is used to return the final value of pin once the loop is ended, to print it out, we have to print the call of the function (or subroutine since it cannot print without a print() function)
res = RandomPin(num) #here we need to use the print function (by asigning it to a variable) becuse the function call "RandomPin(num)" has been replaced by the "pin" by using the return statement.
print(res)



###################################################

print("""THIS IS A MATH GAME:
MULTIPLICATION TABLE\n""")

marks = 0

mult = int(input("name your muliple: "))
for i in range(10):

    final = i * mult
    res = int(input(f"{i} x {mult} = ? "))
    if res == final:
        marks += 1
        print("great !!!")
    else:
      print("oh nooo")

print(f"\nyou've got {marks} our of TEN")

#############################################################

#this is a simple child game where we ask them what animal they would like to hear and then we can output the wanted animal.

answer=input("Do you want to exit? ")
while answer=="no" or answer=="NO" or answer == "No":
  animal=input("\n what animal do you want to hear? ")
  if animal =="Cow" or animal=="cow" or animal=="COW":
    print("\n A cow goes 'Moo' 🐄🐄")
  elif animal=="Cheep" or animal=="cheep" or animal=="CHEEP":
    print("\n A cheep goes 'Meeheeheehee' 🐐🐐")
  answer=input("\n Do you want to exit? ")
  

#############################################################

#understand the "while True: " loop and what is the basic condition behind it and how to break it
while True:
  print("\nthis is running, try again?\n")
  answer=input("again? ")
  if answer =="no":
    break
print("\n the program was terminated") #this line wll be executed once the loop s broken and that is because it is not indented inside the loop, it ia our of it.

#here we are using a "while" loop which can only be broken by using the "break" keyword under a certain condition ... if the condition s met, then we apply the break, if the condition is not met, it is bypassed and the loop continues looping... THIS IS HOW THIS KIND OF WHILE LOOP WORKS, it is broken only under a condition in the "if" statement.

#############################################################

#here is another way of using the "while True" loop with nested loops and colors inside the output to make it more apealing
while True:
  color = input("Enter a color: ")
  if color == "red":
    break
  else:
    print("Cool color!")
    again=input("do you want to try again?: ")
    if again=="no":
      break
    
  
print("I don't like \033[31m red")

######################

#this is another program using the "while True" loop
count=0
print("fill the blank space if youre as cool as me\n")
while True:
  
  print("dont ___ up on me\n")
  answer=input("what is the missing word: ")
  if answer=="give":
    print("\nthat is right, you're a true fan")
    break
  else:
    print("NO, try again!!\n")
    count+=1
print("you messed up",count,"times!!")

###############################################

print("""THIS IS A MAZE GAME!!
TRY TO SURVIVE""")

while True:
  print("\nyou are in a maze coridor, what direction do  you take ?")

  print("""1. right
  2. left\n""")
  direction=input("give your answer: ")
  if direction=="right":
    continue
  elif direction =="left":
    print("you are dead")
    break
  else:
    print("wow, youre clever, you survived")
    exit()
print("you loosed, try again next time")

#################################################################

#HERE ARE SOME LIBRARIES THAT ARE USED IN GAMES ETC, we have been introduced to two of them which are the following (os, time)
"""import os

for i in range(1, 100):
  print(i)
  os.system("clear")  #this is basically telling to the console to clear every number after it has been printed by the loop and the print function inside."""

#now the TIME library
import os,time

print("welcome")
print("to")
print("REPLIT!!")

time.sleep(3) #here we are using the function "sleep" to tell to the computer how many seconds to sleep before to execute the next line of code which is to clear usng the os library
os.system("clear")

print("LET'S GO TO THE LOGIN PAGE")
time.sleep(2)

os.system("clear")

user=input("enter your user name: ")

#################################################################

#here is a small program which simulate a music player with different options
# the user can choose to play a song according to his choice, or can restart the 
# music player if wanted

# here we are using the "replit" library and the "audio" function

"""from replit import audio #to use this library "replit" u have to download it first 
import os, time

def play():
  
  source = audio.play_file('audio.wav')
  time.sleep(10)
  source.paused = True # unpause the playback


while True:
  print("MyPOD Music Player")
  time.sleep(1)

  print("press 1 to play")
  time.sleep(1)
  print("press 2 to exit\n")
  print("Press anything else to see the menu again.")

  choice=input("> ")
  if choice=="1":
    play()
  elif choice=="2":
    exit()
  else:
    os.system("clear")
    time.sleep(1)
    continue"""
  
  ######################################################
  
from random import randint as rd
import os
import time


def character():

  print("\n⚔️CHARACTER BUILDER⚔️\n")

  time.sleep(1)
  #for i in range(1,3):

  #now we  are inside the for loop
  name1 = input("name your legend: ")
  type1 = input("\nwhat type is your character (Elf,Wizard,Orc): ")

  health1 = HealthStat()
  strength1 = StrenghtStat()
  time.sleep(3)

  print("first legend name is", name1)
  print("TYPE IS:", type1)
  print("HEALTH IS:", health1)
  print("STRENGTH IS:", strength1)
  print("\n May your name go down in legends...")
  print("\n")

  print("who is the opponent?\n")

  time.sleep(1)
  #for i in range(1,3):

  #now we  are inside the for loop
  name2 = input("name your legend: ")
  type2 = input("\nwhat type is your character (Elf,Wizard,Orc): ")

  health2 = HealthStat()
  strength2 = StrenghtStat()
  time.sleep(1)

  print("second legend name is", name2)
  print("TYPE IS:", type2)
  print("HEALTH IS:", health2)
  print("STRENGTH IS:", strength2)
  print("\n May your name go down in legends...")
  print("\n")

  os.system("clear")

  characters = [{
    "name": name1,
    "type": type1,
    "health": health1,
    "strenght": strength1
  }, {
    "name": name2,
    "type": type2,
    "health": health2,
    "strenght": strength2
  }]
  #return characters

  blowCount = 0  #for counting the rounds of the game inside the while loop
  StrengthDiff = 0
  CurrentHealth2 = 0
  CurrentHealth1 = 0

  print("BATTLE TIME\n")

  while True:  #this loop will be used to simulate our two characters batle until one of them win the final batle
    print("\nthe battle !!!!!!!!\n")
    time.sleep(1)

    char1 = rd(1, 6)
    char2 = rd(1, 6)
    #the round
    if char1 > char2:

      print(characters[0]["name"], "won first blow")

      if characters[0]["strenght"] > characters[1]["strenght"]:

        StrengthDiff = ((characters[0]["strenght"]) -
                        (characters[1]["strenght"])) + 1

      elif characters[1]["strenght"] > characters[0]["strenght"]:
        StrengthDiff = ((characters[1]["strenght"]) -
                        (characters[0]["strenght"])) + 1

      CurrentHealth2 = (characters[1]["health"]) - StrengthDiff
      (characters[1]["health"]
       ) = CurrentHealth2  #we set the new value of health

      print(characters[1]["name"], ", your health is equal to", CurrentHealth2)
      time.sleep(1)

      if CurrentHealth2 <= 0:
        print(characters[1]["name"], "Have Lost and \033[31m died🕯️")
        print("\n THE WINNER IS \033[32m", characters[0]["name"],       "\033[00m 👑🥇🏆 with the remaining health of",characters[0]["health"],"!!!")
        break
      else:
        time.sleep(1)
        print(" they are both standing for the next round")
        continue
    ############### SECOND POSSIBLE OUTCOME FROM THE BATTLE:
    elif char2 > char1:

      print(characters[1]["name"], "won the blow")

      if characters[0]["strenght"] > characters[1]["strenght"]:

        StrengthDiff = ((characters[0]["strenght"]) -
                        (characters[1]["strenght"])) + 1

      elif characters[1]["strenght"] > characters[0]["strenght"]:
        StrengthDiff = ((characters[1]["strenght"]) -
                        (characters[0]["strenght"])) + 1

      CurrentHealth1 = (characters[0]["health"]) - StrengthDiff
      (characters[0]["health"]
       ) = CurrentHealth1  #we set the new value of health

      print(characters[0]["name"], ", your health is equal to", CurrentHealth1)
      time.sleep(1)

      if CurrentHealth1 <= 0:
        print(characters[0]["name"], "Have Lost and \033[31m died🕯️")
        print("\n THE WINNER IS \033[32m", characters[1]["name"], "\033[00m 👑🥇🏆 with the remaining health of",characters[1]["health"],"!!!")
        break

      else:
        time.sleep(1)
        print("they are both standing for the next round")
        continue

    else:
      continue

    #here we ae TRYING to store the data as asked in the question


def HealthStat():

  roll1 = rd(1, 6)
  roll2 = rd(1, 12)
  Roll = ((roll1 * roll2) / 2) + 10
  return Roll


def StrenghtStat():
  roll1 = rd(1, 6)
  roll2 = rd(1, 8)
  roll = ((roll1 * roll2) / 2) + 12
  return roll


character()

#######################################

def ColoredText():
  #this is a basic subroutine i which we are generating coloured text using color codes
  
  red="\033[31m"
  white="\033[00m"
  green="\033[32m"

  color1=input("> ")
  color2=input("> ")
  color3=input("> ")

  if color1=="red":
    if color2=="white":
      if color3=="green":
        print("i am a",color1,"RED LOVER",color2,"and i love it",color3,"soo much",sep=" ")

ColoredText()

#######################################

import time

#here is another cool program that gonna print some cool looking messages, here we are just learning about allignment, colours, separation and ending of strings in the print function

text = "\033[31m=\033[00m=\033[34m=\033[33m Music App \033[34m=\033[00m=\033[31m="
padding = 100  # Number of spaces to add on each side
print(f"{text:^{padding}}")

time.sleep(1)

print("""👑 \033[00mRadio Gaga 👑
\033[33m   QUEEN""")

time.sleep(0.65)
prev="\n \n \n \033[00mPREV"
print(f"{prev:>12}")

time.sleep(0.65)
next="\033[32mNEXT"
print(f"\n{next:^50}")

time.sleep(0.65)
pause="\033[35mPAUSE"
print(f"\n{pause:^80}")


#######################################

for i in range(1,31):
  print(f"day {i:^3} of 100")
#in this code we have used the format string or "f (string) logic and this basically helps us to write the text printed much easier by directly using the variAbles inside the string without taking care of the data type... we used the {i:<3} as a separator and there are three types of separation which are > right aligned, < left aligned and ^ middle alignment

#####################################

from random import randint as rd
greetings=["bonjour","konnichiwa!","bore Da!","Aloha kakahiaka","shubh prabhaat"]
randoo=rd(0,len(greetings)) #this wil store a random value between 0 and 4
print(greetings[randoo])
print(len(greetings))

#this program simply use the random library and a list of different meanings of "good morning" in different languages and then generate a random greeting among the ones inside the list

############################################

#THIS PROGRAM IS BASICALLY AN AGENDA MAKER [you can add or remove activities or items from it]

my_agenda=[] #this list has to be declared on the top of the program before you use it even before the subroutine coz if a subroutine what to access a list, it has to exit in the first place

def Agenda():
   
  while True:
    menu=input("add or remove?")
    
    if menu=="add":
      activity=input("\nwhat else is on your agenda today: ")
      if activity!='end':    
        my_agenda.append(activity)
        print("\n")
        for i in range(len(my_agenda)):
          print(my_agenda[i])
        print("\n")
      elif activity=="end":
        break
    elif menu=="remove":
      activity=input("\nwhat else to remove on your agenda today: ")
      if activity in my_agenda:
        my_agenda.remove(activity)
      #this remove() function is a function that removes an element from a list, this will help us to easily remove any element from a list despite its index
      
        print("\n")
        for i in range(len(my_agenda)):
          print(my_agenda[i])
        print("\n")
      else:
        print("this element is not in the list")
        continue
      
    
    
Agenda()

#########################

# TO DO LIST Manager HERE WE ARE CREATING A BASIC ToDo list with very basics features which we are going to improve further later. we are basically using here : A SUBROUTINE, IF STATEMENTS, LISTS, APPEND AND REMOVE FUNCTIONS and more later
import time

ToDo = []


def ToDoList():

  while True:
    choice = input("""what do you want to do?
    1. VIEW
    2. ADD
    3. EDIT (REMOVE TASK): """)

    if choice == "view":

      print("\n")
      for i in range(len(ToDo)):
        print(ToDo[i])
        time.sleep(0.5)
      print("\n")

    elif choice == "add":

      item = input("what item do you want to add to your list?: ")
      ToDo.append(item)
      print("\n")
      for i in range(len(ToDo)):
        print(ToDo[i])
        time.sleep(0.5)
      print("\n")

    elif choice == "edit":
      item = input("what item do you want to remove from your list?: ")

      if item in ToDo:
        ToDo.remove(item)

        print("\n")
        for i in range(len(ToDo)):
          print(ToDo[i])
          time.sleep(0.5)
        print("\n")
      else:
        print("this item does not exist in the list")

        print("\n")
        for i in range(len(ToDo)):
          print(ToDo[i])
          time.sleep(0.5)
        print("\n")
        continue


ToDoList()


  

