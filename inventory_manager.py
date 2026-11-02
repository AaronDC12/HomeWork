
"""
Inventory Manager
Name: Aaron Dcunha
Course: CPS 310
Project: HW01 Inventory Manager
"""

INVENTORY_FILE = "inventory.txt"


def display_menu():
    """Display the main Inventory Manager menu."""
    print("\nInventory Manager")
    print("1. View inventory")
    print("2. Add an item")
    print("3. Update an item quantity")
    print("4. Remove an item")
    print("5. Search inventory")
    print("6. View inventory summary")
    print("7. Exit")


def load_inventory(filename):
    """Load inventory records from a text file."""
    inventory = []

    try:
        with open(filename, "r") as file:
            for line in file:
                line = line.strip()

                if line:
                    name, category, quantity = line.split("|")

                    item = {
                        "name": name,
                        "category": category,
                        "quantity": int(quantity)
                    }

                    inventory.append(item)

    except FileNotFoundError:
        return []

    return inventory


def save_inventory(inventory, filename):
    """Save inventory records to a text file."""
    with open(filename, "w") as file:
        for item in inventory:
            file.write(
                f"{item['name']}|{item['category']}|{item['quantity']}\n"
            )


def view_inventory(inventory):
    """Display all inventory items."""
    if not inventory:
        print("No inventory items found.")
        return

    print("\nInventory:")

    for number, item in enumerate(inventory, start=1):
        print(
            f"{number}. {item['name']} | "
            f"{item['category']} | "
            f"Quantity: {item['quantity']}"
        )


# ADD INVENTORY FUNCTIONS

def add_inventory_item(inventory, name, category, quantity):
    """Add a valid inventory item. Return True if successful."""
    name = name.strip()
    category = category.strip()

    if not name or not category:
        return False

    if "|" in name or "|" in category:
        return False

    if not isinstance(quantity, int) or quantity < 0:
        return False

    for item in inventory:
        if item["name"].casefold() == name.casefold():
            return False

    inventory.append({
        "name": name,
        "category": category,
        "quantity": quantity
    })

    return True


def add_item(inventory):
    """Add a new inventory item."""
    name = input("Enter the item name: ").strip()
    category = input("Enter the category: ").strip()
    quantity_input = input("Enter the quantity: ").strip()

    if not quantity_input.isdigit():
        print("Quantity must be a nonnegative whole number.")
        return

    quantity = int(quantity_input)

    if add_inventory_item(inventory, name, category, quantity):
        save_inventory(inventory, INVENTORY_FILE)
        print("Item added successfully.")
    else:
        print("Invalid item or an item with that name already exists.")


# QUANTITY UPDATE FUNCTIONS

def change_quantity(inventory, name, new_quantity):
    """Update the quantity of an existing inventory item."""
    if not name.strip():
        return False

    if not isinstance(new_quantity, int) or new_quantity < 0:
        return False

    for item in inventory:
        if item["name"].casefold() == name.strip().casefold():
            item["quantity"] = new_quantity
            return True

    return False


def update_quantity(inventory):
    """Update the quantity of an existing inventory item."""
    name = input("Enter the item name to update: ").strip()

    if not name:
        print("Item name cannot be empty.")
        return

    quantity_input = input("Enter the new quantity: ").strip()

    if not quantity_input.isdigit():
        print("Quantity must be a nonnegative whole number.")
        return

    quantity = int(quantity_input)

    if change_quantity(inventory, name, quantity):
        save_inventory(inventory, INVENTORY_FILE)
        print("Quantity updated successfully.")
    else:
        print("Item not found.")


# REMOVE INVENTORY FUNCTIONS

def remove_item_by_name(inventory, name):
    """Remove an item by name. Return True if removed."""
    if not name.strip():
        return False

    for item in inventory:
        if item["name"].casefold() == name.strip().casefold():
            inventory.remove(item)
            return True

    return False


def remove_item(inventory):
    """Remove an inventory item."""
    name = input("Enter the item name to remove: ").strip()

    if remove_item_by_name(inventory, name):
        save_inventory(inventory, INVENTORY_FILE)
        print("Item removed successfully.")
    else:
        print("Item not found.")


# SEARCH INVENTORY FUNCTIONS

def find_items(inventory, search_term):
    """Return items matching a partial, case-insensitive name."""
    search_term = search_term.strip()

    if not search_term:
        return []

    return [
        item for item in inventory
        if search_term.casefold() in item["name"].casefold()
    ]


def search_inventory(inventory):
    """Search inventory using a partial, case-insensitive name."""
    search_term = input("Enter a search term: ").strip()

    if not search_term:
        print("Search term cannot be empty.")
        return

    found_items = find_items(inventory, search_term)

    if not found_items:
        print("No matching items found.")
        return

    print("\nSearch Results:")

    for number, item in enumerate(found_items, start=1):
        print(
            f"{number}. {item['name']} | "
            f"{item['category']} | "
            f"Quantity: {item['quantity']}"
        )


# INVENTORY SUMMARY FUNCTIONS

def calculate_summary(inventory):
    """Calculate inventory statistics."""
    unique_items = len(inventory)

    total_quantity = sum(
        item["quantity"] for item in inventory
    )

    low_stock_items = [
        item for item in inventory
        if item["quantity"] < 5
    ]

    category_counts = {}

    for item in inventory:
        category = item["category"].lower()

        if category not in category_counts:
            category_counts[category] = 0

        category_counts[category] += 1

    return {
        "unique_items": unique_items,
        "total_quantity": total_quantity,
        "low_stock_count": len(low_stock_items),
        "category_counts": category_counts,
    }


def display_summary(inventory):
    """Display a summary of the inventory."""
    summary = calculate_summary(inventory)

    print("\nInventory Summary")
    print(f"Unique items: {summary['unique_items']}")
    print(f"Total quantity: {summary['total_quantity']}")
    print(f"Low-stock items: {summary['low_stock_count']}")
    print("Items by category:")

    for category, count in summary["category_counts"].items():
        print(f"- {category}: {count}")


# MAIN PROGRAM

def main():
    """Run the Inventory Manager program."""
    inventory = load_inventory(INVENTORY_FILE)

    while True:
        display_menu()

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            view_inventory(inventory)

        elif choice == "2":
            add_item(inventory)

        elif choice == "3":
            update_quantity(inventory)

        elif choice == "4":
            remove_item(inventory)

        elif choice == "5":
            search_inventory(inventory)

        elif choice == "6":
            display_summary(inventory)

        elif choice == "7":
            print("Goodbye!")
            break

        else:
            print("Please enter a number from 1 to 7.")


if __name__ == "__main__":
    main()
