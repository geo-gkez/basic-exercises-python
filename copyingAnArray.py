from numpy import *
# sum arrays:

arr1 = array([1,2,3,4,5])
arr2 = array([4,3,2,1,0])

arr = arr1 +arr2

print(arr)

print(cos(arr))
print(log(arr))
print(max(arr))
print(concatenate([arr1,arr2]))

# they saved once (shallow copy)
arr2 = arr1
print(id(arr1))
print(id(arr2))

# if i change a value
arr1[1]=10
print(arr1)
print(arr2)

# use view() (shallow copy)
arr2=arr1.view()
print(id(arr1))
print(id(arr2))

# if i change a value
arr1[1]=50
print(arr1)
print(arr2)


# use copy() (deep copy)
arr2=arr1.copy()
print(id(arr1))
print(id(arr2))

# if i change a value
arr1[1]=100
print(arr1)
print(arr2)

