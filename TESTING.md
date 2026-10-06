# Testing

The Inventory Manager was tested manually through the command-line interface. The tests below cover the required features, input validation, file loading/saving, and menu behavior.

| # | Feature | Test | Expected Result | Result |
|---|---|---|---|---|
| 1 | Load inventory | Start program with a valid `inventory.txt` | Existing inventory loads correctly | PASS |
| 2 | Missing file | Start program when inventory file is missing | Program starts with an empty inventory without crashing | PASS |
| 3 | View inventory | Select menu option 1 | All inventory items are displayed | PASS |
| 4 | Add item | Add a valid item with a valid quantity | Item is added and saved | PASS |
| 5 | Add validation | Enter an empty item name | Item is rejected | PASS |
| 6 | Add validation | Enter a duplicate name with different capitalization | Duplicate item is rejected | PASS |
| 7 | Add validation | Enter a nonnumeric quantity | Quantity is rejected | PASS |
| 8 | Add validation | Enter a negative quantity | Quantity is rejected | PASS |
| 9 | Add validation | Enter `|` in the item name | Item is rejected | PASS |
| 10 | Add validation | Enter `|` in the category | Category is rejected | PASS |
| 11 | Update quantity | Update an existing item's quantity | Quantity changes and is saved | PASS |
| 12 | Update validation | Enter a negative quantity during an update | Update is rejected | PASS |
| 13 | Update validation | Try to update an item that does not exist | "Item not found" message is displayed | PASS |
| 14 | Remove item | Remove an existing item | Item is removed and changes are saved | PASS |
| 15 | Remove validation | Try to remove an item that does not exist | "Item not found" message is displayed | PASS |
| 16 | Search | Search using part of an item name | Matching items are displayed | PASS |
| 17 | Search | Search using different capitalization | Matching items are still found | PASS |
| 18 | Search validation | Enter an empty search term | Search is rejected | PASS |
| 19 | Search validation | Search for an item that does not exist | "No matching items found" message is displayed | PASS |
| 20 | Summary | Select menu option 6 | Unique items, total quantity, low-stock count, and category counts are displayed | PASS |
| 21 | Menu validation | Enter an invalid menu choice such as `9` | Invalid choice is rejected | PASS |
| 22 | Exit | Select menu option 7 | Program exits with a goodbye message | PASS |
| 23 | Add persistence | Add an item, exit, and restart the program | Added item remains in the inventory | PASS |
| 24 | Update persistence | Update an item's quantity, exit, and restart | Updated quantity remains saved | PASS |
| 25 | Remove persistence | Remove an item, exit, and restart | Removed item does not return | PASS |

## Final Inventory Used for Testing

```text
Laptop Charger|Electronics|15
Printer Paper|Office Supplies|25
Dry-Erase Markers|Classroom Supplies|4
HDMI Cable|Electronics|6
Notebook|Classroom Supplies|12