# control statements ->control the flow of execution of the program
# conditional statement
#if statement 
print("if statement")
age=int(input("Enter your age:"))
if age>=18:
    print("You are eligible to vote.")

#else statement
print("else statement")
age=int(input("Enter your age:"))
if age>=18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")

#elif statement
print("elif statement")
age=int(input("Enter your age:"))
if age>=18:
    print("You are eligible to vote.")
elif age<=0:
    print("Invalid age")
else:
    print("You are not eligible to vote.")

#Practice Question
print("Practice Question")
n1=int(input("Enter first number:"))
n2=int(input("Enter second number:"))
choice=input("Enter your choice (+,-,*,/,//,%,**):")
if choice == "+":
    print(n1+n2)
elif choice == "-":
    print(n1-n2)
elif choice == "*":
    print(n1*n2)
elif choice == "/":
    print(n1/n2)
elif choice == "//":
    print(n1//n2)
elif choice == "%":
    print(n1%n2)
elif choice == "**":
    print(n1**n2)
else:
    print("Invalid choice")