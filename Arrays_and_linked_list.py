''' ALWAYS REMEMBER TO TRY BY YOURSELF TO SEE IF YOU;VE IMPLEMENTED THE CONCEPT IN EACH PROGRAM, ALSO, DONT LUNCH THE CODE DIRECTLY FROM THIS FILE BECAUSE IT IS AN EXPLANATORY FILE WHERE WE ARE MIXING SOME BASICS CODES ... ALWAYS REMEMBER TO COMMENT THE PART YOU DON'T WANT TO EXECUTE 😁'''


import numpy as np

lst = list(range(100))
print(lst)

#in this code we are importing the "numpy" library and we use one of its functions wich is list()
# here the output will be a list of numbrs from zero to 99, remember, for the list there are comas 
# separating the values, which is different from the array and we are going to see it soon
# This numpy library is very vast and can allow us to use many different relevant functions that we are going to explore with time

########################################################################

a = ['foo', 'bar', 'baz', 'qux', 'quux', 'corge']

print(a[-5:-3]) #here we can see that we can use negative indexes and that will work in the inverse
                # of normal positive indexes (here "corge" is at index [-1] and also index [5])
                # here the [-5:-3] specifies a range of values to be printed except the value at index  [-3]
array=np.array(a)
print(array.dtype)
print(array.shape)
sub_array=array[1:4].copy() #to copy and get a new array which will be the slice of the previous one
                            #in the index range 1:4 where is 4 excluded

########################################################################

array = np.arange(100) 
print(array) #the output here will be an ARRAY ... and the first difference we can see between the list and the array is that the values in an array are not separated with a coma buy just an empty space

########################################################################

data = [2, 4,7.5, 8, 1]
array = np.array(data)
print(array) #here we are converting a list into an array. the np (is the library 'numpy' and np.array(data) means "convert data into array")
print(array.dtype) # here we want to print the data type of the array contents
print(array.shape) # this will print the number of elements in the array (the dimensions in a tuple)
print(array.ndim) # this will print the dimension of the vector (which is an array and we know that an array can be accessed as a vector and vectors have dimmensions ... a  vector of one row and "n" column is of dimmension 1, a vector of 2 or 3 or 4 or n+1 rows and many columns is a 2 dimension vector or array)

#########################################################################

data = [[2, 4,7, 8, 1], [23, 5, 9, 3, 9], [4, 10, 43, 12, 0]] #here we've created a list of lists and we want to convert it into an array (also, remember that it will be a matrix of three rows and 5 columns after)
array = np.array(data) #here is the conversion code of the list called "data"
print(array) #here we simply print the array created
print(array.shape) # here we will print the number of rows and columns (row,columns)
print(array.ndim) #here we will print the dimmension of the matrix (we have two rows and 5 columns so its a 2 dimension matrix (here its an array which acts like a matrix))

#########################################################################

array = np.zeros((3, 5))
print(array)
#this small program will create an array of zeros which will have 3 rows and 5 columns
# remeber that here we used the numpy library to call the "zeros" function which
# here weve used the abreviated form of numpy which is "np" as we specified while we impored the library

array = np.ones((3, 5)) #this program will do the same but instead of zeros it will be a matrix of ones
print(array)

array = np.eye(4) #this special function "eye" will print a 4 by 4 matrix (an array) where the main diagonal is filled by ones and the other places will be zeros 
print(array)

array = np.eye(4, dtype=int) #this is the same as the previous one but here the elements will be integer coz we specified the datatype by writing "dtype=int"
print(array)

#########################################################################

array=np.random.randint(0,100,(3,5))
print(array) #this program will print an aray (matrix of 3 rows and 5 columns) with random values inside between 0 and 100 which was specified coz we wrote "random.randint()"

#########################################################################

data=[[3,5,4,3,6,8,5],[8,6,9,5.4,3,6,8,]]
array=np.array(data)
print(array) #here we will have an output of an array of those two lists
print(array * array) #here we are multiplying the array by itself using the matrix theory about multiplication
print(array**2) #here we are squaring the matrix ( which is our array)
print(array - array) #here the output will be a matrix of zeros coz weve substracted every element if the matrix by it self.


