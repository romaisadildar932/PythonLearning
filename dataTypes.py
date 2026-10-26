#numeric datatypes
a=10
b=2.3
c=1+2j
print(type(a),type(b), type(c))

#bool datatype
d=True
e=False
print(d,e)
print(type(d),type(e))

# none datatype
f=None
print(f)
print(type(f))
f=5
print(f)
print(type(f))

#sequence datatypes->str,list,tuple,range
g="hello" #immutable
h=[1,2,3] #mutable
i=(4,5,6) #immutable
j=list(range(1,5,1)) #immutable ->range(start,stop,step)
print(g,h,i,j)
print(type(g),type(h),type(i),type(j))

#set datatype ->unique values,unordered,mutable
k={1,2,3,3,3,5,7,7,6,9} #mutable
print(k)
print(type(k))

#frozenset datatype ->unique values,unordered,immutable
l=frozenset({1,2,3,3,3,5,7,7,6,9}) #immutable
print(l)
print(type(l))

#mapping datatype ->dict,key-value pair,unordered,mutable
person={"name":"Romaisa","age":22,"height":5.3} #mutable
print(person)
print(type(person))