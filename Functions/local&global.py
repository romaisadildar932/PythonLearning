#local variables ->define and  access only inside the function 

def greet():
    n = 'Romaisa'  # local variable
    print('Hi',n)
greet()
# print(n) # here will give an error because name is a local variable and cannot be accessed outside the function

#global variables -> define and access inside and outside the function

name = 'Ayesha' # global variable
def greet():
    print('Hi',name)
greet()
print(name) # here will not give an error because name is a global variable and can be accessed outside the function