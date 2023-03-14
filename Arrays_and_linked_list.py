import numpy as np

lst = list(range(100))
print(lst)

#in this code we are importing the "numpy" library and we use one of its functions wich is list()
# here the output will be a list of numbrs from zero to 99, remember, for the list there are comas 
# separating the values, which is different from the array and we are going to see it soon
# This numpy library is very vast and can allow us to use many different relevant functions that we are going to explore with time

########################################################################

a = ['foo', 'bar', 'baz', 'qux', 'quux', 'corge']

print(a[-5:-3]) #here we can see that we can use nrgative indexes and that will work in the inverse
                # of normal positive indexes (here "corge" is at index [-1] and also index [5])
                # here the [-5:-3] specifies a range of values to be printed except the value at index  [-3]
array=np.array(a)
print(array.dtype)
print(array.shape)
sub_array=array[1:4].copy() #to copy and get a new array whic will be the slice of the previous one
                            #in the index range 1:4 where is 4 excluded

########################################################################

array = np.arange(100) 
print(array) #the output here will be an ARRAY ... and the first difference we can see between the list and the array is that the values in an array are not separated with a coma buy just an empty space

########################################################################

data = [2, 4,7.5, 8, 1]
array = np.array(data)
print(array) #here we are converting a list into an array. the np (is the library 'numpy' and np.array(data) means "convert data into array")
print(array.dtype) # here we want to print the data type of the array contents
print(array.shape) # this will print the number of elements in the array
print(array.ndim) # this will print the dimension of the vector (which is an array and we know that an array can be accessed as a vector and vectors have dimmensions ... a  vector of one row and "n" column is of dimmension 1, a vector of 2 or 3 or 4 or n+1 rows and many columns is a 2 dimension vector or array)

#########################################################################

data = [[2, 4,7, 8, 1], [23, 5, 9, 3, 9], [4, 10, 43, 12, 0]] #here we've created a list of lists and we want to convert it into an array (also, remember that it will be a matrix of two rows and 5 columns after)
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
#abd that is because with that expression we are comparing each element if the array2 matrix with the elements if the array matrix, if its greater than the output will be true

array_copy=array[4:7].copy() # this will copy the elements in the index range we choosed
print(array_copy) #this will print the sub_array we copied from the original one


array = np.arange(10)
print(array) #here the output will be a row matrix with one row and 10 colums with elements from 0 to 9
print(array[7]) #here also we xan use the index to licalize an element from the array
print(array[2:5]) #elements of index 2 to 5 with the fifth element excluded
array[6:8]=15 #herr we say that the elements from idex 6 to 8 exclided are going to be 15

################################################################################ 

array_slice=array[4:7]
print(array_slice) #here the output will be the sliced array that we took feom the main one using indexes
array_slice[2]=500 #the element at index 2 of the array_slice array will be equal to 500



################################################################################

array2d=np.array([[4,3,5,9,7],[9,4,5,2,6],[7,6,5,9,1]])
print(array2d[2][2])
print(array2d[2,2]) #these are the same and produce the same output which is the value locsted at the row of index 2 and the column of index two (5)




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


########

#more about linked list (frol a tutorial)

stock_prices=[235,654,879,345,888,769,871] #here is an array we create (we have to look first into arrays coz linked list are helping to solve the arrays problems and limitation)

stock_prices.insert(1,444)
# so here we are inserting the number 444 in the list at the index 1, which will push the e xisting numbers back to leavr a space for the inserted number

#here the array insertion complexity are of order of n or O(n).

#when we create an epmty list like "list=[] it alocate a memory space for that list, python lists are dynamic arrays and here is allocated a space capacity of 5 element " and when we start inserting (here we are appending, adding values to the end of the list) values in the list, the values are filling those spaces allocated for the list... when we added three values and we want to add another value but at the location of an existing value, it will puch the existing to make a space for the new value

#now lets imagine that our array is full of capacity (capacity is = 5 and all the five are filled), when we want to insert a new value.. the way dynamic array works now is, since it cannot use other values memory location, it will go in some area of the memory (RAM) then it will allocate more capacity and then will copy all those elements one by one, so if the initial capacity is 5, it will allocate additional 5*2 =10 (or additional capacity 5*2=10) memory locations... now there are 15 capacity or memory locations


#THIS IS NOT THAT EFFICIENT THO 😥

#lets imagine a structure where values are stored into different areas of memory (linked list) .. here we have the    "| value | next value adress |" 

# first, arrays store the value in contegious mem. location while this (linked list) is storing them into random memory locations which are linked with a pointer which point to the next adress  ... so the first value has a reference side to the adress of the next value or element ... those are the links we are creating here.

