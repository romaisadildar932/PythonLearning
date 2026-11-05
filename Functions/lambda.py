#lambda ->small anonymous function that can have multiple arguments but only one expression.

#syntax: lambda arguments: expression condition

square = lambda x: x*x 
print(square(4))

seq = lambda n: [x for x in range(1, n)]
print(seq(11))