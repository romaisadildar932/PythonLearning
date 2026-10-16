"""while loop is used to execute a block of code repeatedly as long as a given condition is true.
for loop is used to iterate over a sequence (such as a list, tuple, dictionary, set, or string)
and execute a block of code for each item in the sequence.
while condition:
    code block
    """

#while loop
print("while loop")
i=1
while i<=5:
    print(i)
    i+=1

#for loop
print("for loop")
for i in range(1,6): #in range stop is exclusive, so it will print 1 to 5
    print(i)

a=[9,10,8]
for i in a:
    print(i)

#nested loop
print("nested loop")
for i in range(1,4):
    for j in range(4,8):
        print(i,j)

#practice question
x=int(input("Enter a number: "))
for i in range(1,11):
    print(x," * ",i,"=",x*i)