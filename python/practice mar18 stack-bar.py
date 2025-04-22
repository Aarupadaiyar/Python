import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
x= ['India','Britain','china','USA']
y1=[10,20,10,30]
y2=[20,25,15,25]
plt.bar(x,y1,color='r')
plt.bar(x,y2,bottom=y1,color='b')
plt.show()
X=['India','Britain','China','USA']
y1=np.array([10,20,10,30])
y2=np.array([20,25,15,25])
y3=np.array([12,15,19,6])

y4=np.array([10,29,13,19])
plt.bar(x,y1,color='r')
plt.bar(x,y2,bottom=y1,color='b')
plt.bar(x,y3,bottom=y1+y2,color='g')
plt.bar(x,y4,bottom=y1+y2+y3,color='y')
plt.xlabel("Country")
plt.ylabel("Sale")
plt.legend(['product 1','product 2','product 3','product 4'])
plt.title("Sales by countries")
plt.show()
df = pd.DataFrame([['India',10,20,30,16],['Britain',20,25,15,21],
                   ['China',12,15,19,6],['Usa',10,18,11,19]],
                  columns=['Country','product 1 ','product 2','product 3 ','product 4 '])
print(df)
df.plot(x='Country',kind='bar',stacked=True,
        title='Stacked bar graph by data frame')

plt.show()
