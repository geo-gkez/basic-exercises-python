import pandas as pd

df = pd.read_csv('grades.csv')
print(df.head(10))

mask = df.isnull()

print(mask.head(10))
print()
print(df.dropna().head(10))
print()
df.fillna(0,inplace=True)
print(df.head(10))