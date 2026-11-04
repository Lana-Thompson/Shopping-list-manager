# importing menu displays from the menu file
from menu import show_menu


def start_app():
    print("Welcome to you personal Shopping List Manager!")
    show_menu()
    print("\nHave a great day!")


if __name__ == "__main__":
    start_app()
