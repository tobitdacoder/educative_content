#the basic logic behind the fibonashi numbers is that, the next number n is the result of the sum of the two previous numbrs (n-1 and n-2)... here we use the index when calling the function

def fib(n):
   if n==0 or n==1:
      return n
   else:
      return fib(n-1)+fib(n-2)
print(fib(7))
#here the 3 is the index of the fibonashi number we are looking for:

# 0,1,1,2,3,5,8,13 ... (fibonachi numbers)
# 0,1,2,3,4,5,6,7 ... (their index which we use when calling the function)