list=["une","deux","trois","trois","trois","trois","quatre"]



list.pop()

#this pop function removes the last element of the list


print(list.index("trois"))

#pour verifier l'index

print(list.count("trois"))

#this counts the number of times the world trois is repeated

list.sort()
print(list)

#this sort the list in acendent order following alphabetic or numerical order
nombre=[4,7,3,9,5,12,3,4,2,3]
#nombre.sort()
#print(nombre)

#nombre.reverse()
#print(nombre)

#this reverse function sort the content of a list in decendent order

#nombre2=nombre.copy()
#print(nombre2)

#this will copy the content of the previous list and past it to this new one

nombre.insert(1,10)
print(nombre)

#this insert the number 10 at the index 1
###########################################################################

#TUPLES:

coordinates=(4,5) 
print(coordinates[0])



#the tuple is inchangeable or inmuetable, we cant modify it anymore (unlike with the list) but we still use the indexing in the same way


#FUNCTIONS:

def salutation():
   
   name="tobit"  
   print(f"hi new user!, welcome {name.upper()}")
   
salutation()



#this last "salutation() is there to call the function"

#this is a function that will always print hello user once its called...

def hi_here(name,age):
   
     
   print(f"hi brother!, welcome {name} you are {age}")
     
hi_here("tobit",23)
hi_here("theo",21)
hi_here("israel",22)

#here the (name) which is a parameter and that is used so that whenever we call the function, it will add the name we chosen
#we can add as many parameters as we want ... like name 

def cube(num):
   print("this is the result")
   return num*num*num
   print("this is the results")

   
 
result=cube(3)
print(result)

#here the return statement will give back a value from the function called by the function... here the 3 is a parameter
#any code in the function which comes after the return statement will not be printed

#IF STATEMENT

am_male=True
if am_male:
   print("yeah am a male")
else:
   print("oh no am not...DAAAMN!!!")

#here we are using the if statement with the booleans values
#we can put thousands of code in that if statement if we want to

is_male=True
is_tall=False

if is_male and is_tall:
   #here we can also use the and gate to verify if both are true
   print("yeah he is male")
   
elif is_male and not(is_tall):
   #this not(is_tall) means if it was true, it will be false
   #Aand if it is false it will be true
   print("you are male but not tall")
   
else:
   print("he is not a male!")

#we are using keywords or logical gates (or, and)
#for the "or", only one of them have to be true or both
#for the "and" all of them have to be true in order to be true

#USE YOUR IMAGINATION FOR THE MORE COMPLEX BOOLEAN EXPRESSION        

def max_num(num1,num2,num3):
   if num1>=num2 and num1>=num3:
      return(num1)
   elif num2>=num1 and num2>=num3:
      return(num2)
   else:
      return(num3)
ans=max_num(56,2,100)
print(ans)
# these are the comparison statements (operators) we can have:
# ==, >=, <=, <, >, !=
# this is to find the greatest number among the given ones
# here we used the if and elif statements with comparison 
# statements

#we can also compare strings

num1=int(input("enter first numbr: "))
num2=int(input("enter second number: "))
print("\n")
print("1. multiplication")
print("2. division")
print("3. addition")
print("4. substraction\n")

opp=input("choose an opperation: ")

if opp=="*":
   print("answer is:", num1*num2)
elif opp=="/":
   if num2 !=0:
      print("answer is:", num1/num2)
   else:
      print("the dividand have to be different from 0")
elif opp=="+":
   print("answer is:", num1+num2)
elif opp=="-":
   print("the answer is:", num1-num2)
else:
   print("invalid opperator")

#this is a simple calculator using if statement

for i in reversed(range(100)): #this "reversed" make the order reversed while we print the result of our loop
    if i%3==0:
        print(i) 
        
        
#########################################################

def main():
    multiplier(12)
    
def multiplier(size):
    for i in range(1, size+1):
        for j in range(1, size+1):
            print(f"{str(i*j):>4}", end="")
        print()
        
main()

########################################################

def Splitter():
   #this function basicaly retrieves only the first name of a full name that the user entered
    fullname=input("enter your full name ") 
    return fullname.split()[0] #here we are using the split() function to split the input at the first place where there is a blank space (this will allow us to split exactly after the first name from the full entered name)
res=Splitter()
print(res)

####################################################


vowels=["a",'e','i','o','u']
# 1. so here we first created our list of the vowels that exist
def Checker():
   userIn=str(input("give me a word: ")) #2. here we now get the input from the user in string
                                         #   also we can use the try/except here to enhence the 
                                         #   program features to avoid errors when a bad datatype is used (we will do it after, this is the basic form of the program)
   if vowels[0] and vowels[1] and vowels[2] and vowels[3] and vowels[4] in userIn: 
      #3. here we now check if the user input contains all the vowels from the list we created
      #   this is a non proffesional way of doing it but uts the most basic to understand
      print("YEAHH 🥳🥳 all the vowels are in 😃")
   else:
      #4. this is the alternative in case the user input does not contain all the vowels
      print ("ohh no 😢no they are not in 🙂")
Checker()


########################################################

input_str = "   hello world"
output_str = input_str.lstrip() #this lstrip() only remove the leading characters, rstrip() removes
                                # the trailing characters and the strip() remove the two leading characters
print(output_str)

#######################################################


import random #here we are importing a library and we are then using its functions
# here the function is 
coin=random.choice([43,54,53,76])
print(coin)

cards=["head","tail","mix"]
random.shuffle(cards)
for card in cards:
    print(card)
    
    
##################################################

import calendar
# leaps = calendar.leapdays(2010, 2022)
# print(leaps)

print(">>>>>>>>>>Leap Year Calculator<<<<<<<<<<\n")
year1 = int(input("Enter the first year: "))
year2 = int(input("Enter the second year: "))
leaps = calendar.leapdays(year1, year2)
print("Number of leap years between", year1, "and",
      year2, "is:", leaps)

""" The script first imports the calendar module.

It then comments out a line that calculates the number of leap years between the years 2010 and 2022, using the leapdays() function of the calendar module.

The script then prints a welcome message and prompts the user to enter two years: year1 and year2. These years are converted to integers using the int() function.

The script then uses the leapdays() function of the calendar module to calculate the number of leap years between year1 and year2. The result is stored in the variable leaps.

Finally, the script prints a message that displays the number of leap years between the two input years.

Note that the leapdays() function returns the number of leap years in the range [y1, y2) (i.e., including y1 but not including y2). Therefore, the number of leap years between year1 and year2 is calculated as leaps = calendar.leapdays(year1, year2)"""