friends=["fortune","israel","theo","bingi"]
others=["josh","grady","baby"]

print(friends[1:])

#this way of using indexes allows to print all the elements of the list which comes after the index 1 element including itself

print(friends[1:3])

#this will print only the words between the index 1 and 3

friends[1]="chiz"
print(friends[1])

#this is how we update a value in a list

me="dis lui que tout ira bien"

print(me.replace("lui","toi"))
#here we replace "lui" by "toi"

friends.extend(others)
#this append a list to another or add a list to another

print(friends)

friends.append("me too")
print(friends)

#this append function helps to add another individual element at the end of the list

friends.insert(2,"me and you")
print(friends)

#this will insert the "me too" at the index 2

''' 
friends.clear()     this will delete all the elements in the list
'''

friends.remove("me and you")
print(friends)
#this removes the selected word we chosed to be removed

friends.pop()
#removes the last element of the list

print(friends.index("theo"))
#this checks if oscar is or not in the list

print(friends.count("theo"))
#count how many times the element is repeated in the list

print(friends.sort())
#put the list in alphabetic order
#or in ascendent order for the numbers list  

print(friends.reverse())
#this will print the reverse of the order of the list (alphabetic or numbers)

friends2=friends.copy()
print(friends2)
#this will creste the copy of our list

''' 
here is the structure of a tuple which is almost like a list but we can't change the content of it.. we comonly use tuples for the coordinates (like x,y,z coordinates of something that dont need to change)

coordinates=(4,5)   this cannot be modified or changed 
'''

coordinates=(4,5)
print(coordinates[1])

#this will print the number or the element at the index 1 (which is five in this case)
#here this "coordinates[1]=19" cannot work because we cannot change the elements of a tupple once we chosed them.  

coordinate=[(4,5),(5,3),(8,2)]
coordinate[1]=(32,3)
print(coordinate)
#this is a list containing tupples
#the list can be changed but not the tupples

def say_hi(salute):
   salutation=("toby"+" "+salute) 
   return salutation
   
print(say_hi("jambo"))
print(say_hi("niaye?"))
print(say_hi("ma siku zina sema aye?"))

#this is simply a function with "salute as the parameter" and "jambo as it's argument" 


'''
the basics uses of "if,elif and else" statements
the uses of the logical comparisons keywords "or,and"


is_male=True
is_tall=True

if is_male or is_tall:
   print("you are a male or tall or both")
else:
   print("you neither male nor tall")
   
!!! here, if "is male=True" then "not(is_male) means is not male or not(is_male)= not True= False" 
   
!!! we can change and do more complex things with these
statements and keywords 😊




def max_num(num1,num2,num3):
   if num1>=num2 and num1>num3:
      print("num1 is the greatest")






def max_num(num1,num2,num3):
   if num1>=num2 and num1>num3:
      return num1
   elif num2>=num1 and num2>=num3:
      return num2
   else:
      return num3
#its a must to have the block if,elif,else here for the comparizon... this will give us the biggest num... we can compare even strings or booleans

print(max_num(3,4,5))
'''




#NESTED LIST AND 2Dimension LIST:

number_grid=[
   [1,2,3,4],
   [5,6,7,8],
   [9,10,11,12] 
]

print(number_grid[0][0])
#this gonna print the number at row of index 0 and column of index 0



