import json


# this function is used to save any changes made to the lists
def save_list(shopping_list, filename):
    with open(f"{filename}.json", "w") as file:
        json.dump(shopping_list, file, indent=4)


# This function reloads the most current version of the shopping lists every time the program is run
def load_list(filename):
    try:
        with open(f"{filename}.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []


# Helper function for getting a valid quantity from users
def get_valid_quantity(item_name):

    while True:
        item_quantity = input(f"How many {item_name}s ? ").strip()

        if item_quantity.isdigit():
            break
        else:
            print("\nPlease enter a valid amount.")

    return item_quantity


# Helper function for getting valid item name from users
def get_valid_item_name():

    while True:
        item_name = input("Whats the name of the item: ").strip().lower()

        if item_name == "" or item_name.isdigit():
            print("\nPlease enter an item name.")
            continue
        else:
            if item_name[-1] == "s":
                item_name = item_name[:-1]
            return item_name


def get_valid_item_price(item_name):
    while True:
        item_price = (input(f"How much do {item_name}s cost: $")).strip()

        try:
            float(item_price)
            break
        except ValueError:
            print("\nPlease enter a valid price..")
            continue
    return item_price


# Allows user to view their current shopping list
def view_list(shopping_list):

    # checking for an empty list
    if len(shopping_list) == 0:
        print(
            "You're shopping list is empty right now, select option 1 to add some items!"
        )
        return

    for items in shopping_list:
        print(
            f" - {items['quantity']} {items['name']}s: ${items['quantity'] * items['price']:.2f}"
        )

    # calculating the sum of the quantity of items as well as the prices
    quantity_count = sum([items["quantity"] for items in shopping_list])
    price_count = sum([items["price"] * items["quantity"] for items in shopping_list])

    print(f"Total Items: {quantity_count}")
    print(f"Total Price: ${price_count:.2f}")


# Allows user to add item to their current shopping lis
def add_items(shopping_list, item_name, item_price, item_quantity):

    # if item already exists the quantity is increased by 1
    for items in shopping_list:
        if item_name == items["name"]:
            items["quantity"] += int(item_quantity)
            print(
                f"You've added {item_quantity} more {item_name} to your shopping list"
            )
            return

    # Adding the items into the shopping list
    item = {
        "name": item_name,
        "quantity": int(item_quantity),
        "price": float(item_price),
    }
    shopping_list.append(item)

    print(
        f"\nYou've added {item_quantity} {item_name}{'s' if int(item_quantity) > 1 else ''} to your list!"
    )


# Allows user to remove items from current shopping list
def remove_items(shopping_list, item_name, item_quantity):

    item = next((items for items in shopping_list if items["name"] == item_name), None)

    if item == None:
        print("\nThat items not currently in your list. Please try again")

    else:
        if item["quantity"] < int(item_quantity):
            print(
                "\nThe amount of items you want to remove is too large. Please try again."
            )

        if item["quantity"] == int(item_quantity):
            shopping_list.remove(item)
            print(f"You've removed {item_name}s from your list!")

        if item["quantity"] > int(item_quantity):
            item["quantity"] -= int(item_quantity)
            print(
                f"You've removed {item_quantity} {item_name}{'s' if int(item_quantity) > 1 else ''} from your list!"
            )


# This allows the user to clear their shopping list
def clear_items(shopping_list):
    shopping_list.clear()

    print("\nShopping list cleared!")
