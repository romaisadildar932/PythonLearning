#strings are immutable,indexed,iterable
#ways of writing strings
name = 'romaisa'
name1= "Romaisa"
name2= '''My name is romaisa.My age is 22.
I have done my gradution in BS IT and currently learning a python'''
print(name,name1,name2)
#iterating through string
for i in name:
    print(i)

#indexed 
print(name[0])
print(name[4]) #+ve indexing ->left to right
print(name[-1]) #-ve indexing ->right to left