import numpy as np
# getting a specific element in 2d array
a=np.array([[1,2,3,4,5,6,7],[8,9,10,11,12,13,14]])
print(a[1,-2])
#getting specific row and column
print(a[0,:])
print(a[:,2])
#slicing syntax a[startindex:endindex:stepsize]
print(a[0,2:6:2])
#a[0th row , start from index 2 : end with index 6 : step size 2]
print(a[0,-2:-7:-2])
print(a[0,0:-1:2])
#modify or change the elemets in array
a[1,6]=20
print(a)
#modify element of one full column
a[:,0]=[11,21]
print(a)
#3d array
b=np.array([[[1,2,3],[4,5,6]],
            [[7,8,9],[10,11,12]]])
print(b)
#getting specific element of 3d array
print(b[0,1,2])
#conditional operator are also applied
m=np.array([20,-5,30,40])
print(m<[15,16,35,36])
print(m<25)
#to get the elements below 25
print(m[m<25])
#np.arange(number of elements from 0 to x).reshape(no of rows, no of col)
l=np.arange(12).reshape(3,4)
#np.arange(number of elements from 0 to x).reshape(,no of blocks,no of rows, no of col)
n=np.arange(24).reshape(3,4,2)
print(n)
s=np.array([[-2.5,3.1,7],[10,11,12]])
print(s)
print(type(s))
print("mean= ", a.mean())
print("min= ", a.min())
print("max= ", a.max())
print("sum= ", a.sum())
print("std= ", a.std())
print("var= ", a.var())
print("product= ", a.prod())

p=np.arange(12).reshape(3,4)
print(b)
#axis = 0 means column
print("Sum across columns" , p.sum(axis=0))
#axis = 1 means row
print("Min across columns" , p.min(axis=1))
print("Cummulative sum", p.cumsum(axis =1))
#transpose
q=np.array([[1,2,3,4],[5,6,7,8]])
print(q)
print(q.T)
