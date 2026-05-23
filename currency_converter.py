#Currency Converter
def image():
    print("\n+-------------------------------------------------------------------------------------+\n| If you want to convert your currency from Indian Rupee to Indian Rupee  : Enter [1] |\n| If you want to convert your currency from Indian Rupee to U.S. Dollar   : Enter [2] |\n| If you want to convert your currency from Indian Rupee to Euro          : Enter [3] |\n| If you want to convert your currency from Indian Rupee to Japanese Yen  : Enter [4] |\n| If you want to convert your currency from Indian Rupee to British Pound : Enter [5] |\n| If you want to convert your currency from Indian Rupee to Chinese Yuan  : Enter [6] |\n| To Exit This Menu                                                       : Enter [7] |\n+-------------------------------------------------------------------------------------+\n")
    return
def image1():
    print("\n+---------------------------------------------------------------+\n| If you have Indian Rupee that you want to convert : Enter [1] |\n| If you have U.S. Dollar that you want to convert  : Enter [2] |\n| If you have Euro that you want to convert         : Enter [3] |\n| If you have Japanese Yen that you want to convert : Enter [4] |\n| If you have British Pound that you want to convert: Enter [5] |\n| If you have Chinese Yuan that you want to convert : Enter [6] |\n| To Exit This Menu                                 : Enter [7] |\n+---------------------------------------------------------------+\n")
    return
def User_selected_choice(a,b):
    if a == 1:
        User_selected_choice1 = "Indian Rupees"
        if b == 1:
            User_selected_choice2 = "Indian Rupees"
        elif b == 2:
            User_selected_choice2 = "U.S. Dollars"
        elif b == 3:
            User_selected_choice2 = "Euroes"
        elif b == 4:
            User_selected_choice2 = "Japanese Yens"
        elif b == 5:
            User_selected_choice2 = "British Pounds"
        elif b == 6:
            User_selected_choice2 = "Chinese Yuans"
    elif a == 2:
        User_selected_choice1 = "U.S. Dollars"
        if b == 1:
            User_selected_choice2 = "Indian Rupees"
        elif b == 2:
            User_selected_choice2 = "U.S. Dollars"
        elif b == 3:
            User_selected_choice2 = "Euroes"
        elif b == 4:
            User_selected_choice2 = "Japanese Yens"
        elif b == 5:
            User_selected_choice2 = "British Pounds"
        elif b == 6:
            User_selected_choice2 = "Chinese Yuans"
    elif a == 3:
        User_selected_choice1 = "Euroes"
        if b == 1:
            User_selected_choice2 = "Indian Rupees"
        elif b == 2:
            User_selected_choice2 = "U.S. Dollars"
        elif b == 3:
            User_selected_choice2 = "Euroes"
        elif b == 4:
            User_selected_choice2 = "Japanese Yens"
        elif b == 5:
            User_selected_choice2 = "British Pounds"
        elif b == 6:
            User_selected_choice2 = "Chinese Yuans"
    elif a == 4:
        User_selected_choice1 = "Japanese Yens"
        if b == 1:
            User_selected_choice2 = "Indian Rupees"
        elif b == 2:
            User_selected_choice2 = "U.S. Dollars"
        elif b == 3:
            User_selected_choice2 = "Euros"
        elif b == 4:
            User_selected_choice2 = "Japanese Yens"
        elif b == 5:
            User_selected_choice2 = "British Pounds"
        elif b == 6:
            User_selected_choice2 = "Chinese Yuans"
    elif a == 5:
        User_selected_choice1 = "British Pounds"
        if b == 1:
            User_selected_choice2 = "Indian Rupees"
        elif b == 2:
            User_selected_choice2 = "U.S. Dollars"
        elif b == 3:
            User_selected_choice2 = "Euros"
        elif b == 4:
            User_selected_choice2 = "Japanese Yens"
        elif b == 5:
            User_selected_choice2 = "British Pounds"
        elif b == 6:
            User_selected_choice2 = "Chinese Yuans"
    elif a == 6:
        User_selected_choice1 = "Chinese Yuans"
        if b == 1:
            User_selected_choice2 = "Indian Rupees"
        elif b == 2:
            User_selected_choice2 = "U.S. Dollars"
        elif b == 3:
            User_selected_choice2 = "Euroes"
        elif b == 4:
            User_selected_choice2 = "Japanese Yens"
        elif b == 5:
            User_selected_choice2 = "British Pounds"
        elif b == 6:
            User_selected_choice2 = "Chinese Yuans"
    return User_selected_choice1, User_selected_choice2
