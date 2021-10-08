from numpy import *

# # arr = array([1,2,3,2,5,4],float)

# # (start,final,parts)
# arr0 = linspace(0,15,16)

# # (start,final,gap)
# arr1 = arange(0,15,2)

# # values of log
# arr2 = logspace(0,40,5)
# #print('%.2f' %arr[4])

# # (size,format)
# arr = zeros(5,int)

# print(arr.dtype)
# print(arr)

###############################################

arr1 = array([
    [1,2,3,4,5,6],
    [4,5,6,7,8,9]
])


print("########################")
print("########################")
print("########################")
print(arr1)
print(arr1.ndim)
print(arr1.dtype)
print(arr1.shape)
print(arr1.size)

arr2 = arr1.flatten()
print("########################")
print("########################")
print("########################")
print(arr2)

arr3 = arr2.reshape(3,4)
print("########################")
print("########################")
print("########################")
print(arr3)

arr4 = arr2.reshape(2,2,3)

print("########################")
print("########################")
print("########################")
print(arr4)

print("########################")
print("########################")
print("########################")
m1 = matrix(arr1)
print(m1)

print("########################")
print("########################")
print("########################")
m2 = matrix('1 2 3; 6 4 5; 1 6 7')
print(m2)
print("########################")
print("########################")
print("########################")
print(m2.max())
print("########################")
print("########################")
print("########################")
m3 = matrix('1 2 3; 6 4 5; 1 6 7')
m4 = matrix('1 2 3; 6 4 5; 1 6 7')
m5 = m3+m4
print(m5)