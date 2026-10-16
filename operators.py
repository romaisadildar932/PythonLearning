#arithmetic operators
print("arithmetic operators")
a=10
b=2
print(a+b)
print(a-b)
print(a*b)
print(a/b) #division ->return in float
print(a//b) #floor division ->return in integer
print(a%b) #modulus ->return the remainder
print(a**b) #exponentiation ->return the power of a raised to b

#comparison operators ->compare the values and return boolean value
print("comparison operators")
print(a==b) #equal to
print(a!=b) #not equal to
print(a>b) #greater than
print(a<b) #less than
print(a>=b) #greater than or equal to
print(a<=b) #less than or equal to

#logical operators ->return boolean value
print("logical operators")
x=True
y=False
print(x and y) #logical and
print(x or y) #logical or
print(not x) #logical not

print("Example of logical operators")
age = 22
is_student = True
print(age > 18 and is_student) #True
print(age > 25 or is_student) #True
print(not is_student) #False

print("Another example of logical operators")
a=10
b=20
print(a>5 and b<30) #True
print(a>15 and b<30) #False
print(a>15 or b<30) #True
print(a>15 or b>30) #False 
print(not(a>15 or b>30)) #True
print(not(b==20)) #False

#assignment operators ->assign values to variables
print("assignment operators")
c=10
print(c)
c+=5 # equivalent to c = c + 5
print(c)
c-=3 # equivalent to c = c - 3
print(c)
c*=2 # equivalent to c = c * 2
print(c)
c/=4 # equivalent to c = c / 4
print(c)

#identify operators ->compare the memory location of 2 objects andreturn boolean value
""" is -> returns True if both variables point to the same object in memory 
is not -> returns True if both variables point to different objects in memory """
print("identity operators")
a=[1,2,3]
a=b
c=[1,2,3]
print(a is b) #True
print(a is c) #False
print(a is not c) #True


#membership operators ->return boolean value
""" in -> returns True if a value is found in the specified sequence
not in -> returns True if a value is not found in the specified sequence"""
print("membership operators")
fruits=["apple","banana","cherry","mango"]
print("apple" in fruits) #True
print("grapes" in fruits) #False
print("orange" not in fruits) #True
print("mango" not in fruits) #False