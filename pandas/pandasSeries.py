import pandas as pd
import numpy as np
import timeit


students_classes = {'Sonja': 'Physics',
                   'Tonia': 'Maths',
                   'kaiti': 'English',
                   'Sam': 'Geography'}
s = pd.Series(students_classes)
# print(s)

print("fourth entry(s[3]): ",s[3])
print("fourth entry(s.iloc[3]): ",s.iloc[3])
print("What class Tonia has(s['Tonia']): ",s['Tonia'])
print("What class Tonia has(s.loc['Tonia']): ",s.loc['Tonia'])

print("##########################################")
print("##########################################")
print("##########################################")

class_code = {99: 'Physics',
              100: 'Maths',
              101: 'English',
              102: 'Geography'}
s = pd.Series(class_code)
# print("s[0] ",s[0])
print("s[99] ",s[99])

print("##########################################")
print("##########################################")
print("##########################################")
grades = pd.Series([90, 80, 70, 60])
print("grades: ",grades)
total = 0
for grade in grades:
    total+=grade
print("average of grades(works but it is slow): ",total/len(grades))

print("##########################################")
print("##########################################")
print("##########################################")
# randint: 10000 numbers between 0 - 1000 
numbers = pd.Series(np.random.randint(0,1000,10000))
print(numbers.head())
print("len(numbers): ",len(numbers))
print("##########################################")
print("##########################################")
print("##########################################")

# https://docs.python.org/3/library/timeit.html
mysetup = "import numpy as np"
mycode = """ 
def example():
        numbers = pd.Series(np.random.randint(0,1000,10000))
        total = 0
        for number in numbers:
            total+=number

        total/len(numbers)

"""

# timeit statement
print (timeit.timeit(setup = mysetup,
                     stmt = mycode,
                     number = 10000))
mysetup2 = "import pandas as pd; import numpy as np"

mycode2 = """ 
def example():
        numbers = pd.Series(np.random.randint(0,1000,10000))
        total = np.sum(numbers)
        total/len(numbers)

"""

# timeit statement
print (timeit.timeit(setup = mysetup2,
                     stmt = mycode2,
                     number = 10000))

print("##########################################")
print("##########################################")
print("##########################################")

print(numbers.head())
# print("at::: ",numbers.at[0])
# numbers.at[0]=200
# print(numbers.head())
# numbers+=2
# print(numbers.head())

# We can use the iteritems() function which returns a label and value 
for label, value in numbers.iteritems():
    # now for the item which is returned, lets call at()
    numbers.at[label]=value+2
# And we can check the result of this computation
print(numbers.head())


print("##########################################")
print("##########################################")
print("##########################################")

s = pd.Series(np.random.randint(0,1000,1000))
# And we'll just rewrite our loop from above.
for label, value in s.iteritems():
    s.loc[label]= value+2

s = pd.Series(np.random.randint(0,1000,1000))
# And we just broadcast with +=
s+=2


print("##########################################")
print("##########################################")
print("##########################################")

# Here's an example using a Series of a few numbers. 
s = pd.Series([1, 2, 3])

# We could add some new value, maybe a university course
s.loc['History'] = 102
print(s)

print("##########################################")
print("##########################################")
print("##########################################")
# append
students_classes = pd.Series({'Sonja': 'Physics',
                   'Tonia': 'Maths',
                   'kaiti': 'English',
                   'Sam': 'Geography'})
kelly_classes = pd.Series(['Philosophy', 'Arts', 'Math'], index=['Kelly', 'Kelly', 'Kelly'])

all_students_classes = students_classes.append(kelly_classes)
print(all_students_classes)