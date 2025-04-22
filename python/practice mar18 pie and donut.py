import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

y=np.array([35,25 , 25,25])
mylabels = ["Apples","Bananas","Cherries","Dates"]
plt.pie(y, labels =mylabels ,startangle = 90 , radius = 1)
z=np.array([1])
plt.pie(z,colors='w',radius =0.5)
#myexplode = [0.4,0,0,0]
#plt.pie(y, labels = mylabels , explode = myexplode , shadow = True)
#plt.show()
plt.show()
