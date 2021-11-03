import pandas as pd

df = pd.read_csv('census.csv')
# print(df.head())
print(df['SUMLEV'].unique())

df = df[df['SUMLEV'] == 50]
print(df.head())
print('##############################################')
print('##############################################')
print('##############################################')
print()
columns_to_keep = ['STNAME','CTYNAME','BIRTHS2010','BIRTHS2011','BIRTHS2012','BIRTHS2013',
                   'BIRTHS2014','BIRTHS2015','POPESTIMATE2010','POPESTIMATE2011',
                   'POPESTIMATE2012','POPESTIMATE2013','POPESTIMATE2014','POPESTIMATE2015']
df = df[columns_to_keep]
print(df.head())
print('##############################################')
print('##############################################')
print('##############################################')
print()
df = df.set_index(['STNAME','CTYNAME'])
print(df.head())
print('##############################################')
print('##############################################')
print('##############################################')
print()
print(df.loc['Michigan','Washtenaw County'])
print('##############################################')
print('##############################################')
print('##############################################')
print()
print(df.loc[ [('Michigan', 'Washtenaw County'),
         ('Michigan', 'Wayne County')] ])