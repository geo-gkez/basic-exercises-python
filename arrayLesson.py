
# if name file as array you have errors !!!!!1


# import array as arr

# Efficient arrays of numeric values:
# https://docs.python.org/3/library/array.html


# First example

# from array import *

# vals = array('i',[5,9,8,4,2])

# print(vals)

# print(vals.buffer_info)


# Second example

from array import *


arr =array('i',[])

n = int(input("Enter the length of the array: "))

for i in range (n):
    x = int(input("Enter the next value: "))
    arr.append(x)

print(arr)

# manualy 

val = int(input("Enter the value for search: "))

k=0
for e in arr:
    if e==val:
        print(k)
        break
    k+=1
else:
    print("not found")


# use function

print(arr.index(val))