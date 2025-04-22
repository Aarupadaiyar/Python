import numpy as np
a=np.array([1,2,3,4])
print (a)
b=np.array([[1,2,3,4,5,],
            [6,7,8,9,10]])
print(b)
#array.ndim tells you the dimension of the array
print(a.ndim)
#array.shape tells you the (row,column) of the array
print(b.shape)
"""array.dtype tells you data type of the array ,
by defult it will be int32 or int 64 and it is platform dependent"""
print(a.dtype)
#we can also specify what datatype to use for array
c=np.array([[[1,2,3],
             [1,2,3]],
            [[4,5,6],
             [4,5,6]]] , dtype='int16')
print(c.itemsize)
d=np.array([2,4,7,9,65,4,32,21,11])
print(a[2:5])
#array.size return number of elements
print(c.size)
"""to get total size there are two ways 1. array.size * array.itemsize
2 array.nbytes return number of bytes in the array
8bits = 1 byte"""
print(c.itemsize*c.size)
print(c.nbytes)
print(b[1 ,3])
print(c[1,0,0])

