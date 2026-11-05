#functions ->reusable block of code,modularity,scoping

'''syntax -> def function_name(parameters):
  #code block '''

#function without parameters
def greet(): #defining a function  without parameters
    print("Hello, welcome to the function tutorial!")

greet()  # Calling the function to execute its code block

#function with parameters(placeholders for values,arguments are the actual values passed to the function)
def greet_person(name):  #name is the parameter
    print('Hi',name)

greet_person('Romaisa')  # 'Romaisa' is the argument
greet_person('Ayesha')  

'''there are 3 types of arguments:
1. positional arguments -> the order of arguments matters
2. keyword arguments -> the order of arguments does not matter
3. default arguments -> arguments with default values'''

#positional arguments
def greet(name,age):
    print('Hi',name,'you are',age,'years old')

greet(22,'Romaisa')  # here output makes no sense because the order is wrong
greet('Romaisa',22)  # here output makes sense because the order is correct


#keyword arguments
def gret(name,age):
    print('Hi',name,'you are',age,'years old')
gret(age=22,name='Romaisa')  

#default arguments
def greet(name,age=0):  # age has a default value of 0
    print(f'Hi {name}, you are {age} years old')

greet('Romaisa')  # age will take the default value of 0
greet('Ayesha',25)  # age will take the value of 25