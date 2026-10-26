#list indexing
lst = [1,2,3,4]
print(lst)
print(lst[1])
#updation
lst[1] = "Hlo"
print(lst)
#slicing
lst1 = [5,6,7,8,9,10]
print(lst1)
lst1[0:3] = "Hlo",20,"How are u?"
print(lst1)
#concatination
print(lst + lst1)
#repeatation
print(lst * 3)
#membership
print("Hlo" in lst1)
print(80 in lst1)
lst2 = [5,6,7,8,9,10]
check = int(input("Enter a num to check:"))
if check in lst2: 
    print("Found")
else:
    print("Not Found") 

#alias ->if one list is upadte, second one is also updated(2 variables pointing the same data)
list1 = [1,2,3]
list2 = list1
list2[0] = '100'
print(list1,list2)

#copy -> If one list is updated, the copied list remains unchanged
list1 = [1,2,3]
list2 = list1.copy()
list2[0] = '100'
print(list1,list2)