#here it become muc easier to insert a new value coz there is not a li,itation of capacity for the array... now we are not copying from one lication to another.

#here when we insert or delete element at the begining, the complexity is = O(1)  [this one is just because while inserting, its creating a node for the new element and the adress of the next element, so its iterating only once coz its the elements at the index 1]  and    when we want to insert or delete element at the end the complexoty is = O(n) because we have to iterate between all the elements of th list

#so, linked list has two main benefits over an array: 
# 1. you dont need to pre-allocate space and 2. insertion is easier

#there are also double linked-list (where its no longer |value adress |next address| but now its |previus adress| current value adress | next value adress) this allows to comeback easier, the backward traversal is easier .... the traversall of a list is O(n)

#the only advantage an array has is, if you know the index of the element in array on order of 1 (O(1)) ehich is a constant time operation.. so in array if you want to access the fifth element you just have to specify the index of the element into [] and it will go directly to it, bit for lnked list, ir has to go through all the elements to follow the links 

#inserting/deleting elements at start in array is O(n) cos u have to copy all the elements, but for linked list it is O(1) ,  you dont need to.add()

#inserting elements in the middle is O(n) for both.add()

#    IN PYTHON NOW 😃: !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

#lets create two classes:

class Node: 
   def __innit__(self,data=None,next=None): #this is the constructor of the Node class and has got two elements which construct the class (they are "data" and "next")
      self.data=data #this can contain integers, numbers, or complex objects
      self.next=next #this is a pointed to the next eelement
      #this "node"class represent a single element in the linked-list (it has two class members which are data and next)
      
class LinkedList: 
   def __innit__(self):
      self.head=None
      #this class is a class where we need a head variable which points to the head of the linked list (beginning)

#so now we start by adding a method (function called insert_at_begining)

   def insert_at_begining(self,data): #this is taking the data value and insert it at the beginning of the linked-list !!! THIS IS THE FIRST FUNCTION TO INSERT AT THE BEGINING OF A LINKED-LIST
      
      #LET US CREATE A NODE TO EXPLAIN HOW IT WORKS
      node= Node(data,self.head) #this "self.head" is taking the place of the "next" which is the pointer to the next value of the list and her the "self head is the first pointer"
      
      #just to make things easier,lets say there is an exiating head, when we add a new element(data), it will create a node where the "next" value will be the previous head which was pushed. (now it become the adress of the next value and the current value is now the new node we created)  here the self.head is now the adress of the next value (which was our head value before we inserted anoter at the front) 
      
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
         llstr+=str(itr.data) + '-->' #so here the data which is being itterated will be stored in llstr then we go to the next value ( <-- : this is the direction of itteration)
            #the '-->' is just to show the link (it can be removed without problem 😊)
         itr=itr.next #here we say, now since there are an existing head, that head will become the "next" of the new "self.head =  the new value... so the itr become itr.next (next of the self.head or the new head) remember that it is like that coz we stored the self.head in itr (we stored the already exiating one in itr so that we can easily transform it into the "next" or the adress of the next value)
            
            #anoher way to undrstand it very well is that, while printing, it will start by the last value in the list, verify if it is a head, then turn it into the "next" adress of the coming value to be analised by the printing function... for it, it will be iterrated and become the "next" then we go to the other value (from right to left <-- ) and keep itterating until it reaches the last value to see if there is a head which keep existing after the value we are at, if there is not any value, then the while loop is broken (no head existing after the value we are at so it cannot make the current value the "next" adress of a non existing value)
            
            #WE ARE ITTERATING THROUGH ELEMENTS ONE BU ONE (dirrection: <-- )
            #and for each itteration, the value that is made "next" will be printed after being itterated (and that will make our output)
      print(llstr) #here, after the loop was broken, we print the linked list with the added elements #!!! SO NOW, TO CHECK THIS, WE HAVE TO CREATE A LINKED LIST NAME TO BE USED IN THE PRINTING PROCCESS!!!
         
         #NOW WE ARE TRYING TO INSERT AND PRINT THE LINKED LIST
         #THERE IS A SMALL PROBLEM WITH THE PROGRAM THAT WE ARE GOING TO FIND OUT SOON BUT FOR NOW, THIS IS HOW THE CODE IS SUPPOSED TO E WRITEN and printed
if __name__=='__main__':
   ll=LinkedList()
   ll.insert_at_begining(4)
   ll.insert_at_begining(6)
   ll.insert_at_begining(54)
   ll.insert_at_begining(88)
   ll.print()