data = [[2, 4,6, 8, 10], [1, 2, 3, 4, 5]]
array2=np.array(data)
print(array2>array) #here the output will be a matrix of boolean values (true or false)
#and that is because with that expression we are comparing each element in the array2 matrix with the elements in the array matrix, if its greater then the output will be true.

array_copy=array[4:7].copy() # this will copy the elements in the index range we choosed
print(array_copy) #this will print the sub_array we copied from the original one.


array = np.arange(10)
print(array) #here the output will be a row matrix with one row and 10 colums with elements from 0 to 9
print(array[7]) #here also we can use the index to licalize an element from the array
print(array[2:5]) #elements of index 2 to 5 with the fifth element excluded
array[6:8]=15 #here we say that the elements from idex 6 to 8 exclided are going to be 15.

################################################################################ 

array_slice=array[4:7].copy()
print(array_slice) #here the output will be the sliced array that we took from the main one using indexes
array_slice[2]=500 #the element at index 2 of the array_slice array will be equal to 500



################################################################################

array2d=np.array([[4,3,5,9,7],[9,4,5,2,6],[7,6,5,9,1]])
print(array2d[2][2])
print(array2d[2,2]) #these are the same and produce the same output which is the value located at the row of index 2 and the column of index two (5)




###########################################################

#                     LINKED LISTS


# single node linked list -- single linked list
class LinkedList:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

first = LinkedList(3) #this is our first objext created and we provided value for data (which is three and the default value for next (which is none))... here we created the object by first writing the class name then in the () we put tje values for the parameters we created in the innit function
print(first.data) #this will print 3 (which is the argument assigned to "data")
print(first.next) #this will print none (which is the argument assigned to "next") 


################################################

#more about linked list (from a tutorial)

stock_prices=[235,654,879,345,888,769,871] #here is an array we create (we have to look first into arrays coz linked list are helping to solve the arrays problems and limitation)

stock_prices.insert(1,444)
# so here we are inserting the number 444 in the list at the index 1, which will push the existing numbers back to leave a space for the inserted number

#here the array insertion complexity are of order of n or O(n).

#when we create an epmty list like "list=[] it alocate a memory space for that list, python lists are dynamic arrays and here is allocated a space capacity of 5 element " and when we start inserting (here we are appending, adding values to the end of the list) values in the list, the values are filling those spaces allocated for the list... when we added three values and we want to add another value but at the location of an existing value, it will puch the existing to make a space for the new value

#now lets imagine that our array is full of capacity (capacity is = 5 and all the five are filled), when we want to insert a new value.. the way dynamic array works now is, since it cannot use other values memory location, it will go in some area of the memory (RAM) then it will allocate more capacity and then will copy all those elements one by one, so if the initial capacity is 5, it will allocate additional 5*2 =10 (or additional capacity 5*2=10) memory locations... now there are 15 capacity or memory locations


#THIS IS NOT THAT EFFICIENT THO 😥

#lets imagine a structure where values are stored into different areas of memory (linked list) .. here we have the    "| value | next value adress |" 

# first, arrays store the value in contegious mem. location while this (linked list) is storing them into random memory locations which are linked with a pointer which point to the next adress  ... so the first value has a reference side to the adress of the next value or element ... those are the links we are creating here.

#here it become much easier to insert a new value coz there is not a limitation of capacity for the array... now we are not copying from one location to another.

#here when we insert or delete element at the begining, the complexity is = O(1)  [this one is just because while inserting, its creating a node for the new element and the adress of the next element, so its iterating only once coz its the elements at the index 1]  and    when we want to insert or delete element at the end the complexoty is = O(n) because we have to iterate between all the elements of th list

#so, linked list has two main benefits over an array: 
# 1. you dont need to pre-allocate space and 2. insertion is easier

#there are also double linked-list (where its no longer |value adress |next address| but now its |previus adress| current value adress | next value adress) this allows to comeback easier, the backward traversal is easier .... the traversall of a list is O(n)

#the only advantage an array has is, if you know the index of the element in array on order of 1 (O(1)) which is a constant time operation.. so in array if you want to access the fifth element you just have to specify the index of the element into [] and it will go directly to it, but for linked list, it has to go through all the elements to follow the links 

