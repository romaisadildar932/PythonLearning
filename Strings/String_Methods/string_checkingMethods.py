#checking method ->returns boolean value
#alpha method ->returns True if all characters in the string are alphabets
name = "romaisa"
print(name.isalpha()) #True ->all characters are alphabets
name1 = "romaisa123"
print(name1.isalpha()) #False ->contains numbers

#isdigit method ->returns True if all characters in the string are digits
age = "22"
print(age.isdigit()) #True ->all characters are digits
age1= "22.5"
print(age1.isdigit()) #False ->contains decimal point

#isalnum method ->returns True if all characters in the string are alphanumeric
height = "Height is 5.3"
print(height.isalnum()) #False ->contains space and decimal point
height1 = "Height53"
print(height1.isalnum()) #True ->all characters are alphanumeric

#isspace method ->returns True if all characters in the string are whitespace
space = "   "
print(space.isspace()) #True ->all characters are whitespace
space1 = "  a  "
print(space1.isspace()) #False ->contains non-whitespace character

#islower -> returns true if all characters are in lowercase
print(name.islower())
#isupper -> returns true if all characters are in uppercase
print(name.isupper())