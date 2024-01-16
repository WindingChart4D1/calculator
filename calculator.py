print("Welcome to calculator!")

while (True):
    operation = input("Would you like to Add, Subtract, Multiply or Divide?\n")
    operation = operation.lower()
    if operation == str("add"):
        number1 = input("Alright, what is your first number?\n")
        number1 = int(number1)
        number2 = input("What's your second number?\n")
        number2 = int(number2)
        while (True):
            moreNumber = input("Do you want another number? Yes, or No\n")
            moreNumber = moreNumber.lower()
            if moreNumber == str("yes"):
                number3 = input("Ok, what is your third number?\n")
                number3 = int(number3)
                answer = number1 + number2 + number3
                print("Thank you, your answer is " + str(answer))
                break
            elif moreNumber == str("no"):
                answer = number1 + number2
                print("Thank you, your answer is " + str(answer))
                break
            else:
                print("Sorry, please only use 'Yes' or 'No'")
    elif operation == str("subtract"):
        number1 = input("Alright, what is your first number?\n")
        number1 = int(number1)
        number2 = input("What's your second number?\n")
        number2 = int(number2)
        while (True):
            moreNumber = input("Do you want another number? Yes, or No\n")
            moreNumber = moreNumber.lower()
            if moreNumber == str("yes"):
                number3 = input("Ok, what is your third number?\n")
                number3 = int(number3)
                answer = number1 - number2 - number3
                print("Thank you, your answer is " + str(answer))
                break
            elif moreNumber == str("no"):
                answer = number1 - number2
                print("Thank you, your answer is " + str(answer))
                break
            else:
                print("Sorry, please only use 'Yes' or 'No'")
    elif operation == str("multiply"):
        number1 = input("Alright, what is your first number?\n")
        number1 = int(number1)
        number2 = input("What's your second number?\n")
        number2 = int(number2)
        while (True):
            moreNumber = input("Do you want another number? Yes, or No\n")
            moreNumber = moreNumber.lower()
            if moreNumber == str("yes"):
                number3 = input("Ok, what is your third number?\n")
                number3 = int(number3)
                answer = number1 * number2 * number3
                print("Thank you, your answer is " + str(answer))
                break
            elif moreNumber == str("no"):
                answer = number1 * number2
                print("Thank you, your answer is " + str(answer))
                break
            else:
                print("Sorry, please only use 'Yes' or 'No'")
    elif operation == str("divide"):
        number1 = input("Alright, what is your first number?\n")
        number1 = int(number1)
        number2 = input("What's your second number?\n")
        number2 = int(number2)
        while (True):
            moreNumber = input("Do you want another number? Yes, or No\n")
            moreNumber = moreNumber.lower()
            if moreNumber == str("yes"):
                number3 = input("Ok, what is your third number?\n")
                number3 = int(number3)
                answer = number1 / number2 / number3
                print("Thank you, your answer is " + str(answer))
                break
            elif moreNumber == str("no"):
                answer = number1 / number2
                print("Thank you, your answer is " + str(answer))
                break
            else:
                print("Sorry, please only use 'Yes' or 'No'")
    else:
        print("Sorry, please only enter 'Add', 'Subtract', 'Multiply' or 'Divide'.")
