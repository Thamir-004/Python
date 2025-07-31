num1 = float(input("Enter the first no. : "))
num2 = float(input("Enter the second no. : "))
operation = input("Enter operation(+, - , x, /) : ")

if operation == "+":
    result = num1 + num2
    print(f"{num1} + {num2} = {result}")

elif operation == "-":
    result = num1 - num2
    print(f"{num1} - {num2} = {result}")

elif  operation == "x":
    result = num1 * num2
    print(f"{num1} * {num2} = {result}")

elif operation == "/":
    result = num1 / num2
    print(f"{num1} / {num2} = {result}")

else:
     print("invalid operation entered.")