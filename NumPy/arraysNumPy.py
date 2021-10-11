import numpy as np
import math

# Arrays are displayed as a list or list of lists and can be created through list as well. When creating an
# array, we pass in a list as an argument in numpy array
a = np.array([1,2,3])
print('print a array',a)

# We can print the number of dimensions of a list using the ndim attribute
print('dimension: ',a.ndim)

# If we pass in a list of lists in numpy array, we create a multi-dimensional array, for instance, a matrix
b = np.array([[1,2,3],[4,5,6]])
print('multi-dimensional: ',b)

# We can print out the length of each dimension by calling the shape attribute, which returns a tuple
print('length of each dimension: ',b.shape)

# We can also check the type of items in the array
print('type of items in the array: ',a.dtype)

# Besides integers, floats are also accepted in numpy arrays
c = np.array([2.2, 5, 1.1])
print('type of items in numpy arrays: ',c.dtype.name)

print('print numpy array: ',c)

# Note that numpy automatically converts integers, like 5, up to floats, since there is no loss of prescision.
# Numpy will try and give you the best data type format possible to keep your data types homogeneous, which
# means all the same, in the array

# Sometimes we know the shape of an array that we want to create, but not what we want to be in it. numpy
# offers several functions to create arrays with initial placeholders, such as zero's or one's.
# Lets create two arrays, both the same shape but with different filler values
d = np.zeros((2,3))
print('array with zeros: ',d)

e = np.ones((2,3))
print('array with ones: ',e)

# We can also generate an array with random numbers
print('array with random numbers: ',np.random.rand(2,3))

# You'll see zeros, ones, and rand used quite often to create example arrays, especially in stack overflow
# posts and other forums.

# We can also create a sequence of numbers in an array with the arrange() function. The fist argument is the
# starting bound and the second argument is the ending bound, and the third argument is the difference between
# each consecutive numbers

# Let's create an array of every even number from ten (inclusive) to fifty (exclusive)
f = np.arange(10, 50, 2)
print('an array of every even number from ten (inclusive) to fifty (exclusive): ',f)

# if we want to generate a sequence of floats, we can use the linspace() function. In this function the third
# argument isn't the difference between two numbers, but the total number of items you want to generate
print('15 numbers from 0 (inclusive) to 2 (inclusive): ',np.linspace( 0, 2, 15 )) # 15 numbers from 0 (inclusive) to 2 (inclusive)

# Arithmetic operators on array apply elementwise.

# Let's create a couple of arrays
a = np.array([10,20,30,40])
b = np.array([1, 2, 3,4])

# Now let's look at a minus b
c = a-b
print(c)

# And let's look at a times b
d = a*b
print(d)

# With arithmetic manipulation, we can convert current data to the way we want it to be. With numpy I 
# could easily convert a number of farenheit values, say the weather forecase, to ceclius

# Let's create an array of typical Ann Arbor winter farenheit value

farenheit = np.array([0,-10,-5,-15,0])
print('farenheit: ',farenheit)
# And the formula for conversion is ((°F − 32) × 5/9 = °C)
celcius = (farenheit-32)*5/9
print('celcius: ',celcius)

print('celcius >-20',celcius>-20)

print('celcius%2: ',celcius%2==0)

# Besides elementwise manipulation, it is important to know that numpy supports matrix manipulation. Let's
# look at matrix product. if we want to do elementwise product, we use the "*" sign
A = np.array([[1,1],[0,1]])
B = np.array([[2,0],[3,4]])
print("matrix A: \n", A)
print('A shape: ',A.shape)
print("matrix B: \n",B)
print('matrix A*B: \n',A*B)

# if we want to do matrix product, we use the "@" sign or use the dot function
print(' matrix product: \n',A@B)