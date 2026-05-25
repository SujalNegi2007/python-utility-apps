import string
def window():
    print("+-------------------------------------------------+\n| To Add Numbers                      : Enter [1] |\n| To Subtract Numbers                 : Enter [2] |\n| To Multiply Numbers                 : Enter [3] |\n| To Divide Numbers                   : Enter [4] |\n| To Use Power in Number              : Enter [5] |\n| To Find Module of  Numbers          : Enter [6] |\n| To Find Average of  Numbers         : Enter [7] |\n| To Find Biggest Number b/w Numbers  : Enter [8] |\n| To Find Smallest Number b/w Numbers : Enter [9] |\n| To Find Square root of Number      : Enter [10] |\n| To View History                    : Enter [11] |\n| To Delete History                  : Enter [12] |\n| To Exit                            : Enter [13] |\n+-------------------------------------------------+\n")
    return
#_______________________________________________________________________
def user_input_main_menu():
    input_main_menu = input("Enter the Number where you want to go: ")
    return input_main_menu
#_______________________________________________________________________
def check_int(input_main_menu):
    if input_main_menu.isdigit():
        input_main_menu = int(input_main_menu)
        if input_main_menu > 13 or input_main_menu < 1:
            print("Invalid Input! Error: chose a number that is not b/w 1 to 13.")
            return None , False
        else:
            return input_main_menu , True
    else:
        print("Invalid Input! Error: Wrote something that is not a number!")
        return None , False
#_______________________________________________________________________
def main_menu():
    window()
    input_main_menu = user_input_main_menu()
    checking, is_right = check_int(input_main_menu)
    if is_right:
        front_menu(checking)
    else:
        print("Invalid Input!")
#_______________________________________________________________________
def front_menu(checking):
    if checking == 1:
        output_front_menu = user_input_front_menu()
        sum_input(*output_front_menu)
    elif checking == 2:
        output_front_menu = user_input_front_menu()
        subtract_input(*output_front_menu)
    elif checking == 3:
        output_front_menu = user_input_front_menu()
        multiply_input(*output_front_menu)
    elif checking == 4:
        output_front_menu = user_input_front_menu()
        divide_input(*output_front_menu)
    elif checking == 5:
        output_front_menu = user_input_front_menu()
        #sum_input(*output_front_menu)
    elif checking == 6:
        output_front_menu = user_input_front_menu()
        #sum_input(*output_front_menu)
    elif checking == 7:
        output_front_menu = user_input_front_menu()
        #sum_input(*output_front_menu)
    elif checking == 8:
        output_front_menu = user_input_front_menu()
        #sum_input(*output_front_menu)
    elif checking == 9:
        output_front_menu = user_input_front_menu()
        #sum_input(*output_front_menu)
    elif checking == 10:
        output_front_menu = user_input_front_menu()
        #sum_input(*output_front_menu)
    elif checking == 11:
        output_front_menu = user_input_front_menu()
        #sum_input(*output_front_menu)
    elif checking == 12:
        output_front_menu = user_input_front_menu()
        #sum_input(*output_front_menu)
    elif checking == 13:
        output_front_menu = user_input_front_menu()
        #sum_input(*output_front_menu)
#_______________________________________________________________________
def user_input_front_menu():
    input_front_menu = input("Enter the numbers seperated by [,]: ").split(",")
    output_front_menu = []
    for i in range(len(input_front_menu)):
        output_front_menu.append(int(input_front_menu[i]))
    return output_front_menu
#_______________________________________________________________________
def user_input_main_menu():
    input_main_menu = input("Enter the Number where you want to go: ")
    return input_main_menu
#_______________________________________________________________________
def sum_input(*output_front_menu):
    total_sum = sum(output_front_menu)
    print(f"Sum of Number is: {total_sum}")
    return
#______________________________________________________________________
def subtract_input(*output_front_menu):
    total_subtraction = output_front_menu[0]
    for i in range(1,len(output_front_menu)):
        total_subtraction -= output_front_menu[i]
    print(f"Subtract of Numbers are: {total_subtraction}")
    return
#______________________________________________________________________
def multiply_input(*output_front_menu):
    total_multiply = 1
    for i in range(len(output_front_menu)):
        total_subtraction *= output_front_menu[i]
    print(f"Multiply of Numbers are: {total_subtraction}")
    return
#______________________________________________________________________
def divide_input(*output_front_menu):
    total_divide = output_front_menu[0]
    for i in range(1,len(output_front_menu)):
        if output_front_menu[i] != 0:
            total_divide /= output_front_menu[i]
        else:
            total_divide = "Not Defined"
            break
    print(f"Divide of Numbers are: {total_divide}")
    return
main_menu()
