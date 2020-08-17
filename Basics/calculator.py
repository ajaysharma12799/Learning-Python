# Program for Simple Calculator

def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    return num1 / num2

def modulo(num1, num2):
    return num1 % num2

print("Please Select Following Operation :- \n"
    "1. Addition\n " \
    "2. Subtraction\n " \
    "3. Multiplication\n " \
    "4. Division\n " \
    "5. Modulus\n ")

choice = int(input("Enter Your Choice From Above Otion : "))
number1 = int(input("Enter First Numnber : "))
number2 = int(input("Enter Second Number : "))

if choice == 1:
    print(add(number1, number2))
elif choice == 2:
    print(subtract(number1, number2))
elif choice == 3:
    print(multiply(number1, number2))
elif choice == 4:
    print(divide(number1, number2))
elif choice == 5:
    print(modulo(number1, number2))
else:
    print("Invalid Choice")