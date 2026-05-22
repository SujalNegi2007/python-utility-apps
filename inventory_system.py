#Text-Based Inventory & Barcode System
departments_collection_system = ("Food","Electronics","Carpentry")
barcode_collection_system = set()
store_collection_system = {}
customer_cart_system = []
print("Welcome to the Inventory & Barcode System")
while True:
    menu = input("\n+-------------------------------------------+\n| To Add New Product in the Cart: Enter [1] |\n| To View Inventory             : Enter [2] |\n| Customer Checkout Simulation  : Enter [3] |\n| To Check Avaliable Departments: Enter [4] |\n| To Exit the System            : Enter [5] |\n+-------------------------------------------+\n")
    try:
        menu = int(menu)
    #-------------------------------------------------------------------------------------------
        if menu == 1:
            barcode = input("Enter the four digit barcode of the Product: ")
            if barcode not in barcode_collection_system:
                if len(barcode) == 4:
                    if barcode.isdigit():
                        barcode_collection_system.add(barcode)
                        department = input("Enter the Name of the department: ").capitalize().strip()
                        if department in departments_collection_system:
                            product_name = input("Enter the Product Name: ").capitalize().strip()
                            product_price = input("Enter the Price of Product: ")
                            stock_level = input("Enter the Stock Level: ")
                            if stock_level.isdigit():
                                store_collection_system[barcode] = {
                                    "Product Name" : product_name,
                                    "Price"        : float(product_price),
                                    "Stock"        : int(stock_level),
                                    "Department"   : department
                                }
                            else:
                                print("Please enter valid input!")
                        else:
                            print(f"The {department} you have given does not exists in our database!")
                    else:
                        print("Invalid Enter! Only four-digit barcode is allowed.")
                else:
                    print("Invalid Enter! Only four-digit barcode is allowed.")
            else:
                print(f"This {barcode} already exists in data base.")
    #-------------------------------------------------------------------------------------------
                
        elif menu == 2:
            for key, value in store_collection_system.items():
                print(f"{key} -> {value}")
    #-------------------------------------------------------------------------------------------
        elif menu == 3:
            User_input = input("Enter The Barcode of the Product You Want To Add To Your Cart: ")
            found = False
            for row, all_items in enumerate(customer_cart_system):
                if User_input in all_items:
                    found = True
                    a = row
                    break
            if found:
                choice = input(f"{store_collection_system[User_input]["Product Name"]} is already in cart! Do you want to change the quantity or to add the quantity of {store_collection_system[User_input]["Product Name"]}? If yes then Enter yes if no then Enter no: ").capitalize().strip()
                if choice == "Yes":
                    choice1 = input(f"If you want to add the quantity of {store_collection_system[User_input]["Product Name"]} then Enter add: \nIf you want to change the quantity of {store_collection_system[User_input]["Product Name"]} then Enter change: ").capitalize().strip()
                    if choice1 == "Add":
                        choice2 = input("Enter how much quantity do you want to add: ")
                        if choice2.isdigit():
                            choice2 = int(choice2)
                            if int(choice2) <= store_collection_system[User_input]["Stock"]:
                                customer_cart_system[a][2] += choice2
                                store_collection_system[User_input]["Stock"] -= choice2
                            elif int(choice2) > store_collection_system[User_input]["Stock"]:
                                print("Sorry! We are running low on stocks!")
                        else:
                            print("Invalid Entry!")
                    elif choice1 == "Change":
                        choice2 = input(f"Enter the amount you want to change with {customer_cart_system[a][2]}: ")
                        choice2 = int(choice2)
                        if choice2 <= store_collection_system[User_input]["Stock"]:
                            if choice2 >= customer_cart_system[a][2]:
                                customer_cart_system[a][2] = int(choice2)
                            else:
                                refund_stock = customer_cart_system[a][2] - int(choice2)
                                store_collection_system[User_input]["Stock"] += refund_stock
                                customer_cart_system[a][2] = int(choice2)
                        elif choice2 > store_collection_system[User_input]["Stock"]:
                            print("Sorry! We are running low on stocks!")
                        else:
                            print("Invalid Entry!")
                    else:
                        print("Only options avaliable are add/change!")
                elif choice == "No":
                    print("Taking back to main screen...")
                    continue
                else:
                    print("Only options avaliable are yes/no!")
            
            else:
                if User_input in store_collection_system.keys():
                    print(f"Price of {store_collection_system[User_input]["Product Name"]} is {store_collection_system[User_input]["Price"]} Dollars.")
                    yes_no = input(f"Do you want to add {store_collection_system[User_input]["Product Name"] } to your cart(yes/no): ").capitalize().strip()
                    if yes_no == "Yes":
                        print(f"The {store_collection_system[User_input]["Product Name"]} has been added to your cart.")
                        try:
                            quantity = input(f"Enter the quantity of {store_collection_system[User_input]["Product Name"]} that you want to buy: ")
                            if quantity.isdigit():
                                quantity = int(quantity)
                                if quantity <= store_collection_system[User_input]["Stock"]:
                                    yes_no = input(f"Are you sure you want to add {quantity} {store_collection_system[User_input]["Product Name"]}: ").capitalize().strip()
                                    if yes_no == "Yes":
                                        customer_cart_system.append([User_input, store_collection_system[User_input]["Product Name"], quantity, store_collection_system[User_input]["Price"]])
                                        store_collection_system[User_input]["Stock"] -= quantity
                                        print(customer_cart_system)
                                    elif yes_no == "No":
                                        print("Coming back to main menu.")
                                        continue
                                    else:
                                        print("Only yes and no are avaliable options!")
                                elif quantity > store_collection_system[User_input]["Stock"]:
                                    print("Sorry, but we do not have that much in stock!")
                            else:
                                print("Please Enter integer only!")
                        except:
                            print("Some problem occured!")
                    else:
                        print("Please Enter yes or no only!")
                else:
                    print(f"{User_input} is not avaliable in our store or maybe you have entered the wrong name.")

    #-------------------------------------------------------------------------------------------
        elif menu == 4:
            print(departments_collection_system)
    #-------------------------------------------------------------------------------------------
        elif menu == 5:
            print("Thanks for visiting the site!")
            break
    #-------------------------------------------------------------------------------------------
        else:
            print(f"{menu} is not in options! Please Enter b/w 1 to 5.")
    except:
        print("Only integers are allowed!")
