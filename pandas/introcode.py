import pandas as pd

# call the Series function in pandas and pass in the students
students = ['Sonja','George','Tonia']

print(pd.Series(students))

numbers = [1,2,3]

print(pd.Series(numbers))

# use None 
students = ['Sonja','George',None]
print(pd.Series(students))

numbers = [1,2,None]

print(pd.Series(numbers))
print("############################")
print("############################")
print("############################")

# use dictionaries and tuples
students_scores={'Sonja':'Physics',
                    'Tonia':'Maths',
                    'George':'Chemistry'}
s = pd.Series(students_scores)
print(s)
print(s.index)

students = [("Sonja","Theof"),("Tonia","Pap"),("Geo","Gkez")]
print(pd.Series(students))

s = pd.Series(['Physics','Maths','Chemisty'],index=['Sonja','Tonia','George'])
print(s)

s=pd.Series(students_scores,index=['Sonja','Tonia','Mike'])
print(s)