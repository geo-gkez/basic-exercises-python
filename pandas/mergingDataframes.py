import pandas as pd


staff_df = pd.DataFrame([{'Name':'Sonja','Role':'Boss'},
                         {'Name':'Tonia','Role':'Director'},
                         {'Name':'George','Role':'ball-boy'}
])

staff_df=staff_df.set_index('Name')

student_df = pd.DataFrame([{'Name': 'George', 'School': 'Business'},
                           {'Name': 'Tonia', 'School': 'Law'},
                           {'Name': 'Sally', 'School': 'Engineering'}])

student_df = student_df.set_index('Name')

# print(staff_df.head())
# print(student_df.head())

# outer join (union)
merge=pd.merge(staff_df,student_df,how='outer',left_index=True,right_index=True)
print(merge)