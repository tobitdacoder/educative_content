

'''
from math import *
x=int(input("enter a number: "))
print(f"the square root of {x} is {sqrt(x)}") 

'''

def main():
   x=int(input("enter a number: "))
   print(f"the square of {x} is",square_of_number(x))
   
def square_of_number(n):
   return n*n
main()

#here we have just created a function "square_of_number" that we use then in the main function...
# WE HAVE CREATED A SQUARE FUNCTION THAT CAN SQUARE EVERYTHING WE WANT 🥳🥳🥳
#here we have used the return statement so that, after creating our function we can now use it in the other one

def main():
   x=int(input("enter a value:"))
   if is_even(x):
      print("even")
   else:
      print("odd")

def is_even(n):
   if n%2==0:
      return True
   else:
      return False
'''
#here we can use this: "return True if n%2==0 else False" which is the same as the above code in the is_even function 
also we can just write: return n%2==0   
'''
#I HAVE TO BE USED TO THIS METHOD OF USING CREATED FUNCTIONS, by creating my function in the main function like we did and use it in the main function like is_even(x)
main()