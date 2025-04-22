import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
#generating 2d 10x110 matrix of random no
data = np.random.randint(low=1,high=100,size=(10,10))
hm=sns.heatmap(data=data,annot=True)
plt.show()
"""
heatmap visually represents a matrix of values using color intensity .
since matrix is inherently 2d , sns.heatmap()
requires a 2d array to create a visualisation"""
