# Create menu use Dictionary
menu = {
    'masala tea': 20,
    'elachi tea': 15,
    'black tea': 20,
    'lemon tea': 10,
    'special tea': 25
}

print("Welcome to Desi Chai Store")

#  print menu using loop
print("Menu:")
for tea, price in menu.items():
    print(f"{tea.title()} : Rs{price}")

total_order = 0

# oder accpet
item_1 = input("Enter the name of tea to order: ").lower()
if item_1 in menu:
    total_order += menu[item_1]
    print(f"Your order for {item_1} has been accepted.")
else:
    print(f"{item_1} is not currently available in the tea store.")

extra_cup = input("Do you need extra cups (yes/no): ").lower()
# how many total oder
if extra_cup == 'yes':
    cups = int(input("Enter how many extra cups you need: "))
    if cups > 0:
        total_order += cups * menu[item_1]
        print(f"Adding {cups} extra cups to your order.")
    else:
        print("Invalid number of cups.")
else:
    print("No extra cups added.")

#print the price 
print(f"Your total order for {item_1} is price Rs{total_order}.")
print("Thank you for ordering.\nPlease wait.")
