import pandas as pd
import numpy as np
df2=pd.read_csv("employee_data.csv")
print(df2)
print(df2.info())
print(df2.head())
print(df2.tail(n=2))
print(df2.describe())
print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
data=pd.read_csv("data.csv")
print(data.isnull().sum())
print(data.dropna(inplace=True))
#print(data.fillna(inplace=True))
print(data.isnull().sum())
print(data.mean())
print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
d=pd.read_csv("data.csv")
print(d.isnull().sum())
x=d["Calories"].median()
print(x)
null_rows=d
d["Calories"]=d["Calories"].fillna(x)
print(d)
