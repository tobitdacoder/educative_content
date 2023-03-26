
try:
   
   number=int(input("enter a number here: "))
   print(number)
except:
   print("invalid input")

#here in the "try block", that block will test if the input is in the good datatype before to proceed
#  and if it is not the good one, the "except" block will print the message to specify that the input was wrong    


#this esception error feature is the one that will help our program to not break  in real life when a used tend to not putting the right datatype on the input... (in case a user forget to put the right datatype).. for that we use a try except block... so that if the user enter the right datatype it's okay, but if he/she enter the bad one, the try except block will handle that error

try:
   number=int(input("enter a number here: "))
   print(number)
   #this try is the one that will check if the input is wrong so that it can immediatly shift to the exeption statement so that it will handle the problenm and protect our programm
except ZeroDivisionError as err:
   print(err)
   #here, by writing "ZeroDivisionError as err" we've stored the "ZeroDivisionError" in a variable and that us the message that gonna be printed if there is any such error 
except ValueError:
   print("invalid input")
   
#here we've specified the types of error that can be catched by the except block
# here we use the "ZeroDivisionError" and
# "ValueError"