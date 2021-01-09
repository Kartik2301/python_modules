import pandas as pd

# read csv
df = pd.read_csv('pokemon_data.csv')

# read excel
df_xlsx = pd.read_excel('pokemon_data.xlsx')

# read file in tab separated format
df_tab_separated = pd.read_csv('pokemon_data.txt',delimiter='\t')

# reading data

# 1. read headers

print(df.columns)

# 2. read each column

print(df['Name'])
print(df[['Name','Speed','HP']])

# 3. print a particular row

print(df.iloc[1])
print(df.iloc[0:4])

# 4. Read a specific location

print(df.iloc[2,1])

"""
for index,row in df.iterrows():
    print(index,row['Name'])
"""

print(df.loc[df['Type 1'] == "Fire"])

print(df.describe())

print(df.sort_values('Name', ascending=False))
print(df.sort_values(['Type 1', 'HP']))
print(df.sort_values(['Type 1', 'HP'], ascending=[1,0]))

# adding a column
#df['Total'] = df.iloc[:,4:10].sum(axis=1)
#df.drop(columns=['Total'], inplace=True)

#cols = list(df.columns.values)
#df = df[cols[0:4] + [cols[-1]] + cols[4:len(cols)-1]]
#print(df.head())

#df.to_csv('modified.csv', index=False)
#df.to_excel('modified.xlsx',index=False)
#df.to_csv('modified.txt',index=False,sep='\t')

# Filtering data
#new_df = df.loc[(df['Type 1'] == 'Grass') & (df['Type 2'] == 'Poison') & (df['HP'] > 70)]
#new_df = new_df.reset_index(drop=True)
#print(new_df)

"""
regex_df = df.loc[df['Name'].str.contains('Mega')]
regex_df = df.loc[~df['Name'].str.contains('Mega')]
print(regex_df.head())
"""

"""
import re
regex_df = df.loc[df['Type 1'].str.contains('fire|frass', flags = re.I, regex=True)]
start_regex = df.loc[df['Name'].str.contains('^pi[a-z]*', flags=re.I,regex=True)]
print(start_regex.head())
"""

# Conditional changes

#df.loc[df['Type 1'] == 'Fire', 'Type 1'] = 'Flamer'
#df.loc[df['Type 1'] == 'Fire', 'Legendary'] = True
#df.loc[df['Total'] > 500, ['Generation', 'Legendary']] = ['TEST VALUE 1', 'TEST VALUE 2']
#print(df.head())

# Aggregate statistics

#df = pd.read_csv('modified.csv')
#df = df.groupby(['Type 1']).mean().sort_values('Defense', ascending=False)
#df = df.groupby(['Type 1', 'Type 2']).count()
#print(df)

# Working with large datasets
# load 5 rows at a time
#new_Df = pd.DataFrame(columns=df.columns)
"""
for df in pd.read_csv('modified.csv', chunksize=5):
    results = df.groupby(['Type 1']).count()
    new_Df = pd.concat([new_Df, results])
"""
#print(new_Df)
