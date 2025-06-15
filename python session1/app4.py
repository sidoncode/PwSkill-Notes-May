# lets create a calc

num1 = int(input("Enter the first number"))
num2 = int(input("Enter the second number"))

print("-----------")

opr = input("Enter the operation which needs to be executed")

if opr == "+":
    result = num1 +num2
    print("The result is: ", result)

elif opr == "-":
    result = num1 - num2
    print("The result is: ", result)

elif opr == "*":
    result = num1 * num2
    print("The result is: ", result)

elif opr == "%":
    result = num1 % num2
    print("The result is: ", result)


elif opr == "/":
    result = num1 / num2
    print("The result is: ", result)
