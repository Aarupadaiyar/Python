import numpy as np
a=np.array([1,2,3,4])
#creating array 1d
b=np.array([[1,2,3,4,5,11,12],[6,7,8,9,10,13,14]])
#creating array 2d
print(a)
print(b)
print(a.ndim)
#print the dimension of array
print(b.shape)
#print rows and column
print(b.dtype)
#print datatype of the array
print(a.itemsize)
#print size or byte of single element
print(b.size)
#print number of element
print(b.itemsize * b.size)
#print total size of the array
print (b.nbytes)
#other way print total size of the array
print(b[0,2])
#acessing element a[row,col]
print(b[0,-1])
#acessing elements using negative index where it starts from -1
print(b[0,:])
#acessing specific row
print(b[:,0])
#Acessing specific col
print(b[0,1:6:2])
#Acess in more indepth method [starting index : ending index: stepsize]
print(b[1,0:-1:1])
#Acesssing elements using negative index
b[1,5]=11
print(a)
#manipulating single element
b[:,2]=[1,2]
print(b)
#manipulating whole column
c=np.array([[[1,2,3,4],[5,6,7,8]],
            [[9,10,11,12],[13,14,15,16]],
            [[17,18,19,20],[21,22,23,24]]])
print(c)
#creating 3d array
print(c[1,0,3])
#Acessing specific element in 3d array
