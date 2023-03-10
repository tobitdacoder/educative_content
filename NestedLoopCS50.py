#this file contains topics about function creation and nested loop but also their simplification to make the
# code much more easier and less expensive in term of memory consumption

for _ in range(5):
   print("#")

#get used to create my own functions
#


def main():
   print_column(4)

def print_column(height):
   for _ in range(height):
      print("#")
   #this can be also done like this:

   #'print("#"*height,end="")' and we remove the for loop, thats gonnawork too
main()

#the good thing with the functions that we create for ourself is that, even if someone
# else is using my function, is that you can change the underline implementations without them to notice



def main():
   print_row(5)
   
def print_row(width):
   print("?"*width)
main()
#here we are creating a function to print a string of question marks


#TO PRINT A SQUARE:

def main():
   print_square(3)
   
def print_square(size):
   
   #for each row in square
   for i in range(size):
      #for each brick in row
      for j in range(size):
         #print brick
         print("#",end="")
      #this print() helps us to print a new line after each row of the second loop
      print()

main()
#HERE BASICALLY, WE ARE PRINTING THE INNER LOOP "for j in range(size)" TIMES THE NUMBER OF TIMES THE OUTEER LOOP
# "for i in range(size)" WANT'S IT TO BE PRINTED THERE THE print() JUST HELPS US TO GO TO A NEW LINE EVERYTIME WHEN
# THE INNER LOOP IS PRINTED .. there we used the nested loop theory 😁





#ANOTHER WAY OF WRITING THE SAME CODE IS BY DOING THIS:

def main():
   print_square(7)
   
def print_square(size):
   
   #for each row in square
   for i in range(size):
       
      #print("#"*size)
      print_row(size)
      
      #this will also act like the previous one
      
      #we can also create a function to print each of our row and replace the "print("#"*size)"
def print_row(width):
   
         
   print("#"*width)
   #we can use "print("#"*width) instead of using the for loop here
   #this is our new inner function that main goal is to print a row at each brick printed by the main 


main()
#IN THIS FUNCTION 👆 WE USED MANY CREATED FUNCTIONS 😁

def main():
   x=int(input("what is x: "))
   if is_even(5):
      print("it is even")
   else:
      print("odd")
def is_even(n):
   if n%2==0:
     return True
   else:
      return False
#here this program is using a fuction that specifies wether the input number is odd or even
#we return the True or The false so that while using this custom function, the condition will eithr be
#trie or false in the main function (if is_even(5): [this is true by default and means "if it is true that 5 is even"])

#THIS CAN BE WRITEN LIKE THIS AGAIN:
   return True if n%2==0 else False
   #this will act just like the above statement of if and else

#THIS CAN BE WRITTEN ALSO LIKE THIS:
   return n%2==0 #here we just ask it to return true if this expression is true, the machine will understand this automatically



#now we are going to see how to se the match keywork which replaces the switch used in C:


main()

name=str(input("enter your name here: "))
match name:
   case "tobit":
      print("computer science")
   case "theo":
      print("IT")
   case "other":
      print("other course")

   case _:
      print("not found")

