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
    return []


def save_inventory(inventory, filename):
    """Save inventory records to a text file."""
    pass


def view_inventory(inventory):
    """Display all inventory items."""
    pass


def add_item(inventory):
    """Add a new inventory item."""
    pass


def update_quantity(inventory):
    """Update the quantity of an existing inventory item."""
    pass


def remove_item(inventory):
    """Remove an inventory item."""
    pass


def search_inventory(inventory):
    """Search inventory using an item name."""
    pass


def display_summary(inventory):
    """Display a summary of the inventory."""
    pass


def main():
    """Run the Inventory Manager program."""
    display_menu()


if __name__ == "__main__":
    main()