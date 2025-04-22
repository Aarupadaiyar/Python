import pandas as pd
import numpy as np
a=np.arange(24).reshape(2,3,4)
print(a)
"""Dataframes are important data structure that exist in pandas
similar to matrix row and column
and it is two dimension
Series is 1dimension"""
x=pd.DataFrame([[1,2,3,4],
                [5,6,7,8],
                [9,10,11,12]])
print(x)
b=pd.Series([23,34,45,56])
print(b)
b=pd.Series([23,34,45,56],index=["a","b","c","d"])
print(b)
#to fetch particular element in panda library
"""print(b["c"])
print(b[2])"""
#this above method fetch warning
#but to fetch particular element this is recommended
#array.loc for manipulated index
print(b.loc["c"])
#array.iloc for index
print(b.iloc[2])
c=pd.Series([34,45,56,67],index=["a","b","c","d"])
print(b+c)
s={"a": 12,"b": 23,"c": 34,"d": 45,"e": 56,"f": 67}
d=pd.Series(s)
e=pd.Series(s,index=["b","c","f"])
print(d+e)
#NAN is float value
s5=pd.Series([1000,1000,1000,1000],index=["a","b","c","d"])
print(s5)
print(d+s5)
#Initialising with Scalar points
m=pd.Series(42,["life","universe","everything"])
print(m)
n=pd.Series([2,3,4,5],["a","b","c","d"])
print(n)
import matplotlib.pyplot as plt
temp = [4.4,5.5,6.6,7.7,8.8,1.1,2.2,3.3]
s7=pd.Series(temp,name="temperature")
s7.plot()
plt.show()
