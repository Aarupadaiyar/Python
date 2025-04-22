import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
data={'weight': [45.5,67.4,33.5,76.5,55.5,87.4,23.5,86.5], 'Age':[30,21,29,28,34,56,65,48]}
#df=pd.DataFrame(data)
#sns.scatterplot(x=df['Age'],y=df['weight']}
sns.scatterplot(x='Age',y='weight',data=data)
plt.show()
data={'weight': [45.5,67.4,33.5,76.5,55.5,87.4,23.5,86.5], 'Age':[30,21,29,28,34,56,65,48]}
df=pd.DataFrame(data)
sns.boxplot(data['Age'])
plt.show()
data=pd.DataFrame({'Category':['A','B','C','D','E'],'values':[3,7,2,5,4]})
sns.barplot(x=data['Category'],y=data['values'])
plt.title('Sea born Bar plot')
plt.show()
data=np.random.randn(1000)
print(data)
sns.histplot(data,bins=30,kde=True)
plt.title('Seaborn Histogram')
plt.show()
