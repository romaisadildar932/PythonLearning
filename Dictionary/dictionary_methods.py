info = {
    'Name': 'Romaisa',
    'Age' : 22,
    'CGPA': 3.40,
    'Marks' : [60,70,80,90]
}
#get() ->use to retrieve specific element
age = info.get('Age')
print(age)
height = info.get('Height','Not Found')
print(height)

#keys ->return all keys of dict
k = info.keys()
print(k)

#values ->return all values of dict
v = info.values()
print(v)

#items ->return all items of dict
i = info.items()
print(i)

#pop ->use to remove specific key from list and returns its value
popped = info.pop('CGPA')
print(popped)

#popitem ->use to remove last item of your dict
popped_i = info.popitem()
print(popped_i)
print(info)

#clear ->clear all items of dict
cleared = info.clear()
print(info)