print("Welcome to the Currency Converter!")
History = {}
list_menu_3a = (1,2,3,4,5,6)
list_menu_3b =(7,)
Condition = False
Condition_while_exit_menu_1 = False
Condition_while_exit_menu_2 = False
Condition_while_exit_menu_3 = False
while True:
    User_name = input("Enter Your Full Name: ").capitalize().strip()
    Name_parts = User_name.split(" ")
    Surname = Name_parts[-1]
    First_name = Name_parts[0]
    a = []
    if First_name not in History:
        History[First_name] = []
        #History[User_Name] =a
        while True:
            option = input("\n+-------------------------------------+\n| To Convert Currency     : Enter [1] |\n| To View Currency History: Enter [2] |\n| To Clear History        : Enter [3] |\n| To Exit                 : Enter [4] |\n+-------------------------------------+\n")
            try:
                if option.isdigit():
                    option = int(option)
#-------------------------------------------------------------------------------------------------
                    if option == 1:
                        while True:
                            print("\nWhich currency Do you have?")
                            image1()
                            option1 = input()
                            try:
                                if option1.isdigit():
                                    option1 = int(option1)
#-------------------------------------------------------------------------------------------------
                                    if option1 == 1:
                                        print("Select the currency you want to convert into!")
                                        image()
                                        option2 = input()
                                        if option2.isdigit():
                                            option2 = int(option2)
                                            if option2 in list_menu_3a:
                                                currency1,currency2 = User_selected_choice(option,option2)
                                                while True:
                                                    yes_no = input(f"Are You Sure You want to convert {currency1} to {currency2}(yes/no)?\n").capitalize().strip()
                                                    if yes_no == "Yes":
                                                        try:
                                                            currency = input(f"Enter the amount of {currency1} you want to convert: ")
                                                            try:
                                                                total_currency = currency * 1
                                                                History[First_name].append(f"{First_name} converted {currency} {currency1} to {total_currency} {currency2}")
                                                                print(History)
                                                                Condition_while_exit_menu_3 = True
                                                                break
                                                            except:
                                                                print("Invalid Input! Error: 555")
                                                        except:
                                                             print("Invalid Input!")
                                                    elif yes_no == "No":
                                                        Condition_while_exit_menu_3 = True
                                                        break
                                                    else:
                                                        print("Only Yes And No Are Avaliable Options")
                                            elif option2 in list_menu_3b:
                                                print("Exiting...")
                                                break
                                        else:
                                            print("Only interger b/w 1 to 7 are allowed!")
#-------------------------------------------------------------------------------------------------
                                    elif option1 == 2:
                                        print("Select the currency you want to convert into!")
                                        image()
                                        option2 = input()
                                        if option2.isdigit():
                                            option2 = int(option2)
                                            if option2 in list_menu_3a:
                                                currency1,currency2 = User_selected_choice(option,option2)
                                                while True:
                                                    yes_no = input(f"Are You Sure You want to convert {currency1} to {currency2}(yes/no)?\n").capitalize().strip()
                                                    if yes_no == "Yes":
                                                        try:
                                                            currency = input(f"Enter the amount of {currency1} you want to convert: ")
                                                            try:
                                                                total_currency = currency * 1
                                                                History[First_name].append(f"{First_name} converted {currency} {currency1} to {total_currency} {currency2}")
                                                                print(History)
                                                                Condition_while_exit_menu_3 = True
                                                                break
                                                            except:
                                                                print("Invalid Input! Error: 555")
                                                        except:
                                                             print("Invalid Input!")
                                                    elif yes_no == "No":
                                                        Condition_while_exit_menu_3 = True
                                                        break
                                                    else:
                                                        print("Only Yes And No Are Avaliable Options")
                                            elif option2 in list_menu_3b:
                                                print("Exiting...")
                                                break
                                        else:
                                            print("Only interger b/w 1 to 7 are allowed!")
