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

########################################################################