#inserting/deleting elements at start in array is O(n) coz u have to copy all the elements, but for linked list it is O(1) ,  you dont need to.add()

#inserting elements in the middle is O(n) for both.add()

#    IN PYTHON NOW 😃: !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

#lets create two classes:

class Node: 
   def __init__(self,data=None,next=None): #this is the constructor of the Node class and has got two elements which construct the class (they are "data" and "next")
      self.data=data #this can contain integers, numbers, or complex objects
      self.next=next #this is a pointed to the next eelement
      #this "node"class represent a single element in the linked-list (it has two class members which are data and next)
      
class LinkedList: 
   def __init__(self):
      self.head=None
      #this class is a class where we need a head variable which points to the head of the linked list (beginning)

#so now we start by adding a method (function called insert_at_begining)

   def insert_at_begining(self,data): #this is taking the data value and insert it at the beginning of the linked-list !!! THIS IS THE FIRST FUNCTION TO INSERT AT THE BEGINING OF A LINKED-LIST
      
      #LET US CREATE A NODE TO EXPLAIN HOW IT WORKS
      node= Node(data,self.head) #this "self.head" is taking the place of the "next" which is the pointer to the next value of the list and her the "self head is the first pointer"
      
      #just to make things easier,lets say there is an existing head, when we add a new element(data), it will create a node where the "next" value will be the previous self.head which was pushed. (now it become the address of the next value and the current value is now the new node we created)  here the self.head is now the adress of the next value (which was our head value before we inserted anoter at the front) 
      
      #!!! REMEMBER, HERE THE "node" is an object we are creating and the "Node" is the class of the first value we created before 
      
      #so, here the self.head will be used in a case where, when we want to insert a new value or element, this self.head will be automatically the pointer to the value that was pushed (here will be the adress of the value we pushed so that the next value will be this one we pushed and that is by using its adress to point at it) and
      
      #so, the data in "node=Node(data,self.head)" is the new value we are inserting and the adress which will be in that node will be the adress of the next value (or next element)
      
      #so, lets say we already have a head, and if we are inserting anything (any new data) infront of it, what gonna happen is, we will create a new "node" element (which is an object from the Node class) and the next value of that node will be the current head of the exiating value that will be pushed (here there is not yet another element which is pusshing the new element)
      
      self.head=node
      #here, its easy, we are simply saying that , now, since the new node is created, it become our new head (so that, if we want to insert another new element, this one will be pushed also and let the new node be the new head, and the self.head of that new new element will be the adress of the previously created element)
      
      #in other words, here we are saying that our new head adress is the adress of the newuly created "node", this will be used when we will create a new element so thst it will be the "next" adress of the newly created node(which has a data and the adress of the pushed node) ... I REPEAT 🙏 the self.head of the newly created node will be the adress of the node we inserted earlier.
      
      #!!!!! PAY ATTENTION!!! in all the functions we are creating,we are using the "self" keyword in the parameter parentheses (i will explain it a bit later 😊)
      
      #so here we still in the same class remember, and to verify this insert_at_begining() function, we have to use the utility function called print:
   def print(self):
      if self.head is None: #means there is not any alredy existing head in the lonked-list
         print("linked list is empty")
         return #this return is to break the condition after its verified
            #here, what we just did is that we create this function print so that, if the linked list, where we want to insert a new element or data, is empty, then it will tell us
            #whith this return, we dont need to use the elif again, we can just set the other condition directly
      itr=self.head #here we mean, if head exist, we store it in itr (itterator)
      llstr="" # "linkedliststring", this is the list where all the elements will be stored after being itterated
      while itr: #while its true or its exist .. we will itterate through the whole list
         llstr+=str(itr.data) + ' --> ' #so here the data which is being itterated will be stored in llstr then we go to the next value ( <-- : this is the direction of itteration)
            #the '-->' is just to show the link (it can be removed without problem 😊)
         itr=itr.next #here we say, now since there are an existing head, that head will become the "next" of the new "self.head =  the new value... so the itr become itr.next (next of the self.head or the new head) remember that it is like that coz we stored the self.head in itr (we stored the already exiating one in itr so that we can easily transform it into the "next" or the adress of the next value)
            
            #anoher way to undrstand it very well is that, while printing, it will start by the last value in the list, verify if it is a head, then turn it into the "next" adress of the coming value to be analised by the printing function... for it, it will be iterrated and become the "next" then we go to the other value (from right to left <-- ) and keep itterating until it reaches the last value to see if there is a head which keep existing after the value we are at, if there is not any value, then the while loop is broken (no head existing after the value we are at so it cannot make the current value the "next" adress of a non existing value)
            
            #WE ARE ITTERATING THROUGH ELEMENTS ONE BU ONE (dirrection: <-- )
            #and for each itteration, the value that is made "next" will be printed after being itterated (and that will make our output)
      print(llstr) #here, after the loop was broken, we print the linked list with the added elements #!!! SO NOW, TO CHECK THIS, WE HAVE TO CREATE A LINKED LIST NAME TO BE USED IN THE PRINTING PROCCESS!!!
         
         #NOW WE ARE TRYING TO INSERT AND PRINT THE LINKED LIST
         #THERE IS A SMALL PROBLEM WITH THE PROGRAM THAT WE ARE GOING TO FIND OUT SOON BUT FOR NOW, THIS IS HOW THE CODE IS SUPPOSED TO E WRITEN and printed
         
         #😁 The error was finally solved, it was a syntax error and not a logical error 😁
   
   
   def insert_at_end(self,data):
      if self.head is None: #if the list is empty, or there is not any head node in the list
                            # then the data we insert now will be the new head and after it there is not any value which can be the next (that is why we used the None)
         self.head=Node(data,None) #here we just mean that "now, the new head is the new entered
                                 # data" which does not have any next value or is not pointing at any value since it is the only value in the linked list
                                 
                                 #reemeber for the insertion at the begining we used the "node" object Node(data,self.head) whith the self head as the next value, here, since we want to ad a value at the end if the list, there is not any "next" value that has to be after the adedd value
         return #this is to show that, since there is now only one value added, we will break the condition just after we added the the single value
      itr=self.head
      
      while itr.next: #while there is another value as the "next", then we are not yet at the end of the list.
         
         itr=itr.next  #her we mean : since there is a "next" vlue to the current head, lets make that next value our new itr (self.head) and check again the condition in the loop to see if there is another value after the new itr (which was the previous itr.next), 
      itr.next=Node(data,None) #here it means that we reached the last element and for that element there is not a next value, then its next value will be the bew node we've created which does not have a next[ Node(data,None)], so after the loop is broken, which means that there is not another next value existing after, we can now add our new element (which will be the "next" of the nast element which did not have a "next" before we added the new data)
      
