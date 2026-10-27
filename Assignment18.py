# to print only two columns
import pandas as pd

dic = {'Name':['Anil','Niraj','Soman','Nisha'],
       'Age':[18,19,17,18],
       'Address':['Pune','Jaipur','Delhi','Kolkata']}
df = pd.DataFrame(dic)
print(df[['Name','age']])
