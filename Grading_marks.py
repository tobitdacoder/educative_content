
point=0
def main():
   point=int(input("enter your grade: "))
   gradeit(point)
   
print("\n")  
def gradeit(n):
   if 90<=n<=95:
      print("it's an A+ 😎")
      print("BRAVO!!!")
   elif 80<=n<90:
      print("it's an A- 😃") 
      print("GREAT")
   elif 70<=n<80:
      print("it's a B+ 😇, you can do better!!!")
      print("but its also somehow Good work")
   elif 60<=n<70:
      print("it's a B- 🙂, put more work into it please")
      print("do u need some help?")
   else:
      print(" 😥 redo it please, that is not enough")
      
  
main()

#here i've created a program that grades the students for the final MARKING RANGE, while we want to know in which student category every student falls in.... this can be reenforced with time