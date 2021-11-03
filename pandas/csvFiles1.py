import pandas as pd

# df = pd.read_csv('teachers.csv')
# print(df.head())

df = pd.read_csv('teachers.csv',index_col=0)
# print(df.head())

# print(df.columns)

# change columns

# cols = list(df.columns)
# cols = [x.lower().strip() for x in cols]
# df.columns=cols
# print(df.columns)

df.columns = [x.lower().strip() for x in df.columns]

print(df.columns)

moria_mask=df['μορια πινακα'] > 50

print(moria_mask)
print(df.where(moria_mask))
print(df.where(moria_mask).dropna())
print("########################################")
print("########################################")
print("########################################")
print((df['μορια πινακα'] > 50) & (df['περιφερεια'] == 'ΑΤΤΙΚΗΣ') )
print("########################################")
print("########################################")
print("########################################") 
print(df['μορια πινακα'].gt(0.7) & df['περιφερεια'].eq('ΑΤΤΙΚΗΣ'))