#-------------------------------------------------------------------------------------------------
                                    elif option1 == 3:
                                        print("Select the currency you want to convert into!")
                                        image()
                                        option2 = input()
                                        if option2.isdigit():
                                            option2 = int(option2)
                                            if option2 in list_menu_3a:
                                                currency1,currency2 = User_selected_choice(option,option2)
                                                while True:
                                                    yes_no = input(f"Are You Sure You want to convert {currency1} to {currency2}(yes/no)?\n").capitalize().strip()
                                                    if yes_no == "Yes":
                                                        try:
                                                            currency = input(f"Enter the amount of {currency1} you want to convert: ")
                                                            try:
                                                                total_currency = currency * 1
                                                                History[First_name].append(f"{First_name} converted {currency} {currency1} to {total_currency} {currency2}")
                                                                print(History)
                                                                Condition_while_exit_menu_3 = True
                                                                break
                                                            except:
                                                                print("Invalid Input! Error: 555")
                                                        except:
                                                             print("Invalid Input!")
                                                    elif yes_no == "No":
                                                        Condition_while_exit_menu_3 = True
                                                        break
                                                    else:
                                                        print("Only Yes And No Are Avaliable Options")
                                            elif option2 in list_menu_3b:
                                                print("Exiting...")
                                                break
                                        else:
                                            print("Only interger b/w 1 to 7 are allowed!")
#-------------------------------------------------------------------------------------------------
                                    elif option1 == 4:
                                        print("Select the currency you want to convert into!")
                                        image()
                                        option2 = input()
                                        if option2.isdigit():
                                            option2 = int(option2)
                                            if option2 in list_menu_3a:
                                                currency1,currency2 = User_selected_choice(option,option2)
                                                while True:
                                                    yes_no = input(f"Are You Sure You want to convert {currency1} to {currency2}(yes/no)?\n").capitalize().strip()
                                                    if yes_no == "Yes":
                                                        try:
                                                            currency = input(f"Enter the amount of {currency1} you want to convert: ")
                                                            try:
                                                                total_currency = currency * 1
                                                                History[First_name].append(f"{First_name} converted {currency} {currency1} to {total_currency} {currency2}")
                                                                print(History)
                                                                Condition_while_exit_menu_3 = True
                                                                break
                                                            except:
                                                                print("Invalid Input! Error: 555")
                                                        except:
                                                             print("Invalid Input!")
                                                    elif yes_no == "No":
                                                        Condition_while_exit_menu_3 = True
                                                        break
                                                    else:
                                                        print("Only Yes And No Are Avaliable Options")
                                            elif option2 in list_menu_3b:
                                                print("Exiting...")
                                                break
                                        else:
                                            print("Only interger b/w 1 to 7 are allowed!")