#!!!!! 👆👆👆UNTIL NOW, WE'VE LEARNT THE METHODS (insert_at_begining, print, insert_at_end) 😃😃
#!!!!! NOW LETS STUDY OTHER INTERESTING METHODS (OR FUNCTIONS)

# SO, THE NEXT METHOD WILL BE A METHOD THAT ALLOW US TAKE A LIST OF VALUES AS AN INPUT AND IT WILL CREATE A NEW FRESH LINKED LIST.

   def insert_values(self,data_list):
      self.head=None #here we dont use the conditional "if" to check wether the list is empty or not because we are going to wipe up all the current value from the list and input new values in that list
      for data in data_list:
         self.insert_at_end(data) #here this loop comes to use our previous function (method we created called "insert_at_end")
                                  #and it is using it so that, when we want to input a list of values at the same time, each value from that inputed list will come after another until we reach the last value which will be added at the end (coz we used the insert_at_end method)
                                  
   def get_length(self): #this function will basically help us to get the lenght of the linked list
      count=0 #here we initiate the count so that if there is a head which exist, we will incremement by one for each head
      itr=self.head
      while itr: #here is the loop that will help us find the total count of the element
         count+=1
         itr=itr.next
      return count #if the loop is broken, the count will then be retrieved
   
   def remove_at(self,index): #this function will remove the element at the wanted index
      if index < 0 or index >= self.get_length(): #here we are just specifying that if the index is negative or above the index range of the list, it will be an invalid one. here  "index >= self.get_length()" means that if the length of the list is 6 then the last element is of index 5 (so 6 is >= index and is invalid )
         raise Exception("invalid index 😥") #this is the exception that will be raised if the if statement's condition is met (learn more about this one) , this will appear as an error message if the condition above is met
      if index==0: #here we just say "if the index is equal to the head element (index 0)" then we remove it (WE ARE REMOVING THE HEAD AT THE BEGGINNING OF THE LIST)
         self.head=self.head.next #and this is how we remove the head, by making our next element our new head (this will remove our previous head of index 0)
         return
      count=0 #this because in linked list you have to manualy maintain the count to reach that particular index (here we are dealing with O(n) ), here, since we are not dealing with an array, we have to count manualy the index count since the elements are in different locations 
      
      #so as usual, to itterate through the list, we do:
      itr=self.head
      while itr:
         
         if count==index-1:
            #here we are going to point at the "next" of the previous element (the previous element is the element at index-1)... then its "next" will point at the element we want to remove (is the element we want to remove)
            itr.next=itr.next.next
            #here is the "next" of the previous value (at index-1) which we modify and make it the next of the next (now the new "next" will be the element coming after the element we want to remove)
            break #after the element has been removed, we can break the while loop
         itr=itr.next #this itr.next we are using here is the new itr.next from the if statement !!
         count+=1
         #here we have to iterrate through the list to reach that index (and the value under it)... this go through each of the elements in my linked list.
         
         #note this: in linked list, you have to stop exactly at the element that is prior to the element you want to remove and in that prior element you can modify the links that i have (the next link that i have) so that after modifying the "next" link, it will remove that original "next", and then the element will be removed.
   #NOW WE KNOW HOW TO REMOVE AN ELEMENT FROM A LINKED LIST, USING ITS INDEX, LET US NOW LEARN HOW  TO CREATE A FUNCTION WHICH WILL INSERT AN ELEMENT AT A SPECIFIC INDEX 😃:
   
   def insert_at(self,index,data): 
      if index < 0 or index >= self.get_length():
         raise Exception ("invalid index 😥") #here we are just reusing our raise exception again (you now know why)
      if index==0:
         self.insert_at_begining(data)
         return  #here we are jusr specifying what the program will do if the provided index is 0... now we are reusing our previously created function "add_at_begining" as the default function to be executed for this particular condition
         ''' here we wan also use another way if we don't want to use the "self.insert_at_begining(data)" and that is by creating a note and the "next" of that node will be the self.head just like we did with the "insert_at_beginning()" function''' 
      count=0 #so, for all other cases we need to keep a count.
      itr=self.head
      while itr:
         if count==index-1:
            node=Node(data,itr.next) #so, this node we are adding here is the new data that we wand to insert and its "itr.next" is the "itr.next" of the elelemt at index-1 (which means that, the element which came after the elelemt at index-1 will now be the next element if the newly added node or data)
            itr.next=node #which means that, now the new "itr.next" of the index-1 element is this new data we added just after the index-1 element 
            break #here we break the while loop once the condition is met.
         itr=itr.next
         count+=1
         
