# Creating a file to display the users options for the shopping list
# Importing shopping list from the data file

import os

from tasks import view_list, adding_items, removing_items, clear_items, save_list


def list_choices():
    while True:
        print("What would you like to shop for today? \n")
        print("1) Groceries")
        print("2) Beauty/Health")
        print("3) Household Supplies")

        choice = input("\nSelect an action (Enter 1-3): ").strip()

        if choice == "1":
            return "grocery"
        elif choice == "2":
            return "beauty_health"
        elif choice == "3":
            return "house_supplies"
        else:
            print(f"{choice} is not a valid selection. Please try again.")


def show_menu(shopping_list, filename):
    while True:
        print("\nMenu: ")

        #  Shopping list display options
        print("1) Add an item to your shopping list")
        print("2) Remove an item from your shopping list")
        print("3) View your shopping list")
        print("4) Switch shopping lists")
        print("5) Clear current shopping list")
        print("6) Exit shopping list manager")

        #    Ask for user selection and print out their choice
        choice = input("\nSelect an action (Enter 1-6): ").strip()

        if choice == "1":
            adding_items(shopping_list)
        elif choice == "2":
            removing_items(shopping_list)
        elif choice == "3":
            view_list(shopping_list)
        elif choice == "4":
            return
        elif choice == "5":
            clear_items(shopping_list)
        elif choice == "6":
            return "exit"
        else:
            print(f"{choice} is not a valid selection. Please try again.")

        input("\nPress Enter to continue...")

        save_list(shopping_list, filename)
        # Clear the output so that the "rounds" of messages don't pile up
        os.system("clear")
