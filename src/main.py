# importing menu displays from the menu file
from menu import show_menu, list_choices
from tasks import load_list


def start_app():
    print("Welcome to your personal Shopping List Manager!")

    while True:
        filename = list_choices()
        shopping_list = load_list(filename)
        action = show_menu(shopping_list, filename)

        if action == "exit":
            break

    print("\nHave a great day!")


if __name__ == "__main__":
    start_app()
