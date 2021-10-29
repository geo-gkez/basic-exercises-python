import pandas as pd


record1 = pd.Series({'Name': 'Sonja',
                        'Class': 'Physics',
                        'Score': 85})
record2 = pd.Series({'Name': 'Tonia',
                        'Class': 'Chemistry',
                        'Score': 82})
record3 = pd.Series({'Name': 'Helen',
                        'Class': 'Biology',
                        'Score': 90})

# Like a Series, the DataFrame object is index. Here I'll use a group of series, where each series 
# represents a row of data. Just like the Series function, we can pass in our individual items
# in an array, and we can pass in our index values as a second arguments
df = pd.DataFrame([record1, record2, record3],
                  index=['school1', 'school2', 'school1'])
# print(df.head())

# An alternative method

students = [{'Name': 'Sonja',
              'Class': 'Physics',
              'Score': 85},
            {'Name': 'Tonia',
             'Class': 'Chemistry',
             'Score': 82},
            {'Name': 'Helen',
             'Class': 'Biology',
             'Score': 90}]

df = pd.DataFrame(students, index=['school1', 'school2', 'school1'])

print(df.head())
print("#################")
print(df.loc['school2'])
print("#################")
print(df.loc['school1'])
print("#################")
print("type of school2",type(df.loc['school2']))
print("type of school1",type(df.loc['school1']))
print("#################")
print(df.loc['school1','Name'])
print("#################")
print(df.T)
print("#################")
print(df.T.loc['Name'])
print("#################")
print(df['Name'])
print("#################")
print(df.loc[:,['Name','Score']])
print("#################")
# The drop function returns a copy of the DataFrame with the given rows removed
print(df.drop('school1'))
print("#################")
print(df)
print("#################")
copy_df = df.copy()
# drop the name column in this copy
copy_df.drop("Name",inplace=True,axis=1)
print(copy_df)
print("#################")
# use del for dropping data
del copy_df['Class']
print(copy_df)
# add new column
print("#################")
df['Ranking'] = None
print(df)