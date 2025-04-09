print("learning DVC")

import pandas as pd
import os

my_data = {
        'name':['ayush','piyush'],
        'age':[19,16],
        'occu':['ml engineer','student']
        }

data = pd.DataFrame(my_data)
print(data)

mydir = 'DataDir'
os.makedirs(mydir,exist_ok=True)

filePath = os.path.join(mydir,'trial.csv')
data.to_csv(filePath,index=False)
print(f"Created the file to {filePath}")
print('\n')

df = pd.read_csv(filePath)
print('Printing df just for assurance')
print(df)
