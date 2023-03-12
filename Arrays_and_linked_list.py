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
print(first.data)
print(first.next)