import pandas as pd
import numpy as np
my_df=pd.DataFrame([
    ["biking",78,1985,np.nan],
    ["Dancing",99,1987,3]],
                   columns=["hobby","weight","birthyear","children"],
                            index=["alex","bob"])
print(my_df)
"""Data frame
operation on data frames
creating csv files
operation on csv files
"""
df=pd.read_csv("data.csv")
#to load or read csv file
#df=df.to_csv("Name of the file")
#Save the csv file we creted
"""Handling missing elements in a file : 3 method:
1.deleting the whole column:
.dropna()
#this will not manipulate original dataframe
instead it create new dataframe with changes we made
2.replace the missing value:
.fillna(value)
inplace method
this inplace=True is used to do above method without creating new dataframe
3.mean function
df.isnull().sum()
is used to count number of null value row
"""
print(df.isnull().sum())
#used to give sum of null elements
ndf=df.dropna()
print(ndf.isnull().sum())
print("...................................")
print(df.isnull().sum())
print(ndf)
print("...................................")
df.dropna(inplace = True)
print(df.isnull().sum())
print(df)
df= pd.read_csv("data.csv")
df.fillna(130, inplace=True)
print(df.isnull().sum())
df.to_csv("filled.csv")
