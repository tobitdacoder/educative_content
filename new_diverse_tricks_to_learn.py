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
   print("oh no am not...FUUUUCK!!!")

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

def name():
    fullname=input("enter your full name ") 
    return fullname.split()[0]
res=name()
print(res)

####################################################


vowels=["a",'e','i','o','u']

def Checker():
   userIn=str(input("give me a word: "))
   if vowels[0] and vowels[1] and vowels[2] and vowels[3] and vowels[4] in userIn:
      print("all the vowels are in the word")
   else:
      print ("no they are not in")
Checker()