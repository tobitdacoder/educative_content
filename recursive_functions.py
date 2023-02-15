def main():
   num=int(input("give me a number and i will give you it's factorial: "))
   print(fact(num))

#here we have created a function called fact which will calculate the factorial of every number given

def fact(n):
   if n==1:
      return n
   else: 
      return n*fact(n-1)

#this is to learn recursion and how it works... the limit of recursion in python is 3000
main()


#######################################

def main():
   num=int(input("give me a number and i will give you the addition of all the number bellow it including it: "))
   print(summ(num))

#here we have created a function called fact which will calculate the factorial of every number given

def summ(n):
   if n == 1: #base condition, this is what will help us terminate our code to avoid an infinite loop 
      return n
   else: 
      return n + summ(n-1) #this is the repeatitive task to reduce the problem step by step ... here "n" is the current value on wich we will always add the next value

#this is to learn recursion and how it works... the limit of recursion in python is 3000
main()

#this same code can be done like this in itterative approach which is not recursion approach:

def find_sum(n):
   sum=0
   for i in range(1,n+1):
      sum=sum+i
   return sum
print(find_sum(5))
 #itterative aproach we go from 1 to 5
 #but in recursion approach we go from 5 to 1  