# 👇👇👇EXERCICES TO PRACTICE (ANSWERS ARE AVAILABLE ON THE GITHUB OF THE TUTOR OF "CODE BASICS" ... SEE IT IN T HE VIDEO ABOUT LINKED LISTS .. BUT TRY IT AFTER FIRST) 👇👇👇'''
   
##################################################################
  
   #FIRST EXERCICE:
   
   def insert_after_value(self,data_after,data_to_insert):
      if self.head==None:
         return
      if self.head.data==data_after:
         self.head.next=Node(data_to_insert,self.head.next)
         return
      itr=self.head
      while itr:
         if itr.data==data_after:
            itr.next=Node(data_to_insert,itr.next)
            break
         itr=itr.next
         
         # HERE 👇 IS THE CODE EXPLAINED IN MORE DETAILS AND HOW IT WORKS.
   
   def insert_after_value(self,data_after,data_to_insert):
      #we have first to search for first occurance of "data_after" value in linked list
      #Now insert "data_to_insert" after data_after node (try first, then look for the answer after in the description of the video by code basics)
      if self.head is None: #first we check if the list is empty or not, if it is empty, then we return empty (coz we cannot add a value after a value which does not exist)
         return
      if self.head.data==data_after: #then, if it is not , we verify if the data_after we provided is equal to our self.head.data. 
         self.head.next=Node(data_to_insert,self.head.next) #here we are now defining what is our node that will be inserted. if you noticed, now we are saying that, if the value that we are going to add another after it is equal to the data of the existing head, then we are going to insert the "data_to_insert" after it and the "next" of the "data_to_insert" will be the "next" of the head or the value after (since the condition is "when the self.head.data==data_after").
         return
      itr=self.head #here we iterate through our list when self.head is not equal to data_after
      while itr: #here we are just mensioning "if the self.head exist"
         
         if itr.data == data_after: #another condition (we gonna go deep)
               itr.next = Node(data_to_insert, itr.next)
               break
         itr=itr.next
         
