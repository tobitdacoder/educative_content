import numpy as np
lst = list(range(100))
print(lst)

#in this code we are importing the "numpy" library and we use one of its functions wich is list()
# 

########################################################################

a = ['foo', 'bar', 'baz', 'qux', 'quux', 'corge']

print(a[-5:-3]) #here we can see that we can use nrgative indexes and that will work in the inverse
                # of normal positive indexes (here "corge" is at index [-1] and also index [5])
                # here the [-5:-3] specifies a range of values to be printed except the value at index  [-3]

########################################################################

array = np.arange(100)
print(array)