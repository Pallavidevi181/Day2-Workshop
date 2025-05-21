def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def multi(a, b):
    return a * b

def div(a, b):
    if b != 0:
        return a / b
    else:
        return "Division by zero is not allowed"

print("1: Addition\t2: Subtraction\t3: Multiplication\t4: Division")
choice = int(input("Enter your choice: "))

if choice in [1, 2, 3, 4]:
    x = int(input("Enter the first value: "))
    y = int(input("Enter the second value: "))

    if choice == 1:
        print("Result:", add(x, y))
    elif choice == 2:
        print("Result:", sub(x, y))
    elif choice == 3:
        print("Result:", multi(x, y))
    elif choice == 4:
        print("Result:", div(x, y))
else:
    print("Invalid choice")