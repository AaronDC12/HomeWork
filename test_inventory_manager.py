
import pytest

import inventory_manager
from inventory_manager import (
    load_inventory,
    save_inventory,
    find_items,
    change_quantity,
    remove_item_by_name,
    add_inventory_item,
)


@pytest.fixture
def sample_inventory():
    return [
        {"name": "Laptop", "category": "Electronics", "quantity": 10},
        {"name": "Desk", "category": "Furniture", "quantity": 3},
        {"name": "Mouse", "category": "Electronics", "quantity": 2},
        {"name": "Chair", "category": "Furniture", "quantity": 8},
    ]


# LOAD INVENTORY TESTS

def test_load_inventory(tmp_path):
    inventory_file = tmp_path / "inventory.txt"
    inventory_file.write_text(
        "Laptop|Electronics|10\n"
        "Desk|Furniture|3\n"
    )

    inventory = load_inventory(inventory_file)

    assert len(inventory) == 2
    assert inventory[0]["name"] == "Laptop"
    assert inventory[0]["category"] == "Electronics"
    assert inventory[0]["quantity"] == 10
    assert inventory[1]["name"] == "Desk"


def test_load_inventory_missing_file(tmp_path):
    inventory_file = tmp_path / "missing.txt"

    inventory = load_inventory(inventory_file)

    assert inventory == []


# SEARCH TESTS

def test_find_items_exact_match(sample_inventory):
    results = find_items(sample_inventory, "Laptop")

    assert len(results) == 1
    assert results[0]["name"] == "Laptop"


def test_find_items_case_insensitive(sample_inventory):
    results = find_items(sample_inventory, "lApToP")

    assert len(results) == 1
    assert results[0]["name"] == "Laptop"


def test_find_items_no_match(sample_inventory):
    results = find_items(sample_inventory, "Phone")

    assert results == []


def test_find_items_empty_search(sample_inventory):
    results = find_items(sample_inventory, "")

    assert results == []


# SAVE INVENTORY TESTS

def test_save_inventory(tmp_path):
    inventory_file = tmp_path / "saved_inventory.txt"
    inventory = [
        {"name": "Laptop", "category": "Electronics", "quantity": 10},
        {"name": "Desk", "category": "Furniture", "quantity": 3},
    ]

    save_inventory(inventory, inventory_file)

    saved_content = inventory_file.read_text()

    assert "Laptop|Electronics|10" in saved_content
    assert "Desk|Furniture|3" in saved_content


def test_save_empty_inventory(tmp_path):
    inventory_file = tmp_path / "empty_inventory.txt"

    save_inventory([], inventory_file)

    assert inventory_file.exists()
    assert inventory_file.read_text() == ""


def test_save_and_load_inventory(tmp_path):
    inventory_file = tmp_path / "round_trip.txt"
    original_inventory = [
        {"name": "Laptop", "category": "Electronics", "quantity": 10},
        {"name": "Desk", "category": "Furniture", "quantity": 3},
    ]

    save_inventory(original_inventory, inventory_file)
    loaded_inventory = load_inventory(inventory_file)

    assert loaded_inventory == original_inventory


# QUANTITY UPDATE TESTS

def test_change_quantity(sample_inventory):
    result = change_quantity(sample_inventory, "Laptop", 5)

    assert result is True
    assert sample_inventory[0]["quantity"] == 5


def test_change_quantity_case_insensitive():
    inventory = [
        {"name": "Laptop", "category": "Electronics", "quantity": 10}
    ]

    result = change_quantity(inventory, "lApToP", 7)

    assert result is True
    assert inventory[0]["quantity"] == 7


def test_change_quantity_item_not_found():
    inventory = [
        {"name": "Laptop", "category": "Electronics", "quantity": 10}
    ]

    result = change_quantity(inventory, "Phone", 5)

    assert result is False
    assert inventory[0]["quantity"] == 10


def test_change_quantity_negative_quantity():
    inventory = [
        {"name": "Laptop", "category": "Electronics", "quantity": 10}
    ]

    result = change_quantity(inventory, "Laptop", -1)

    assert result is False
    assert inventory[0]["quantity"] == 10


# REMOVE INVENTORY TESTS

