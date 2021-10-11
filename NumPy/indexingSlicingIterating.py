import numpy as np
import math

a = np.array([1,3,4,5,7])
print('a[3]: ',a[3])

a = np.array([[1,2], [3, 4], [5, 6]])
print('multi-dimensional array: ',a)

print('a[2,1]: ',a[2,1])

print('get multiple elements: ',np.array([a[0, 0], a[1, 1], a[2, 1]]))

# we can also do that by using another form of array indexing, which essentiall "zips" the first list and the
# second list up
print('another form of array indexing: ',a[[0, 1, 2], [0, 1, 1]])

print('bollean a>5: ',a >5)

print('array relating to the true values: ',a[a>5])


a = np.array([0,1,2,3,4,5])
print(a[:3])

print(a[2:4])

a = np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12]])
print(a)

print(a[:2])
print(a[:2, 1:3])

# It is important to realize that a slice of an array is a view into the same data. This is called passing by
# reference. So modifying the sub array will consequently modify the original array

# Here I'll change the element at position [0, 0], which is 2, to 50, then we can see that the value in the
# original array is changed to 50 as well

sub_array = a[:2, 1:3]
print("sub array index [0,0] value before change:", sub_array[0,0])
sub_array[0,0] = 50
print("sub array index [0,0] value after change:", sub_array[0,0])
print("original array index [0,1] value after change:", a[0,1])