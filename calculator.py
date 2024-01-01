def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Error: Division by zero"

print("Simple Calculator")
print("Select operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

# Get user input
operation = input("Enter choice (1, 2, 3, 4): ")
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# Perform calculation based on user choice
if operation == '1':
    result = add(num1, num2)
    print(f"{num1} + {num2} = {result}")
elif operation == '2':
    result = subtract(num1, num2)
    print(f"{num1} - {num2} = {result}")
elif operation == '3':
    result = multiply(num1, num2)
    print(f"{num1} * {num2} = {result}")
elif operation == '4':
    result = divide(num1, num2)
    print(f"{num1} / {num2} = {result}")
else:
    print("Invalid input. Please enter a valid operation (1, 2, 3, or 4).")
