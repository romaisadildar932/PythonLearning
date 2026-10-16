#break statement ->used to exit the loop when a certain condition is met
print("break statement")
for i in range(1,11):
    if i==5:
        break
    print(i)

#continue statement ->used to skip the current iteration of the loop and move on to the next iteration

print("continue statement")
for i in range(1,11):
    if i==5:
        continue #skip 5
    print(i)

#pass statement ->used as a placeholder for future code, it does nothing when executed
print("pass statement")
for i in range(1,11):
    if i==5:
        pass #placeholder for future code
    print(i)

#practice question
a=int(input("Enter a start number: "))
b=int(input("Enter an stop number: "))
x=int(input("Enter a number to skip: "))
if a<b and x in range(a,b):
 for i in range(a,b):
    if i==x:
        continue #skip the number entered by user
    print(i)
else:
    print("Invalid range")