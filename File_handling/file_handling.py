"""here we work with 2 types of data
1.text files(.txt,.csv)
2.binary files(.jpg,.png,.pdf,.mp3,.mp4)
text files -> files that contain human-readable characters and can be opened and edited using a text editor
binary files -> files that contain data in a format that is not human-readable and can only be opened and edited using specific software or applications
file handling -> process of working with files in a program, including creating, reading, writing,
"""
#open -> open('filename','mode') -> opens a file and returns a file object that can be used to read or write data to the file
file = open('C:\\Users\\Dell\\Desktop\\PythonLearning\\README.md', 'r', encoding='utf-8') #open file in read mode
content = file.read() #read the content of the file
print(content)
file.close() #closes the file and releases any system resources associated with it

"""List of modes:
r -> read mode
w -> write mode (also craete new file if not exist or overwrite the existing data)
a -> append mode (also craete new file if not exist)
x -> Exclusive creation mode 
r+ -> read and write mode
w+ -> write and read mode
a+ -> append and read mode
x+ -> exclusive creation with read and write mode"""