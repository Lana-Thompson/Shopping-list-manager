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
def getting_valid_quantity(item_name):

    if item_name[-1] == "s":
        item_name = item_name[:-1]

    while True:
        item_quantity = input(f"How many {item_name}s ? ").strip()

        if item_quantity.isdigit() == True:
            break
        else:
            print("\nPlease enter a valid amount.")

    return item_quantity


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

    quantity_count = sum([items["quantity"] for items in shopping_list])
    price_count = sum([items["price"] * items["quantity"] for items in shopping_list])

    print(f"Total Items: {quantity_count}")
    print(f"Total Price: ${price_count:.2f}")


def adding_items(shopping_list):

    # collecting user input on item descriptions
    while True:
        item_name = input("\nWhats the name of the item: ").strip().lower()

        if item_name == "":
            print("\nPlease enter an item name.")
            continue
        else:
            break

    if item_name[-1] == "s":
        item_name = item_name[:-1]

    # if item already exists the quantity is increased by 1
    for items in shopping_list:
        if item_name == items["name"]:
            items["quantity"] += 1
            print(f"You've added 1 more {item_name} to your shopping list")
            return

    # Only accepts ints and floats as user input for price
    while True:
        item_price = (input(f"How much do {item_name}s cost: $")).strip()

        try:
            float(item_price)
            break
        except ValueError:
            print("\nPlease enter a valid price..")
            continue

    # Only accepts numbers as input for quantities
    item_quantity = getting_valid_quantity(item_name)

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


def removing_items(shopping_list):

    if len(shopping_list) == 0:
        print(
            "You're shopping list is empty right now, select option 1 to add some items!"
        )
        return

    while True:
        item_name = input("What item would you like to remove? ").strip().lower()

        if item_name[-1] == "s":
            item_name = item_name[:-1]

        item = next(
            (items for items in shopping_list if items["name"] == item_name), None
        )

        if item == None:
            print("\nThat items not currently in your list. Please try again")
            continue

        else:
            while True:
                item_quantity = getting_valid_quantity(item_name)

                if item["quantity"] < int(item_quantity):
                    print(
                        "\nThe amount of items you want to remove is too large. Please try again."
                    )
                    continue

                if item["quantity"] == int(item_quantity):
                    shopping_list.remove(item)
                    print(f"You've removed {item_name}s from your list!")
                    break

                if item["quantity"] > int(item_quantity):
                    item["quantity"] -= int(item_quantity)
                    print(
                        f"You've removed {item_quantity} {item_name}{'s' if int(item_quantity) > 1 else ''} from your list!"
                    )
                    break

        break


def clear_items(shopping_list):
    shopping_list.clear()

    print("\nShopping list cleared!")
