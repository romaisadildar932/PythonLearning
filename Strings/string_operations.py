#length
name="romaisa"
print(len(name))
name1= 'My name is romaisa.My age is 22.'
print(len(name1))

#practice question 
password = input("Enter a password: ")
if len(password)>5:
 print("Login Successful")
else:
 print("Invalid password")

#indexing
name = 'romaisa'
print(name[0])
print(name[4]) #+ve indexing ->left to right
print(name[-1]) #-ve indexing ->right to left

#slicing -> string[start:stop:step]
print(name[0:4]) #slicing from index 0 to 3
print(name[1:4]) #slicing from index 1 to 3
print(name[::2]) #slicing with step 2
print(name[::-1]) #reversing the string

#repeatation
print(name * 3) #repeating the string 3 times

#concatination ->strings are only concatenated with other strings not with other data types
name = 'romaisa'
sur_name = 'dildar'
print("Hi,",name + sur_name) #concatination of two strings

#checking membersip
text = "Hello, my name is romaisa."
print("name" in text)
print("name" not in text)
print("age" in text)
print("age" not in text)