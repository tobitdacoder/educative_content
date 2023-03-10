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
# else is using my function, is that you can change the underline implementations without them to notice'''



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
   print_square(3)
   
def print_square(size):
   
   #for each row in square
   for i in range(size):
       
      '''print("#"*size)'''
      print_row(size)
      
      #this will also act like the previous one
      
      #we can also create a function to print each of our row and replace the "print("#"*size)"
def print_row(width):
   
         
   print("#"*width)
   ''' we can use "print("#"*width) instead of using the for loop here'''
   #this is our new inner function that main goal is to print a row at each brick printed by the main 


main()
#IN THIS FUNCTION 👆 WE USED MANY CREATED FUNCTIONS 😁 