#-------------------------------------------------------------------------------------------------
                                    elif option1 == 5:
                                        print("Select the currency you want to convert into!")
                                        image()
                                        option2 = input()
                                        if option2.isdigit():
                                            option2 = int(option2)
                                            if option2 in list_menu_3a:
                                                currency1,currency2 = User_selected_choice(option,option2)
                                                while True:
                                                    yes_no = input(f"Are You Sure You want to convert {currency1} to {currency2}(yes/no)?\n").capitalize().strip()
                                                    if yes_no == "Yes":
                                                        try:
                                                            currency = input(f"Enter the amount of {currency1} you want to convert: ")
                                                            try:
                                                                total_currency = currency * 1
                                                                History[First_name].append(f"{First_name} converted {currency} {currency1} to {total_currency} {currency2}")
                                                                print(History)
                                                                Condition_while_exit_menu_3 = True
                                                                break
                                                            except:
                                                                print("Invalid Input! Error: 555")
                                                        except:
                                                             print("Invalid Input!")
                                                    elif yes_no == "No":
                                                        Condition_while_exit_menu_3 = True
                                                        break
                                                    else:
                                                        print("Only Yes And No Are Avaliable Options")
                                            elif option2 in list_menu_3b:
                                                print("Exiting...")
                                                break
                                        else:
                                            print("Only interger b/w 1 to 7 are allowed!")
#-------------------------------------------------------------------------------------------------
                                    elif option1 == 6:
                                        print("Select the currency you want to convert into!")
                                        image()
                                        option2 = input()
                                        if option2.isdigit():
                                            option2 = int(option2)
                                            if option2 in list_menu_3a:
                                                currency1,currency2 = User_selected_choice(option,option2)
                                                while True:
                                                    yes_no = input(f"Are You Sure You want to convert {currency1} to {currency2}(yes/no)?\n").capitalize().strip()
                                                    if yes_no == "Yes":
                                                        try:
                                                            currency = input(f"Enter the amount of {currency1} you want to convert: ")
                                                            try:
                                                                total_currency = currency * 1
                                                                History[First_name].append(f"{First_name} converted {currency} {currency1} to {total_currency} {currency2}")
                                                                print(History)
                                                                Condition_while_exit_menu_3 = True
                                                                break
                                                            except:
                                                                print("Invalid Input! Error: 555")
                                                        except:
                                                             print("Invalid Input!")
                                                    elif yes_no == "No":
                                                        Condition_while_exit_menu_3 = True
                                                        break
                                                    else:
                                                        print("Only Yes And No Are Avaliable Options")
                                            elif option2 in list_menu_3b:
                                                print("Exiting...")
                                                break
                                        else:
                                            print("Only interger b/w 1 to 7 are allowed!")
#-------------------------------------------------------------------------------------------------
                                    elif option1 == 7:
                                        while True:
                                            yes_no = input("Do you want to exit(yes/no)?\n").capitalize().strip()
                                            if yes_no == "Yes":
                                                print("Exiting...")
                                                Condition_while_exit_menu_2 = True
                                                break
                                            elif yes_no == "No":
                                                print("Staying...")
                                                break
                                            else:
                                                print("Only Option Avaliable Are Yes And No!")
                                        if Condition_while_exit_menu_2:
                                            Condition_while_exit_menu_2 = False
                                            break
                                    else:
                                        print("Invalid Input!")
                                    if Condition_while_exit_menu_3:
                                        Condition_while_exit_menu_3 = False
                                        break
                            except:
                                print("Invalid Input! Error: Unknown Entry")
#_________________________________________________________________________________________________
                    elif option == 2:
                        for key, value in dict.items(History):
                            print(f"{key} => {value}")
#_________________________________________________________________________________________________
                    elif option == 3:
                        while True:
                            User_name_delete = input("Enter the name you want to delete from database: ")
                            if History[User_name_delete] in History:
                                yes_no = input(f"Do you want to Delete the database of {User_name_delete}(yes/no)?").capitalize().strip()
                                if yes_no == "Yes":
                                    History.pop(User_name_delete, "Error: 411!")
                                    print(f"All Info of {User_name_delete} has been deleted successfully!")
                                    break
                                elif yes_no == "No":
                                    print("Taking back to main screen!")
                                    break
                                else:
                                    print("Only Yes and No are avaliable for options!")
                            else:
                                print(f"{User_name_delete} does not exists in database")
                                break
