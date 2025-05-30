import pandas as pd

df = pd.read_excel('input_table.xlsx')
pd.set_option('display.max_columns', None)      # Display every column
print(df)

print('COLUMNS:')
print(df.columns)

unique_id = df[['Unique ID']]
print(unique_id.columns)

df = df.iloc[:, 10:]
df = pd.concat([unique_id, df], axis = 1)     # Keeping columns that contain valuable information plus id of taker of survey
print(df)

_dict = {}
for elem in df['Q11 - Which Country do you live in?']:
    if elem in _dict:
        _dict[elem] += 1
    else:
        _dict[elem] = 1
print(list(_dict.values()))

sum = 0
for elem in list(_dict.values()):
    if elem >= 5:
        sum += 1
print(sum)

print(df['Q9 - Male/Female?'].value_counts())
print(df['Q9 - Male/Female?'])

print(df['Q12 - Highest Level of Education'].value_counts())
print(df['Q12 - Highest Level of Education'])

pd.set_option('display.max_rows', None)      # Display every column
for elem in df.columns:
    print(df[elem].value_counts())

# df.loc[df['Q1 - Which Title Best Fits your Current Role?'] == 'Other (Please Specify):Analytics Consultant', 'Q1 - Which Title Best Fits your Current Role?'] = 0
# print(df)

print('DATABASE:')
print(df)

print(df['Q1 - Which Title Best Fits your Current Role?'].value_counts())
df['Q1 - Which Title Best Fits your Current Role?'] = df['Q1 - Which Title Best Fits your Current Role?'].apply(lambda x: 'Data Analyst' if 'analy' in x.lower() else ('Other' if 'other' in x.lower() else x))
print(df['Q1 - Which Title Best Fits your Current Role?'].value_counts())

lookup_q4 = df['Q4 - What Industry do you work in?'].value_counts()
print(lookup_q4)
df['Q4 - What Industry do you work in?'] = df['Q4 - What Industry do you work in?'].apply(lambda x: x if lookup_q4[x] >= 5 else 'Other')
print(df['Q4 - What Industry do you work in?'].value_counts())

print(df['Q5 - Favorite Programming Language'].value_counts())
df['Q5 - Favorite Programming Language'] = df['Q5 - Favorite Programming Language'].apply(lambda x: 'SQL' if 'sql' in x.lower() else ('Other' if 'other' in x.lower() else x))
print(df['Q5 - Favorite Programming Language'].value_counts())

print(df)

lookup_q11 = df['Q11 - Which Country do you live in?'].value_counts()
print(lookup_q11)
df['Q11 - Which Country do you live in?'] = df['Q11 - Which Country do you live in?'].apply(lambda x: x if lookup_q11[x] >= 5 else 'Other')
print(df['Q11 - Which Country do you live in?'].value_counts())

df.to_excel("output_table.xlsx",
             sheet_name='Sheet_1')