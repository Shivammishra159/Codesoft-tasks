# Simple Calculator

# Ask the user to enter two numbers
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# Ask the user to choose an operation
print("Choose operation: +, -, *, /")
op = input("Enter operation: ")

# Perform calculation based on the operation
if op == "+":
    result = num1 + num2
elif op == "-":
    result = num1 - num2
elif op == "*":
    result = num1 * num2
elif op == "/":
    if num2 != 0:
        result = num1 / num2
    else:
        print("Error: Cannot divide by zero")
        exit()
else:
    print("Invalid operation")
    exit()

# Show the result
print("Result:", result)
