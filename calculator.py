#Calculator
import math
History = []
print("Welcome to the Calculator!")
while True:
    menu = input("\n+--------------------------------+\n| To Add Numbers     : Enter [1] |\n| To Subtract Numbers: Enter [2] |\n| To Multiply Numbers: Enter [3] |\n| To Divide Numbers  : Enter [4] |\n| To Use Power       : Enter [5] |\n| To Use Modulus     : Enter [6] |\n| To Use Sqrt        : Enter [7] |\n| To View History    : Enter [8] |\n| To Clear History   : Enter [9] |\n+--------------------------------+\n")
    if menu.isdigit():
        menu = int(menu)
        if menu == 1:
            num1 = input("Enter the number you want to add: ")
            num2 = input("Enter the number you want to add: ")
            try:    
                num1 = float(num1)
                num2 = float(num2)
                num3 = num1 + num2
                print(f"{num1} + {num2} = {num3}")
                History.append(f"{num1} + {num2} = {num3}")
            except:
                print("Invalid Input!")
        elif menu == 2:
            num1 = input("Enter the number you want to subtract: ")
            num2 = input("Enter the number you want to subtract: ")
            try:    
                num1 = float(num1)
                num2 = float(num2)
                num3 = num1 - num2
                print(f"{num1} - {num2} = {num3}")
                History.append(f"{num1} - {num2} = {num3}")
            except:
                print("Invalid Input!")
        elif menu == 3:
            num1 = input("Enter the number you want to multiply: ")
            num2 = input("Enter the number you want to multiply: ")
            try:    
                num1 = float(num1)
                num2 = float(num2)
                num3 = num1 * num2
                print(f"{num1} * {num2} = {num3}")
                History.append(f"{num1} * {num2} = {num3}")
            except:
                print("Invalid Input!")
        elif menu == 4:
            try:
                num1 = input("Enter the Numerator: ")
                num2 = input("Enter the Denominator: ")
                num1 = float(num1)
                num2 = float(num2)
                if num2 == 0.0:
                    print("Not Defined!")
                else:
                    num3 = num1 / num2
                    print(f"{num1} / {num2} = {num3}")
                    History.append(f"{num1} / {num2} = {num3}")
            except:
                print("Invalid Input!")
        elif menu == 5:
            try:
                power_input = input("Enter both numbers seperated by [,] to get power of that number: ").split(",")
                num1 = float(power_input[0])
                num2 = float(power_input[1])
                num3 = num1**num2
                print(f"{num1} ** {num2} = {num3}")
                History.append(f"{num1} ** {num2} = {num3}")
            except:
                print("Invalid Input!")
        elif menu == 6:
            try:
                modulus_input = input("Enter both numbers seperated by [,] to get the modulus of number: ").split(",")
                num1 = float(modulus_input[0])
                num2 = float(modulus_input[1])
                num3 = num1%num2
                print(f"{num1} % {num2} = {num3}")
                History.append(f"{num1} % {num2} = {num3}")
            except:
                print("Invalid Input!")
        elif menu == 7:
            sqrt_input = input("Enter the number: ")
            try:
                sqrt_input = float(sqrt_input)
                num3 = math.sqrt(sqrt_input)
                print(num3)
                History.append(f"sqrt of {sqrt_input} = {num3}")
            except:
                print("Invalid Input!")
        elif menu == 8:
            print("History of calculations")
            for i in History:
                print(i)
        elif menu == 9:
            History.clear()
            print("History Cleared!")
        else:
            print("Enter Number b/w 1 to 4.")
    else:
        print("Invalid Input!")
