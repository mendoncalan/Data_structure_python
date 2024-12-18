import array

# Array object will be created which contains the metadata
# such as Datatype of elements and legth of the array
my_array =array.array('i')
print(my_array)

# Suppose we want the list of element to be added to an array
my_array1 =array.array('i',[1,2,3,4])
print(my_array1)

#Creating a empty Array using Numpy lib
import numpy as np

np_array =np.array([],dtype=int)
print(np_array)

