shopping_list = [
    {
        "name": "apples",
        "quantity": 3,
        "price": 0.5,
    },
    {
        "name": "carton of 12 eggs",
        "quantity": 3,
        "price": 7.99,
    },
]


def view_list():

    quantity_count = sum([items["quantity"] for items in shopping_list])
    price_count = sum([items["price"] * items["quantity"] for items in shopping_list])

    for items in shopping_list:
        print(
            f" - {items['quantity']} {items['name']}: ${items['quantity'] * items['price']:.2f}"
        )

    print(f"Total Items: {quantity_count}")
    print(f"Total Price: ${price_count:.2f}")
