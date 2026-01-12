import pandas as pd
import os

data = { "name": ["Default User", "Alice", "Bob"], 
        "username": ["default@example.com", "alice@mail.com", "bob@mail.com"], 
        "password": ["12345", "alicepwd", "bobpwd"], 
        "loggedin": [False, True, False]
        }

df = pd.DataFrame(data)
# print(f"My data is :\n {df}")

# Add a row in the dataframe
new_row = ['Moumita', 'palitmoumita5@gamil.com', 'mou', 'False']
df.loc[len(df.index)] = new_row


dir = 'data'
os.makedirs(dir, exist_ok= True)

file_path = os.path.join(dir, 'sample_data.csv')
df.to_csv(file_path, index = False)
