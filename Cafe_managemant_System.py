# Create menu using a Dictionary
menu = {
    'coffee': 50,
    'pizza': 100,
    'burger': 50,
    'tea': 30,
    'noodle': 25
}

print("Welcome to Desi Restaurant")

# Print menu using a loop
print("Menu:")
for item, price in menu.items():
    print(f"{item.title()} : Rs {price}")

total_order = 0
ordered_item = []

# Accept order
item_1 = input("Enter the name of item to order: ").lower()
if item_1 in menu:
    total_order += menu[item_1]
    ordered_item.append(item_1)
    print(f"Your order for {item_1} has been accepted.")
else:
    print(f"{item_1} is not currently available in store.")

# Check if the customer wants to order another item
while True:
    another_order = input("Do you need another item (yes/no): ").lower()

    if another_order == 'yes':
        item_2 = input("Enter the next item: ").lower()
        if item_2 in menu:
            total_order += menu[item_2]
            ordered_item.append(item_2)
            print(f"Adding {item_2} to your order.")
        else:
            print(f"{item_2} is not currently available in store.")
    else:
        break

#print the order items list
print('Your order list:')
for item in ordered_item:
    print(f"{item.title()}: Rs {menu[item]}")
        
# Print the total price
print(f"Your total order price is Rs {total_order}.")
print("Thank you for ordering. Please wait.")