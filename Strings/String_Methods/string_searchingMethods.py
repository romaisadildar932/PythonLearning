#find method ->returns the index of the first occurrence of the substring
text = "My name is Romaisa"
print(text.find("n"))
print(text.find("is")) #also use index

#rfind method ->returns the index of the last occurrence of the substring
print(text.rfind("m"))

#count method ->returns the number of occurrences of the substring
print(text.count("a"))

#startswith method ->returns True if the string starts with the specified substring
print(text.startswith("M")) #true
print(text.startswith("m")) #false
print(text.startswith("r")) #false

#endswith method ->returns True if the string ends with the specified substring
print(text.endswith("a")) #true
print(text.endswith("e")) #false