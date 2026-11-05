#dictionary ->key-value pair,unordered before 3.7 now ordered,mutable,dynamic
#dictionary creation
info = {
    'Name': 'Romaisa',
    'Age' : 22,
    'CGPA': 3.40,
    'Marks' : [60,70,80,90]
}
print(info)
#add element in dict
info['Height'] = 5.3
print(info)

#update element in dict 
info['Name'] = 'Romaisa Dildar'
print(info)

#delete element from dictionary
del info['CGPA']
print(info)