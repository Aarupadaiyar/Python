import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
# line plot is most popular plot to draw a relationship between x and y
data =[30,21,29,28]
#df=pd.DataFrame(data)
sns.lineplot(data)
plt.show()
dat={'Name':['Mohe','Karnal','Yrik','Jack'],'Age':[30,21,29,20]}
#df = pd.DataFrame(dat)
#sns.lineplot(x=df['Name'],y=df['Age'])
sns.lineplot(x='Name',y='Age',data=dat)
plt.title('Seaborn Lineplot')
plt.show()
#sns.lineplot(df['Age'])
#plt.show()
data = {'weight':[45.5,67.5,33.5,76.5],'Age':[30,29,26,22]}
