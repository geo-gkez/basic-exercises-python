import pandas as pd

df = pd.read_csv("presidents.csv")
# print(df.head())

def splitname(row):
    row['First']=row['President'].split(" ")[0]
    row['Last']=row['President'].split(" ")[-1]
    return row 

df = df.apply(splitname, axis='columns')
print(df.head())

# delete columns First and Last
del(df['First'])
del(df['Last'])
print("#####################################################")
print("#####################################################")

pattern="(^[\w]*)(?:.* )([\w]*$)"

print(df["President"].str.extract(pattern).head())
print("#####################################################")
print("#####################################################")
pattern="(?P<First>^[\w]*)(?:.* )(?P<Last>[\w]*$)"

# Now call extract
names=df["President"].str.extract(pattern).head()
print(names)

print("#####################################################")
print("#####################################################")
df["First"]=names["First"]
df["Last"]=names["Last"]
print(df.head())

print("#####################################################")
print("#####################################################")

df["Born"] = df["Born"].str.extract("([\w]{3} [\w]{1,2}, [\w]{4})")
print(df["Born"].head())

print("#####################################################")
print("#####################################################")

df["Born"]=pd.to_datetime(df["Born"])
print(df["Born"].head())