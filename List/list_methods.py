#append ->add element at the end of list
list = [1,2,3,4]
list.append(5)
print(list)

#extend ->Add multiple elements to the end of a list
list1 = [1,2,3]
list1.extend([4,5,6,7])
print(list1)

list2 = [1,2,3,4]
list3 = [5,6,7,8,9]
list3.extend(list2)
print(list3)

#insert ->add element at a specific position 
list1.insert(0,10)
print(list1)

#remove ->remove the specific value from list
a=[1,2,3,4,5]
a.remove(2)
print(a)

#pop ->remove the element at a specific position
a.pop(0)
print(a)

#clear ->clear all elements of list at once
a.clear()
print(a)

#index ->gives the index of specific element
b=[10,20,30,40,50,60]
index = b.index(10)
print(index)
#count ->returns how many times a specific element appears in a list
c= [1,2,3,4,5,5,6,3,2,1,3,3,3,8,9,1,2,2,2]
counter = c.count(3)
print(counter)
#sort ->arranges the elements of a list in ascending order by default
c.sort()
print(c)
#reverse ->reverse all elements of list
c.reverse()
print(c)
#min ->find min element of the list
print(min(c))
#max ->find max element of the list
print(max(c))
#common ->find common element from 2 lists
d=[1,2,3,4,5,6,7,8]
s1 = set(c)
s2 = set(d)
s3 = s1.intersection(s2)
print(s3)

#nested ->list inside a list
e = [1,2,3]
f = [4,5,6,e,[7,8,9]]
print(f)

#list comprehension
squares =[i ** 2 for i in range(1,10)]
print(squares)
