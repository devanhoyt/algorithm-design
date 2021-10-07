shopping_cart_item = []
shopping_cart_price = []
item = ""
price = 0.00

print(" Welcome to the Shopping Cart Program!")
print("")

print("Please select one of the following:")
print("1. Add item")
print("2. View cart")
print("3. Remove item")
print("4. Compute total")
print("5. Quit")


option = int(input("Enter an option: "))

while option != 5:
    if option == 1:
        item = input("What item would you like to add? ")
        price = float(input(f"What is the price of {item}? "))
        shopping_cart_item.append(item)
        shopping_cart_price.append(price)
        print(f"{item} has been added to the cart.")
        cont = input("Would you like to add more to your cart? 1 to add more, 2 to go back to the main menu\n")
        
        if cont == "2":
            print("Please select one of the following:")
            print("1. Add item")
            print("2. View cart")
            print("3. Remove item")
            print("4. Compute total")
            print("5. Quit")
            option = int(input("Enter an option: "))
            

    elif option == 3:
        item_number = int(input("Which item number would you like to remove? "))

        shopping_cart_item.pop(item_number - 1)
        shopping_cart_price.pop(item_number - 1)
        print("Please select one of the following:")
        print("1. Add item")
        print("2. View cart")
        print("3. Remove item")
        print("4. Compute total")
        print("5. Quit")
        option = int(input("Enter an option: "))

    elif option == 2:
        for item_number in range(len(shopping_cart_item)):
            item = shopping_cart_item[item_number]
            price = shopping_cart_price[item_number]
            print(f"{item} - {price}")
        print("Please select one of the following:")
        print("1. Add item")
        print("2. View cart")
        print("3. Remove item")
        print("4. Compute total")
        print("5. Quit")
        option = int(input("Enter an option: "))

    elif option == 4:
        sum = 0
        for price in shopping_cart_price:
            sum += price
        print(f"The total is: ${sum}")
        print("Please select one of the following:")
        print("1. Add item")
        print("2. View cart")
        print("3. Remove item")
        print("4. Compute total")
        print("5. Quit")
        option = int(input("Enter an option: "))
    elif option != 5:
        print("You made a wrong entry.")
        option = int(input("Enter an option: "))
        
if option == 5:
    print("Thanks for shopping with us!")
