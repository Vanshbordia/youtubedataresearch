import requests
import pandas as pd
import os  
df=pd.read_csv('Dataset1_clean.csv')
print(df.iloc[1,14])
print(df.iloc[1,15])

for i in range(len(df)):
    img_data = requests.get(df.iloc[i,14]).content
    with open("./d1_img/"+df.iloc[i,15]+".jpg", 'wb') as handler:
        handler.write(img_data)
