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