#_________________________________________________________________________________________________
                    elif option == 4:
                        while True:
                            yes_no = input("Are You Sure You Want To Exit This Beautiful System(yes/no)?\n").capitalize().split()
                            if yes_no == "Yes": 
                                print("Thank you for visiting my code!")
                                print("Exiting...")
                                Condition_while_exit_menu_1 = True
                                break
                            elif yes_no == "No":
                                print("Thanks for staying!")
                                break
                            else:
                                print("Only Avaliable Options Are Yes And No!")
                        if Condition_while_exit_menu_1:
                            break
                    else:
                        print("Only Avaliable Options Are b/w 1 to 4.")
                else:
                    print("Only Integers are allowed! Error 001")
            except:
                print("Invalid Input!")
#_________________________________________________________________________________________________
    else:
        print(f"Welcome back {First_name}")
        while True:
            option = input("\n+-------------------------------------+\n| To Convert Currency     : Enter [1] |\n| To View Currency History: Enter [2] |\n| To Clear History        : Enter [3] |\n| To Exit                 : Enter [4] |\n+-------------------------------------+\n")
            try:
                if option.isdigit():
                    option = int(option)
#-------------------------------------------------------------------------------------------------
                    if option == 1:
                        while True:
                            print("\nWhich currency Do you have?")
                            image1()
                            option1 = input()
                            try:
                                if option1.isdigit():
                                    option1 = int(option1)
#-------------------------------------------------------------------------------------------------
                                    if option1 == 1:
                                        print("Select the currency you want to convert into!")
                                        image()
                                        option2 = input()
                                        if option2.isdigit():
                                            option2 = int(option2)
                                            if option2 in list_menu_3a:
                                                currency1,currency2 = User_selected_choice(option,option2)
                                                while True:
                                                    yes_no = input(f"Are You Sure You want to convert {currency1} to {currency2}(yes/no)?\n").capitalize().strip()
                                                    if yes_no == "Yes":
                                                        try:
                                                            currency = input(f"Enter the amount of {currency1} you want to convert: ")
                                                            try:
                                                                total_currency = currency * 1
                                                                History[First_name].append(f"{First_name} converted {currency} {currency1} to {total_currency} {currency2}")
                                                                print(History)
                                                                Condition_while_exit_menu_3 = True
                                                                break
                                                            except:
                                                                print("Invalid Input! Error: 555")
                                                        except:
                                                             print("Invalid Input!")
                                                    elif yes_no == "No":
                                                        Condition_while_exit_menu_3 = True
                                                        break
                                                    else:
                                                        print("Only Yes And No Are Avaliable Options")
                                            elif option2 in list_menu_3b:
                                                print("Exiting...")
                                                break
                                        else:
                                            print("Only interger b/w 1 to 7 are allowed!")
#-------------------------------------------------------------------------------------------------
                                    elif option1 == 2:
                                        print("Select the currency you want to convert into!")
                                        image()
                                        option2 = input()
                                        if option2.isdigit():
                                            option2 = int(option2)
                                            if option2 in list_menu_3a:
                                                currency1,currency2 = User_selected_choice(option,option2)
                                                while True:
                                                    yes_no = input(f"Are You Sure You want to convert {currency1} to {currency2}(yes/no)?\n").capitalize().strip()
                                                    if yes_no == "Yes":
                                                        try:
                                                            currency = input(f"Enter the amount of {currency1} you want to convert: ")
                                                            try:
                                                                total_currency = currency * 1
                                                                History[First_name].append(f"{First_name} converted {currency} {currency1} to {total_currency} {currency2}")
                                                                print(History)
                                                                Condition_while_exit_menu_3 = True
                                                                break
                                                            except:
                                                                print("Invalid Input! Error: 555")
                                                        except:
                                                             print("Invalid Input!")
                                                    elif yes_no == "No":
                                                        Condition_while_exit_menu_3 = True
                                                        break
                                                    else:
                                                        print("Only Yes And No Are Avaliable Options")
                                            elif option2 in list_menu_3b:
                                                print("Exiting...")
                                                break
                                        else:
                                            print("Only interger b/w 1 to 7 are allowed!")
