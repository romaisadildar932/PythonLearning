#exception handling -> process of dealing with runtime errors in a program to prevent it from crashing
'''try:
    num = int(input('Enter a number:'))
    result = 10 / num
    print(f'Result: {result}')
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")

except ValueError:
    print("u can't divide with a string")

finally:  #must be executed whether an exception occurs or not
    print("Execution completed.")'''


'''
try:
    file = open('non_existent_file.txt', 'r')
except FileNotFoundError:
    print("Error: File not found.")
finally:
    file.close()  #close the file if it was opened successfully
    print("File closed.")'''

#nested try-except blocks
try:
    num1 = int(input('Enter a number:'))
    num2 = int(input('Enter another number:'))
    try:
        result = num1 / num2
        print(f'Result: {result}')
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
except ValueError:
    print("Error: Please enter valid integers.")