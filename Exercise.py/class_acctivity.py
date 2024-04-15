name = str(input("Enter your name:"))
num1 = float(input("Enter your first number:"))
num2 = float(input("Enter you second number:"))
z = ("You can use only fpur operators which are\n+, -, /and *")
print (z)
operation = (input("Enter the operation you want to use with given number :"))

if operation == '+':
    a = num1 +num2
    print(f"Sum is: {a}")
elif operation == '*':
    b = num1 * num2
    print(f"product is: {b}")
elif operation == '-':
    c = num1 - num2
    print(f"difference is: {c}")

else:
    operation == '/'
    d = num1 * num2
    print(f"quaotion is: {d}")

