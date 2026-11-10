# Project Overview

This project is an easy-to-use command-line shopping list manager. The user can add, remove, and view items in a groceries, beauty/health, or household supplies shopping list. Each list is saved to its own JSON file, so items are still there the next time the program is run.

## Key Features & Usage Example

When the user runs the application, they are presented with the option to work with a grocery list, a beauty/health list, or a household supplies list. After selecting a list, the user can:

1. Add a new item to their shopping list
2. Remove an item from their shopping list
3. View the current items in the shopping list
4. Switch shopping lists
5. Clear the current shopping list
6. Exit the shopping list manager


## Setup

Follow these steps to get started with the project:

```sh
git clone git@github.com:Lana-Thompson/Shopping-list-manager.git
cd Shopping-list-manager

# Create a virtual environment in a folder named .venv, then turn it on
python3 -m venv .venv
source .venv/bin/activate

# Install pytest into the virtual environment
pip install pytest

# Run the application
python3 src/main.py

# If you need to end the program abruptly, use Control+D
```

## Key Technologies & Packages

- Python 3
- `input()` and `print()` from the built-in functions
- The `json` module from the standard library
- `pytest`