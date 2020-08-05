#Beginner calculator

cont = "Y"

while cont == "Y" or cont == "y":
 
    operation = input("Select operation (+|-|*|/):")
    
    while True:
        if (operation == "+" or operation == "-" or operation == "*" or operation == "/"):
            break
        else:
            operation = input("Please enter valid operation:")
    
    #simple validation
    while True:
        try:
            num1 = int(input("Enter first number: "))
            num2 = int(input("Enter second number: "))
            break
        except ValueError:
            print("Please enter an interger")
    
    #Simple function
    def result(numA, numB, op):
        if op == '+':
         print("The sum of the input is: ", numA + numB)
    
        if op == '-':
         print("The substraction of the input is: ", numA - numB)
    
        if op == '*':
         print("The multiplication of the input is: ", numA * numB)
    
        if op == '/':
         print("The division of the input is: ", numA / numB)
    
    #Function call
    result(num1, num2, operation)
    
    #Rerun calculator
    cont = input("Do you want to run the calculator again? [Y/N] ")
    
    while True:
        if cont == "y" or cont == "Y":
            break
        else:
            print("Calculator stopped")
            break
        
#Note: While True means that it will loop indefinitely until it is breaked (stopped) in the statement.


