import numpy as np
a=np.array([1,2,3])
b=type(a)
print(b)
#print odd number and even number:
a=[]
n=int(input("Write the number of element: "))
for i in range(n):
    element=int(input(f"Enter the element {i+1} : "))
    a.append(element)
print(a)
for i in range(n):
    if(a[i]%2==0):
        print(a[i], end=" ")
        #print("\n")

for i in range(n):
    if(a[i]%2!=0):
        print(a[i], end=" ")

#print prime numbers:
user_input = input("Enter the all number with one whitespace between them: " ).split( )
print(user_input)

    
