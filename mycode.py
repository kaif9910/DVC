import pandas as pd
import os

# create a samples dataframe with column names 

data = {'name': ['alice', 'bob', 'charlie'],
        'age': [25,30,35]}

df = pd.DataFrame(data)

# adding new row to df for v2

new_row_loc = {'name':'GF1', 'age': 20, 'city': 'city1'}

df.loc[len(df.index)] = new_row_loc

# adding new row to df for vs

new_row_loc2 = {'name':'GF2', 'age': 20, 'city': 'city2'}
df.loc[len(df.index)] = new_row_loc2

new_row_loc3 = {'name':'GF3', 'age': 20, 'city': 'city3'}
df.loc[len(df.index)] = new_row_loc3

data_dir = 'data'

os.makedirs(data_dir, exist_ok=True)

# define the file path

file_path = os.path.join(data_dir, 'sample_data.csv')

# save the dataframe to a csv file , including column names


df.to_csv(file_path , index= False)

print(f'csv file saved to {file_path}')
