import art



def add(a, b):
    return a + b
def subtract(a, b):
    return a - b
def multiply(a, b):
    return a * b
def divide(a, b):
    return a / b

def operation(a, b, operator):
    if operator == '+':
        return add(a, b)
    elif operator == '-':
        return subtract(a, b)
    elif operator == '*':
        return multiply(a, b)
    else:
        return divide(a, b)


print(art.logo)

first_number = float(input("What is your first number? "))
while True:
    operators = {
        "+": '+',
        "-": '-',
        "*": '*',
        "/": '/',
    }
    operator = input("+\n-\n*\n/\nWhat is your operator? ")
    second_number = float(input("What is your second number? "))

    result = operation(first_number, second_number, operators[operator])
    print(f"{first_number} {operators[operator]} {second_number} = {result}")

    is_continue = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ").lower()
    if is_continue == 'n':
        first_number = float(input("What is your first number? "))
        result = 0
    else:
        first_number = result


















