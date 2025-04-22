import pandas as pd
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
