#Beginner app [Simple Calculator]

operation = input("Select operation (+|-|*|/):")

#simple validation
while True:
    try:
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))
        break
    except ValueError:
        print("Please enter an interger")

if operation == '+':
    print("The sum of the input is: ", num1 + num2)

if operation == '-':
    print("The sum of the input is: ", num1 - num2)

if operation == '*':
    print("The sum of the input is: ", num1 * num2)

if operation == '/':
    print("The sum of the input is: ", num1 / num2)


