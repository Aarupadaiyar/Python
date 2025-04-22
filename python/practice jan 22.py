#Conditional operator
a=5
print((a>3 and a<5) or (a<3 and a>5))
print('a>3 or a<5')
print('a>3 and a<5', a<3 and a<5)
#" ," in multiprint statement gives one default whitespace
#conditional operator

age=int(input("Enter your age? "))
if(age>=18):
    print("Welcome to adulthood and your knee pain era starts ")
else:
    print("Ouch go and simp on cocomelon")
a=(int(input("Enter 1st number")))
b=(int(input("Enter 2nd number")))
c=(int(input("Enter 3rd number")))
if((a>b) & (a>c)):
    print("A is bada number")
elif((b>a) & (b>c)):
    print("B is bada number")
else:
    print("C is bada number")
#Loops in python
for i in  range(5):
    print(i, end=" ")
while i<5 :
    print(i)
    i+=1
print(i)
fruits=["amazon apple","kashmir apple","department store apple"]
for x in fruits:
    print(x)
for i in range(10):
    if i==5:
        break;
    print(i)
for i in range (10):
    if i==5:
        continue
    print(i)
#try:code that might raise an exception
#expect:code to handle the exception
try:
    x=10/0
except :
    print("cannot divide by zero")
try:
    print(s)
except:
    print("something went wrong:")
def namastebolo(name):
    print("Namaste uncle",name,"ji")
name=input("enter the name:")
namastebolo(name)
def sum(a,b):
    print(a+b)
def power(a,b):
    y=pow(a,b)
    return y
a=int(input("write A : "))
b=int(input("write B : "))
sum(a,b)
power(a,b)
#Module
def greeting(name):
    print("Hello, " + name)
student = {"name":"john"
           "age":20
           "group":2}
import module as mm
q=mm.student["age"]
print(q)
l






































