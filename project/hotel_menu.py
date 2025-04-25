from typing import Dict

menu: Dict[str, int] = {
    'Pasta': 40,
    'Pizza': 60,
    'Coffee':70,
    'Salad': 50
}

print("Welcome to Restaurant!")
print("Pasta: Rs 40\nPizza: Rs 60\nCoffee: Rs 70\nSalad: Rs 50")
total_order: int = 0
item_1 = input("What you want to order?")
if item_1 in menu:
    total_order += menu[item_1]
    print(f"Your item {item_1} has been added to your order.")
else:
    print(f"ordered item {item_1} is not available.")
another_item = input("Do you want to add another item? Yes/No")
if another_item == "Yes":
    item_2 = input("Enter the name of the order:")
    if item_2 in menu:
        total_order += menu[item_2]
        print(f"your order{item_2} has been added to your order.")
    else:
        print(f"your order{item_2} is not available")
print(f"Total amount of orders to pay is {total_order}")




