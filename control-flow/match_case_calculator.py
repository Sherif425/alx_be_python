num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
operation = input("Choose the operation (+, -, *, /): ")

match operation:
    case '+':
        sum = num1 + num2
        print("The result is: ", sum)
    case '-':
        sub = num1 - num2
        print("The result is: ", sub)
    case '*':
        mult = num1 * num2
        print("The result is: ", mult)
    case '/':
        if num2 == 0:
            print("Cannot divide by zero")
        else:
            div = num1 /num2
            print("THe result is: ", div)
