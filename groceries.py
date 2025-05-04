# open file to read the data
# .splitlines( ) is to splits a string into a list
with open("usernames.txt", "r") as f:
    usernames = f.read().splitlines()
with open("passwords.txt", "r") as f:
    passwords = f.read().splitlines()
with open("ordered_items.txt", "r") as f:
    ordered_items = [line.split(', ') if line != 'None' else [] for line in f.read().splitlines()]  # nested list
with open("personal_info.txt", 'r') as f:
    personal_info = f.read().splitlines()

# print(usernames, passwords, ordered_items, personal_info)

# stores the available groceries and their details
# which can be managed by admin
with open("groceries_lists.txt", "r") as f:
    groceries = f.read().splitlines()

# print(groceries)


def upload_data():
    # upload all the new data to the files when they exit so that data is saved for next run of code too
    with open("usernames.txt", "w") as f:
        f.write("\n".join(usernames))
    with open("passwords.txt", "w") as f:
        f.write("\n".join(passwords))
    with open("ordered_items.txt", "w") as f:
        f.write("\n".join([", ".join(i) if i else 'None' for i in ordered_items]))  # nested list
    with open("groceries_lists.txt", "w") as f:
        f.write("\n".join(groceries))
    with open("personal_info.txt", 'w') as f:
        f.write("\n".join(personal_info))


# upload groceries detail for admin system
def upload():
    print()
    print("******************** Upload Items ********************")
    # input from user 
    up_gro_name = input("Enter item name: ").lower()
    up_gro_exp = input("Enter exp date (dd/mm/yyyy): ")
    up_gro_price = input("Enter price: ")
    up_gro_spe = input("Enter specification: ")
    # append to groceries file
    groceries.append(f"Name: {up_gro_name} | Expiry: {up_gro_exp} | Price: {up_gro_price} | Specification: {up_gro_spe}")
    print("Added item to groceries!")


# view groceries for all the system (admin & new customer & registered customer)
def view():
    print()
    print("******************** View Items ********************")
    for item in groceries:
        print(item)
        print()

# print groceries 


# function for admin to modify grocery items
def modify():
    print("")
    print("******************** Modify Items ********************")
    item_found = False
    while True:
    # input from user for modify grocery item
        item_modify = input("Which item you want to modify? ").lower()
        for item in groceries:
            itemname = ""
            start = False
            # get name of grocery item
            for char in item:
                if char == " ":
                    if start: # print item not found, please retry and ask for input again
                        break
                    else:
                        start = True
                        continue
                if start:
                    itemname += char
            if itemname.lower() == item_modify:
                index = groceries.index(item)
                item_found = True
                break

        # stop infinite while loop
        if item_found:
            break
        else:
            print("Item not found, please retry")
    up_gro_name = input("Enter item's new name: ").lower()
    up_gro_exp = input("Enter new exp date (dd/mm/yyyy): ")
    up_gro_price = input("Enter new price: ")
    up_gro_spe = input("Enter new specification: ")
    # modify groceries list
    groceries[index] = f"Name: {up_gro_name} | Expiry: {up_gro_exp} | Price: {up_gro_price} | Specification: {up_gro_spe}"
    print("Modified Item!")

    
# delete groceries in the groceries_lists
def delete():
    print("")
    print("******************** Delete Items ********************")
    item_found = False
    while True:
        deleteitem = input("Which item you want to delete? ").lower()
        # remove line that contain the deleteitem
        for item in groceries.copy():  # can't loop from list that changing size
            itemname = ""
            start = False
            # get name of grocery item
            for char in item:
                if char == " ":
                    if start:
                        break
                    else:
                        start = True
                        continue
                if start:
                    itemname += char

            if itemname.lower() == deleteitem:  # Name: Oranges\nDetails: ... # [Name: Oranges, Details] # [Name:, Oranges] # Oranges
                groceries.remove(item)
                print("Deleted!")
                item_found = True
                break
        # stop infinite while loop
        if item_found:
            break
        else:
            print("item not found")


