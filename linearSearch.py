list=[5,65,33,48,78,95,34,56,77,70,92,33,39,6,5,8,22,39,564,77,9,4]
attendence=['toby','theo','josh','grady','james','seth']
################################### after lists creation, we have the part one which is geting input:
answer=int(input("enter the number: "))
name=str(input("enter the name: "))

################################### now we have our first algo which checks if a number is part of the list or not
if answer in list:
   print(f"{answer} is in")
else:
   print("not in")
################################### part two (for name searching)  
if name in attendence:
   print( name, "is in")
else:
   print("not in")

#here we are performing a linear search (basic and needs improvement with time)

my_list=[34,-65,88,3,56,74,33,78,-9,7,29,-54,76,71,26]

def linearsearch(value):
   if value in my_list:
      print(f"yes {value} is in my list")
   else:
      print("no it is not")
linearsearch(45)