import pytest

from src.shopping_data import view_list, add_items, remove_items, clear_items


@pytest.fixture
def shopping_list():
    """A fresh list for every test, so one test can't affect another."""
    return [
        {"name": "apple", "quantity": 2, "price": 1.50},
        {"name": "bread", "quantity": 1, "price": 3.00},
    ]


# view_list


def test_view_list_prints_a_message_when_the_list_is_empty(capsys):
    view_list([])

    assert capsys.readouterr().out == (
        "You're shopping list is empty right now, select option 1 to add some items!\n"
    )


def test_view_list_prints_each_item_and_the_totals(shopping_list, capsys):
    view_list(shopping_list)

    assert capsys.readouterr().out == (
        " - 2 apples: $3.00\n - 1 breads: $3.00\nTotal Items: 3\nTotal Price: $6.00\n"
    )


# add_items


def test_add_items_appends_a_new_item(shopping_list):
    add_items(shopping_list, "orange", "0.75", "3")

    assert len(shopping_list) == 3
    assert shopping_list[-1] == {"name": "orange", "quantity": 3, "price": 0.75}


def test_adding_an_existing_item_increases_its_quantity_without_adding_a_duplicate(
    shopping_list,
):
    add_items(shopping_list, "apple", "1.50", "3")

    assert len(shopping_list) == 2
    assert shopping_list[0]["quantity"] == 5


# remove_items


def test_removing_some_of_an_item_lowers_its_quantity(shopping_list, capsys):
    remove_items(shopping_list, "apple", "1")

    assert shopping_list[0] == {"name": "apple", "quantity": 1, "price": 1.50}
    assert capsys.readouterr().out == "You've removed 1 apple from your list!\n"


def test_removing_the_full_quantity_removes_the_item(shopping_list, capsys):
    remove_items(shopping_list, "apple", "2")

    assert shopping_list == [{"name": "bread", "quantity": 1, "price": 3.00}]
    assert capsys.readouterr().out == "You've removed apples from your list!\n"


# clear_items


def test_clear_items_removes_every_item(shopping_list):
    clear_items(shopping_list)

    assert shopping_list == []


def test_clear_items_prints_a_confirmation(shopping_list, capsys):
    clear_items(shopping_list)

    assert capsys.readouterr().out == "\nShopping list cleared!\n"