###############################################################
      
   #SECOND EXERCICE:
   
   def remove_by_value(self,data):
      #remove first node  that contains data
      # i suggest you to review the above code before to attempt these exercices
      if self.head==None: #so, as usual we first check if the list is empty
         return
      if self.head.data==data: #then we chwck if the value we want to remove is the head of our list. if yes then..
         self.head=self.head.next # ... then we make its "next" the new head authomatically
         return
      
      itr=self.head #here, is the condition when we want to remove a value which is in the list but is not the head...
      while itr.next: # ... and we do that by itterating in the list (here we are going to use the itr to eliminate the itr.next when it is equal to our value we want to remove, then make the "next.next" of the itr into the new "next")
         if itr.next.data==data:
            itr.next=itr.next.next #here is where we delete the value by replacing it with its next
            break #then we break the loop
            
         itr=itr.next
   
   
   
   
   #THIRD EXERCICE: implementing a double linked list:
   
   
   
   
   
   
class Node:
   def __init__(self,data=None,next=None,prev=None):
      self.data=data
      self.next=next
      self.prev=prev
         
         #it is the same process as the prvious linked list, pass through the previous code before to start these questions please. FOR THESE ONES, TRY THEM LATER THEN FIND THE ANSWER IN THE DESCRIPTION OF THE VIDEO "LINKED LIST : CODE BASICS channel"
         
   # then implement these two methods: 
   def print_forward(self):
      #this method prints lists in forward direction. use node.next.
      pass
   
   def print_backward(self):
      #print linked list in reverse direction. use node.prev for this.
      pass
   
#‼️‼️ implement all other methods in regular linked list class and make necessary changes for doubly linked list (you need to populate node.prev in all those methods)
   
   
   
   
      
      
      
      
      
      
ll=LinkedList()
ll.insert_at_begining(34) #this will be the first element to be inserted in the linkedlist
ll.insert_at_begining(23) #this will be the second and will push the (34) value and become the head
ll.insert_at_begining(44) #then this will come and push the (23) and then become the head
ll.insert_at_begining(20) #then this (20) will be inserted at the beginning too and push the (44) and become the head. 
#notice that, for the "insert_at_begining" the one which is inserted after the other is the one which become the head (so it is aded at the beginning of the linked list)

ll.insert_at_end(100) #this will be the first one to be added at the end of our list
ll.insert_at_end(130) #the this will come and be addedd after the (100) and become the "next" of (100)
ll.insert_at_end(141) #then this will also come and become the "next" of (130) 
                      # NOTICE that, if we dont hadd any value after (141), then it does not have a "next" and then it is ponting at nothing "None"
#ll.insert_values(["babane ","mangue ","tomato ","garlic"]) #here, as we saw, we erased all the previous content of the previous linked lists and created a new one with the inputed content,


ll.insert_after_value(54.6,400)
ll.insert_after_value(400,400)
ll.remove_by_value(65)


ll.print()
length=ll.get_length()
print(f"the length is equal to {length} ")

ll.remove_at(2) #here we are now using our new module to remove an element at a specific index
# ll.remove_at(20)  or ll.remove_at(-1) ...  for these ones, we will reveive an error message or raise exception error message "invalid index" coz we created a condition for such cases if you remember ... 
ll.insert_at(1,"kwanga")  
ll.print() #then this function comes and print the linked list while itterating through all the values until it reaches the value which does not have another value in after it (in front of it)
length=ll.get_length()
print(f"the length is equal to {length} ") #now we print the length like this after weve already stored it into a variable to use it in a much easier way.




