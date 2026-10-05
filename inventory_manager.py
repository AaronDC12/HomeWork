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


def add_item(inventory):
    """Add a new inventory item."""
    name = input("Enter the item name: ").strip()

    if not name:
        print("Item name cannot be empty.")
        return

    if "|" in name:
        print("Item name may not contain |.")
        return

    for item in inventory:
        if item["name"].lower() == name.lower():
            print("An item with that name already exists.")
            return

    category = input("Enter the category: ").strip()

    if not category:
        print("Category cannot be empty.")
        return

    if "|" in category:
        print("Category may not contain |.")
        return

    quantity_input = input("Enter the quantity: ").strip()

    if not quantity_input.isdigit():
        print("Quantity must be a nonnegative whole number.")
        return

    quantity = int(quantity_input)

    item = {
        "name": name,
        "category": category,
        "quantity": quantity
    }

    inventory.append(item)

    save_inventory(inventory, INVENTORY_FILE)

    print("Item added successfully.")
def update_quantity(inventory):
    """Update the quantity of an existing inventory item."""
    name = input("Enter the item name to update: ").strip()

    if not name:
        print("Item name cannot be empty.")
        return

    for item in inventory:
        if item["name"].lower() == name.lower():
            quantity_input = input("Enter the new quantity: ").strip()

            if not quantity_input.isdigit():
                print("Quantity must be a nonnegative whole number.")
                return

            item["quantity"] = int(quantity_input)

            save_inventory(inventory, INVENTORY_FILE)

            print("Quantity updated successfully.")
            return

    print("Item not found.")

def remove_item(inventory):
    """Remove an inventory item."""
    name = input("Enter the item name to remove: ").strip()

    if not name:
        print("Item name cannot be empty.")
        return

    for item in inventory:
        if item["name"].lower() == name.lower():
            inventory.remove(item)

            save_inventory(inventory, INVENTORY_FILE)

            print("Item removed successfully.")
            return

    print("Item not found.")

def search_inventory(inventory):
    """Search inventory using a partial, case-insensitive name."""
    search_term = input("Enter a search term: ").strip()

    if not search_term:
        print("Search term cannot be empty.")
        return

    found_items = []

    for item in inventory:
        if search_term.lower() in item["name"].lower():
            found_items.append(item)

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

def display_summary(inventory):
    """Display a summary of the inventory."""
    unique_items = len(inventory)
    total_quantity = sum(item["quantity"] for item in inventory)

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

    print("\nInventory Summary")
    print(f"Unique items: {unique_items}")
    print(f"Total quantity: {total_quantity}")
    print(f"Low-stock items: {len(low_stock_items)}")

    print("Items by category:")
    for category, count in category_counts.items():
        print(f"- {category}: {count}")

def main():
    """Run the Inventory Manager program."""
    inventory = load_inventory(INVENTORY_FILE)

    display_summary(inventory)
if __name__ == "__main__":
    main()