#-------------------------------------------------------------------------------------------------
                                    elif option1 == 3:
                                        print("Select the currency you want to convert into!")
                                        image()
                                        option2 = input()
                                        if option2.isdigit():
                                            option2 = int(option2)
                                            if option2 in list_menu_3a:
                                                currency1,currency2 = User_selected_choice(option,option2)
                                                while True:
                                                    yes_no = input(f"Are You Sure You want to convert {currency1} to {currency2}(yes/no)?\n").capitalize().strip()
                                                    if yes_no == "Yes":
                                                        try:
                                                            currency = input(f"Enter the amount of {currency1} you want to convert: ")
                                                            try:
                                                                total_currency = currency * 1
                                                                History[First_name].append(f"{First_name} converted {currency} {currency1} to {total_currency} {currency2}")
                                                                print(History)
                                                                Condition_while_exit_menu_3 = True
                                                                break
                                                            except:
                                                                print("Invalid Input! Error: 555")
                                                        except:
                                                             print("Invalid Input!")
                                                    elif yes_no == "No":
                                                        Condition_while_exit_menu_3 = True
                                                        break
                                                    else:
                                                        print("Only Yes And No Are Avaliable Options")
                                            elif option2 in list_menu_3b:
                                                print("Exiting...")
                                                break
                                        else:
                                            print("Only interger b/w 1 to 7 are allowed!")
#-------------------------------------------------------------------------------------------------
                                    elif option1 == 4:
                                        print("Select the currency you want to convert into!")
                                        image()
                                        option2 = input()
                                        if option2.isdigit():
                                            option2 = int(option2)
                                            if option2 in list_menu_3a:
                                                currency1,currency2 = User_selected_choice(option,option2)
                                                while True:
                                                    yes_no = input(f"Are You Sure You want to convert {currency1} to {currency2}(yes/no)?\n").capitalize().strip()
                                                    if yes_no == "Yes":
                                                        try:
                                                            currency = input(f"Enter the amount of {currency1} you want to convert: ")
                                                            try:
                                                                total_currency = currency * 1
                                                                History[First_name].append(f"{First_name} converted {currency} {currency1} to {total_currency} {currency2}")
                                                                print(History)
                                                                Condition_while_exit_menu_3 = True
                                                                break
                                                            except:
                                                                print("Invalid Input! Error: 555")
                                                        except:
                                                             print("Invalid Input!")
                                                    elif yes_no == "No":
                                                        Condition_while_exit_menu_3 = True
                                                        break
                                                    else:
                                                        print("Only Yes And No Are Avaliable Options")
                                            elif option2 in list_menu_3b:
                                                print("Exiting...")
                                                break
                                        else:
                                            print("Only interger b/w 1 to 7 are allowed!")
#-------------------------------------------------------------------------------------------------
                                    elif option1 == 5:
                                        print("Select the currency you want to convert into!")
                                        image()
                                        option2 = input()
                                        if option2.isdigit():
                                            option2 = int(option2)
                                            if option2 in list_menu_3a:
                                                currency1,currency2 = User_selected_choice(option,option2)
                                                while True:
                                                    yes_no = input(f"Are You Sure You want to convert {currency1} to {currency2}(yes/no)?\n").capitalize().strip()
                                                    if yes_no == "Yes":
                                                        try:
                                                            currency = input(f"Enter the amount of {currency1} you want to convert: ")
                                                            try:
                                                                total_currency = currency * 1
                                                                History[First_name].append(f"{First_name} converted {currency} {currency1} to {total_currency} {currency2}")
                                                                print(History)
                                                                Condition_while_exit_menu_3 = True
                                                                break
                                                            except:
                                                                print("Invalid Input! Error: 555")
                                                        except:
                                                             print("Invalid Input!")
                                                    elif yes_no == "No":
                                                        Condition_while_exit_menu_3 = True
                                                        break
                                                    else:
                                                        print("Only Yes And No Are Avaliable Options")
                                            elif option2 in list_menu_3b:
                                                print("Exiting...")
                                                break
                                        else:
                                            print("Only interger b/w 1 to 7 are allowed!")