# search groceries for admin system
def search():
    print("")
    print("******************** Search Items ********************")
    item_found = False
    while True:
        s_word = input("Enter item you want to search: ").lower()
        for item in groceries:
            itemname = ""
            start = False
            # get name of grocery item
            for char in item:
                if char == " ":
                    if start:
                        break
                    else:
                        start = True
                        continue
                if start:
                    itemname += char
            if itemname.lower() == s_word:  # Name: Oranges\nDetails: ... # [Name: Oranges, Details] # [Name:, Oranges] # Oranges
                print(item)
                item_found = True
                break
        # stop infinite while loop
        if item_found:
            break
        else:
            print("Do not have this item")


# view all customer orders for admin system
def view_customer_orders():
    print()
    print("**************** View Customer Orders ****************")
    for i in range(len(usernames)):
        print("Username:", usernames[i])
        print("Order:-")
        for item in ordered_items[i]:
            print(item)
        print()
        print()


# search customer order with customer's username for admin system 
def search_customer_order():
    print()
    print("******************** Search Orders ********************")
    # input customer username to search their order
    name = input("Enter customer name you want to search: ").lower()
    for i in range(len(usernames)):
        if usernames[i].lower() == name:
            index = i
            break
    else:
        # print if the username not found in the txt file
        print("Do not have this customer")
        return # return back to the admin system 
    print("Ordered items are:-")
    for item in ordered_items[index]:
        print(item)

        # print ordered_items the customer has ordered 


# admin system
def admin():
    print("Please Login via an administrative account To access Admin Page\ntype cancel to go back")
    # Login Loop
    while True:
        username = input("Enter username: ")
        password = input("Enter password: ")
        if username == 'cancel' or password == 'cancel':
            return # go back to the main system

        # check if username password is administrator
        # the first account entry in the accounts is always admin
        # username: admin  password: freeadmin123 
        if username == usernames[0] and password == passwords[0]:
            print("Access granted!")
            break
        else:
            print("Invalid username/password, try again...")
    # Admin Panel Loop
    while True:
        print()
        print("==================== Welcome to admin page ====================")
        print("1. Upload Groceries Detail\n2. View Groceries\n"
              "3. Upload/Modify Groceries\n4. Delete Groceries\n5. Search Groceries\n6. View All Orders\n"
              "7. Search Order\n8. Exit")
        try:
            n_admin = int(input("Enter number: "))
        except ValueError:
            print("Please enter numeric value")
            continue # ask for input again
        if n_admin == 1:
            upload() # jump to upload function
        elif n_admin == 2:
            view() # jump to view function
        elif n_admin == 3:
            modify() # jump to modify function
        elif n_admin == 4:
            delete() # jump to delete function
        elif n_admin == 5:
            search() # jump ro search function
        elif n_admin == 6:
            view_customer_orders() # jump to view_customer_orders function
        elif n_admin == 7:
            search_customer_order() # jump to search_customer_order function 
        elif n_admin == 8:
            break # return back to the main function 
        else:
            print("Error") # ask input again 


# register for new customers
def register():
    print()
    print("*************** Register ****************")
    name = input("Enter name: ").lower()
    address = input("Enter address: ")
    email = input("Enter email ID: ")
    contact = input("Enter contact number: ")
    gender = input("Enter gender: ")
    birth = input("Enter date of birth (dd/mm/yyyy): ")
    while True:
        username = input("Enter username: ")
        # check if username exists
        if username in usernames:
            print("Username already exists!")
        else:
            break
    while True:
        password = input("Enter password: ")
        password1 = input("Confirm password: ")
        # check if password1 same as password
        if password1 != password:
            print("Incorrect password")
        else:
            break
    # append all the data into the text file
    personal_info.append(f"Name: {name} | Address: {address} | Email: {email} | Contact Number: {contact} | Gender: {gender} | Date of birth: {birth}")
    usernames.append(username)
    passwords.append(password)
    ordered_items.append([])
    print("Successfully Registered!")


# new customer system
def new_customer():
    # new customer panel loop 
    while True:
        print("==================== Welcome to new customer page ====================")
        print("1. View Groceries\n2. Registration\n3. Exit")
        try:
            n_cus_num = int(input("Enter number: "))
        except ValueError:
            print("Please enter number")
            continue
        if n_cus_num == 1:
            view()
        elif n_cus_num == 2:
            register()
        elif n_cus_num == 3:
            break
        else:
            print("Error")


