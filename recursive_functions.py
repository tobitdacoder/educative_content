def main():
   num=int(input("give me a number and i will give you it's factorial: "))
   print(fact(num))

#here we have created a function called fact which will calculate the factorial of every number given

def fact(n):
   if n==1:
      return n
   else:
      return n*fact(n-1)

#this is to learn recursion and how it works
main()