def test_remove_item_by_name(sample_inventory):
    result = remove_item_by_name(sample_inventory, "Laptop")

    assert result is True
    assert len(sample_inventory) == 3
    assert all(item["name"] != "Laptop" for item in sample_inventory)


def test_remove_item_case_insensitive():
    inventory = [
        {"name": "Laptop", "category": "Electronics", "quantity": 10}
    ]

    result = remove_item_by_name(inventory, "lApToP")

    assert result is True
    assert inventory == []


def test_remove_item_not_found():
    inventory = [
        {"name": "Laptop", "category": "Electronics", "quantity": 10}
    ]

    result = remove_item_by_name(inventory, "Phone")

    assert result is False
    assert len(inventory) == 1


def test_remove_item_empty_name():
    inventory = [
        {"name": "Laptop", "category": "Electronics", "quantity": 10}
    ]

    result = remove_item_by_name(inventory, "")

    assert result is False
    assert len(inventory) == 1


# ADD INVENTORY TESTS

def test_add_inventory_item():
    inventory = []

    result = add_inventory_item(
        inventory, "Mouse", "Electronics", 8
    )

    assert result is True
    assert len(inventory) == 1
    assert inventory[0] == {
        "name": "Mouse",
        "category": "Electronics",
        "quantity": 8
    }


def test_add_inventory_item_duplicate():
    inventory = [
        {"name": "Mouse", "category": "Electronics", "quantity": 8}
    ]

    result = add_inventory_item(
        inventory, "mouse", "Electronics", 5
    )

    assert result is False
    assert len(inventory) == 1


def test_add_inventory_item_empty_name():
    inventory = []

    result = add_inventory_item(
        inventory, " ", "Electronics", 5
    )

    assert result is False
    assert inventory == []


def test_add_inventory_item_negative_quantity():
    inventory = []

    result = add_inventory_item(
        inventory, "Mouse", "Electronics", -2
    )

    assert result is False
    assert inventory == []
@pytest.mark.parametrize(
    "search_term, expected_names",
    [
        pytest.param("Laptop", ["Laptop"], id="laptop-match"),
        pytest.param("Desk", ["Desk"], id="desk-match"),
        pytest.param("Mouse", ["Mouse"], id="mouse-match"),
        pytest.param("Phone", [], id="no-match"),
    ],
)
def test_find_items_parameterized(sample_inventory, search_term, expected_names):
    results = find_items(sample_inventory, search_term)
    actual_names = [item["name"] for item in results]

    assert actual_names == expected_names

@pytest.mark.parametrize(
    "item_name, new_quantity, expected_result, expected_quantity",
    [
        pytest.param("Laptop", 5, True, 5, id="update-existing"),
        pytest.param("laptop", 0, True, 0, id="case-insensitive-zero"),
        pytest.param("Phone", 4, False, 10, id="missing-item"),
        pytest.param("Laptop", -1, False, 10, id="negative-quantity"),
    ],
)
def test_change_quantity_parameterized(
    item_name, new_quantity, expected_result, expected_quantity
):
    inventory = [
        {"name": "Laptop", "category": "Electronics", "quantity": 10}
    ]

    result = change_quantity(inventory, item_name, new_quantity)

    assert result is expected_result
    assert inventory[0]["quantity"] == expected_quantity
# INVENTORY SUMMARY TESTS

def test_calculate_summary(sample_inventory):
    summary = inventory_manager.calculate_summary(sample_inventory)

    assert summary["unique_items"] == 4
    assert summary["total_quantity"] == 23
    assert summary["low_stock_count"] == 2
    assert summary["category_counts"] == {
        "electronics": 2,
        "furniture": 2
    }


def test_calculate_summary_empty_inventory():
    summary = inventory_manager.calculate_summary([])

    assert summary["unique_items"] == 0
    assert summary["total_quantity"] == 0
    assert summary["low_stock_count"] == 0
    assert summary["category_counts"] == {}


def test_calculate_summary_no_low_stock():
    inventory = [
        {"name": "Laptop", "category": "Electronics", "quantity": 10},
        {"name": "Desk", "category": "Furniture", "quantity": 8},
    ]

    summary = inventory_manager.calculate_summary(inventory)

    assert summary["low_stock_count"] == 0