def place_order(username):
    index = usernames.index(username)
    view() # Display all groceries
    print()
    print("************ Place Order *************")
    order = []
    while True:
        item_name = input("Enter name of item you wish to add to your order(stop to stop): ").lower()
        if item_name == 'stop':
            break
        # check if item exists
        for item in groceries:
            itemname = ""
            start = False
            # get name of grocery item
            for char in item:
                if char == " ":
                    if start:
                        break
                    else:
                        start = True
                        continue
                if start:
                    itemname += char
            if itemname.lower() == item_name:
                # ask quantity
                quantity = int(input("Enter quantity: "))
                if quantity <= 0:
                    print("Invalid")
                else:
                # add to orders
                    order += [item]*quantity  # [1,2] + [3,4] = [1,2,3,4]
                    print("Added item to order!")
                    break
        else:
            print("item not found")

    total = 0
    for item in order:
        try:
            price = float(item.split(' | ')[2].split()[1])
        except ValueError:
            price = 0
        total += price # total up the price of the item
    print("Total:", total)
    buy_now = input("Would you like to (pay/cancel) order ").lower()
    if buy_now == 'pay':
        print("Payment done!")
        # save most recent order
        ordered_items[index] = order
    else:
        print("Cancelled payment")

        # the order will be deleted and not save to the txt file 


# registered customer order
def display_cart(username):
    print("**********", username, "Order ************")
    print("Your Order:-")
    for item in ordered_items[usernames.index(username)]: # search for the ordered_items according to their username
        print(item)
        print("-------------")


# registered customer info
def display_info(username):
    pwd = passwords[usernames.index(username)] # seach the passwords accoridng the their username
    cart_length = len(ordered_items[usernames.index(username)]) # search the number of ordered item with the length according to their username
    information = personal_info[usernames.index(username)] # search their own personal information according to their username
    print("Personal Information:", information)
    print("USERNAME:", username)
    print("PASSWORD:", pwd)
    print("CART ITEMS:", cart_length)


# registered customer system
def re_customer():
    print("Please Login To access Registered Customer Page\ntype cancel to go back")
    # Login Loop
    while True:
        username = input("Enter username: ")
        password = input("Enter password: ")
        if username == 'cancel' or password == 'cancel':
            return

        # check the username and password match with the txt file 
        if username in usernames:
            index = usernames.index(username)
            if password == passwords[index]:
                print("Access granted!")
                break

        print("Invalid username/password, try again")

    # registered customer panel loop 
    while True:
        print("==================== Welcome to registered customer page ====================")
        print("1. View Groceries\n2. Place Order\n3. View Order\n4. View Personal Information\n5. Exit")
        try:
            re_cus_num = int(input("Enter number: "))
        except ValueError:
            print("Please enter numeric value")
            continue
        if re_cus_num == 1:
            view() # jump to view function
        elif re_cus_num == 2:
            place_order(username) # jump to place_order function 
        elif re_cus_num == 3:
            display_cart(username) # jump to display_cart function
        elif re_cus_num == 4:
            display_info(username) # jump to display_info function
        elif re_cus_num == 5:
            break # return back to the main function 
        else:
            print("Error")


# main function for whole system
def main():
    while True:
        print("-------------------- Welcome to the FRESHCO --------------------")
        print("Enter 1 for admin")
        print("Enter 2 for new customer")
        print("Enter 3 for registered customer")
        print("Enter 4 for exit")
        while True:
            try:
                num = int(input("Enter number: "))
            except ValueError:
                print("Please enter a numeric value")
                continue # go back for asking input again

            if num == 1:
                admin() # jump to admin function 
                break
            elif num == 2:
                new_customer() # jump to new_customer function
                break
            elif num == 3:
                re_customer() # jump to re_customer function
                break
            elif num == 4:
                print("-------------------- Bye --------------------")
                upload_data() # upload all the data into the file when it is end 
                return
            else:
                print("Error") # ask for input again


main()
