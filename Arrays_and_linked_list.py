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

data = [[2, 4,7.5, 8, 1], [23, 5, 9, 3, 9]] #here we've created a list of lists and we want to convert it into an array (also, remember that it will bea matrix of two rows and 5 columns after)
array = np.array(data) #here is the conversion code of the list called "data"
print(array.shape) # here we will print the number of rows and columns (row,columns)
print(array.ndim) #here we will print the dimmension of the matrix (we have two rows and 5 columns so its a 2 dimension matrix (here its an array which acts like a matrix))

