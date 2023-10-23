def arithmetic_operation():
    first_num = float(input("Enter first number: "))
    operator = str(input("Enter operator: "))
    second_num = float(input("Enter second number: "))

    add = first_num + second_num
    subtract = first_num - second_num
    divide = first_num / second_num
    multiply = first_num * second_num

    print("Your answer is")

    if operator == "+":
        print(add)
    elif operator == "-":
        print(subtract)
    elif operator == "/":
        if second_num == 0:
            print("Cannot divide by zero")
        else:
            print(divide)
    elif operator == "*":
        print(multiply)
    else:
        print("Invalid operator!")

arithmetic_operation()

while True:
    option_to_continue = input("Do you want to continue. Choose Yes or No: ")
    if option_to_continue == "Yes":
        arithmetic_operation()
    elif option_to_continue == "No":
        print("Thanks for using the calculator")
        break
    else:
        print("Invalid option!")
