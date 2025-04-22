#list
list1=[1,"hi","python",2]
print(type(list1))
print(list1)
#list operations
print(list1[3:])
"""slicing , in slicing [n:m]
n is starting index and it prints unitl m-1"""
print(list1[0:2])
print(list1+list1)
print(list1*3)
#tuple
tup= ("hi","python",2)
print(type(tup))
print (tup[3:1])
i=[7,8,"jj"]
print(i[1])
i[1]=10
print(i)
t1=(1,2,3,4,"GG")
print(t1[0])
print(t1[-1:-3])
print(t1[-3])
"""slice syntax is: start:stop:step """
#t1[0]=55 , this statement is not possible as tuples are immutable
tt=(2)
print(type(tt))
"""when there is one element of in tuple
instead of datatype tuple , it will print datatype of the element"""
#creating a set
t1={"apple","banana","cherry"}
print(t1)
t2={"apple","banana","cherry","apple"}
print(t2)
t3={"apple","banana","cherry",True,1,2}
print(t3)
t4={"apple","banana","cherry",False,True,0}
print(t4)
print(t1.add("nancy"))
t1.add("nancy")
print(t1)
#add an element in set
t1.remove("nancy")
print(t1)
#remove element in set
print("banana" in t1)
print("banana" not in t1)
#Creating Dictionaries
d1={"fruit":"apple","fruit":"orange","fruit":"banana"}
print(d1)
#boolean value
print(int(True))
print(bool(0))
#operators
a=int(input())
b=int(input())
c=int(input())
print(a+b-c)
print(a**b-c)
print(a+b//c)
print(a+b/c)
print(a%b-c)
print(a+b*c)
#check the comparision operator
print(bool(a!=c))
print(bool(c==c))
print(bool(a<=c))
print(bool(a>=b))
print(bool(b>c))
a+=b
print(a)
"""in assignment operator you can't use +=,-=,/=*= and print statement on same line"""
