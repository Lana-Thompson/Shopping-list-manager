# importing menu displays from the menu file
from menu import show_menu


def start_app():
    print("Welcome to the Shopping List Manager!")
    show_menu()
    print("\nGoodbye!")


if __name__ == "__main__":
    start_app()
