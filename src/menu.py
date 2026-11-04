# Creating a file to display the users options for the shopping list
# Importing shopping list from the data file
from shopping_lists import shopping_list


from shopping_lists import view_list


def show_menu():
    is_running = True
    while is_running:
        print("\nMenu: ")

        #  Shopping list display options
        print("1) Add an item to your shopping list")
        print("2) Remove an item from your shopping list")
        print("3) View your shopping list")
        print("4) Exit shopping list")

        #    Ask for user selection and print out their choice
        choice = input("Select an action (Enter 1-4): ").strip()

        if choice == "1":
            print("You chose to Add an item to your shopping list")
        elif choice == "2":
            print("You chose to Remove an item from your shopping list")
        elif choice == "3":
            view_list()
        elif choice == "4":
            is_running = False
        else:
            print(f"{choice} is not a valid selection. Please try again.")
