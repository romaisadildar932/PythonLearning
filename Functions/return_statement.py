#return -> The return statement is used to exit a function and go back to the place where it was called. This statement can optionally return a value to the caller. If no value is specified, the function will return None by default.

def greet(name):
    return f'Hi,{name}'
greeting =greet('Romaisa')
print(greeting)

def add(a,b):
    return a+b
result =add(5,20)
print(result)