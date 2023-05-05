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



