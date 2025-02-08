def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

num1 = float(input("Enter your first number: "))
num2 = float(input("Enter your second number: "))
op_choice = input("Enter your operation choice (+, -, *, /) : ")
if op_choice == "+":
    print(operations["+"](num1, num2))
elif op_choice == "-":
    print(operations["-"](num1, num2))
elif op_choice == "*":
    print(operations["*"](num1, num2))
elif op_choice == "/":
    print(operations["/"](num1, num2))

