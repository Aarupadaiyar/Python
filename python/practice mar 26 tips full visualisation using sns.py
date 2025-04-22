import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
data=pd.read_csv('tips-1.csv')
print(data.head(10))
#Lineplot 1
sns.lineplot(data , x = 'tip' , y = 'size' , color= 'yellow')
plt.show()
#Groupby function
ag=data.groupby('day')['tip'].sum()
sns.barplot(ag)
plt.show()
#when you use groupby data it became series so you must use index and values as x and y
sns.barplot(data=data,x='day',y='tip')
plt.show()
#Barplot
sns.barplot(ag)
plt.show()
#lineplot 2
sns.lineplot(data,x='sex',y='tip',color='purple')
plt.show()
#histogram
sns.histplot(data['total_bill'],bins=5)
plt.show()
#countplot
sns.countplot(data["day"])
plt.show()
#scatterplot
sns.scatterplot(data=data, x='day' , y='tip',hue='sex')
plt.show()
#pairplot
sns.pairplot(data,hue='sex')
plt.show()
#boxplot
sns.boxplot(data=data['total_bill'])
plt.show()