#-------------------------------------------------------------------------------------------------
                                    elif option1 == 6:
                                        print("Select the currency you want to convert into!")
                                        image()
                                        option2 = input()
                                        if option2.isdigit():
                                            option2 = int(option2)
                                            if option2 in list_menu_3a:
                                                currency1,currency2 = User_selected_choice(option,option2)
                                                while True:
                                                    yes_no = input(f"Are You Sure You want to convert {currency1} to {currency2}(yes/no)?\n").capitalize().strip()
                                                    if yes_no == "Yes":
                                                        try:
                                                            currency = input(f"Enter the amount of {currency1} you want to convert: ")
                                                            try:
                                                                total_currency = currency * 1
                                                                History[First_name].append(f"{First_name} converted {currency} {currency1} to {total_currency} {currency2}")
                                                                print(History)
                                                                Condition_while_exit_menu_3 = True
                                                                break
                                                            except:
                                                                print("Invalid Input! Error: 555")
                                                        except:
                                                             print("Invalid Input!")
                                                    elif yes_no == "No":
                                                        Condition_while_exit_menu_3 = True
                                                        break
                                                    else:
                                                        print("Only Yes And No Are Avaliable Options")
                                            elif option2 in list_menu_3b:
                                                print("Exiting...")
                                                break
                                        else:
                                            print("Only interger b/w 1 to 7 are allowed!")
#-------------------------------------------------------------------------------------------------
                                    elif option1 == 7:
                                        while True:
                                            yes_no = input("Do you want to exit(yes/no)?\n").capitalize().strip()
                                            if yes_no == "Yes":
                                                print("Exiting...")
                                                Condition_while_exit_menu_2 = True
                                                break
                                            elif yes_no == "No":
                                                print("Staying...")
                                                break
                                            else:
                                                print("Only Option Avaliable Are Yes And No!")
                                        if Condition_while_exit_menu_2:
                                            Condition_while_exit_menu_2 = False
                                            break
                                    else:
                                        print("Invalid Input!")
                                    if Condition_while_exit_menu_3:
                                        Condition_while_exit_menu_3 = False
                                        break
                            except:
                                print("Invalid Input! Error: Unknown Entry")
#_________________________________________________________________________________________________
                    elif option == 2:
                        for key, value in dict.items(History):
                            print(f"{key} => {value}")
#_________________________________________________________________________________________________
                    elif option == 3:
                        while True:
                            User_name_delete = input("Enter the name you want to delete from database: ")
                            if History[User_name_delete] in History:
                                yes_no = input(f"Do you want to Delete the database of {User_name_delete}(yes/no)?").capitalize().strip()
                                if yes_no == "Yes":
                                    History.pop(User_name_delete, "Error: 411!")
                                    print(f"All Info of {User_name_delete} has been deleted successfully!")
                                    break
                                elif yes_no == "No":
                                    print("Taking back to main screen!")
                                    break
                                else:
                                    print("Only Yes and No are avaliable for options!")
                            else:
                                print(f"{User_name_delete} does not exists in database")
                                break
#_________________________________________________________________________________________________
                    elif option == 4:
                        while True:
                            yes_no = input("Are You Sure You Want To Exit This Beautiful System(yes/no)?\n").capitalize().split()
                            if yes_no == "Yes": 
                                print("Thank you for visiting my code!")
                                print("Exiting...")
                                Condition_while_exit_menu_1 = True
                                break
                            elif yes_no == "No":
                                print("Thanks for staying!")
                                break
                            else:
                                print("Only Avaliable Options Are Yes And No!")
                        if Condition_while_exit_menu_1:
                            break
                    else:
                        print("Only Avaliable Options Are b/w 1 to 4.")
                else:
                    print("Only Integers are allowed! Error 001")
            except:
                print("Invalid Input!")
