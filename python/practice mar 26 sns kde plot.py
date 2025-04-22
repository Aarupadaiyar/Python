import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
#simple data
data = [1,2,2,3,3,4,5,5,7,8,6,6,9,9,10,10]
#create kde plot
sns.kdeplot(data, shade=True , color='blue')
plt.title("kernel density estimate (KDE) plot")
plt.xlabel("Value")
plt.ylabel("Density")
plt.show()
data = sns.load_dataset("iris")
d=pd.DataFrame(data)
print(d.head(10))
sns.kdeplot(d,x='sepal_length', y='sepal_width',shade=True,color='aquamarine')
plt.xlabel("Sepal Length")
plt.ylabel("Sepal Width")
plt.show()
sns.pairplot(d,hue='species')
plt.show()
