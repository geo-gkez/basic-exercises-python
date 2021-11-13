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

print("#############################################")
print()

# inner
inner_merge=pd.merge(staff_df,student_df,how='inner',left_index=True,right_index=True)
print(inner_merge)

print("#############################################")
print()
# left join
left_join_merge=pd.merge(staff_df,student_df,how='left',left_index=True,right_index=True)
print(left_join_merge)

print("#############################################")
print()
# right join
right_join_merge=pd.merge(staff_df,student_df,how='right',left_index=True,right_index=True)
print(right_join_merge)

print("#############################################")
print()

staff_df=staff_df.reset_index()
student_df=student_df.reset_index()

merge_with_on=pd.merge(staff_df,student_df,how='right',on='Name')

print(merge_with_on)
print("#############################################")
print()