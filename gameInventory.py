# This is the file where you must work. Write code in the functions, create new functions, 
# so they work according to the specification
import pprint
import sys
import csv


# Displays the inventory.
def display_inventory(inventory):
    items = 0
    print("Inventory:")
    for k, v in inventory.items():
        print(str(v) + ' ' + str(k))
        items += v
    print("Total number of items: " + str(items))


# Adds to the inventory dictionary a list of items from added_items.
def add_to_inventory(inventory, added_items):
    for item in added_items:
        if item in inventory:
            inventory[item] += 1
        else:
            inventory[item] = 1


# Takes your inventory and displays it in a well-organized table with
# each column right-justified. The input argument is an order parameter (string)
# which works as the following:
# - None (by default) means the table is unordered
# - "count,desc" means the table is ordered by count (of items in the inventory) 
#   in descending order
# - "count,asc" means the table is ordered by count in ascending order
def print_table(inventory, order=None, order1="count,desc", order2="count,asc"):
    items = 0
    print("Inventory:")
    print("count".rjust(6) + "    " + "item name".rjust(max(map(len, inventory))))
    for i in range(max(map(len, inventory)) + 10):
        print("-", end='')
    print()
    if order is None:
        for k, v in inventory.items():
            print(str(v).rjust(4) + "      " + str(k).rjust(max(map(len, inventory))))
            items += v
            continue
    elif order is order1:
        print("it's order1")
        for v, k in sorted(((v, k) for k, v in inventory.items()), reverse=True):
            print(str(v).rjust(4) + "      " + str(k).rjust(max(map(len, inventory))))
            items += v
            continue
    elif order is order2:
        print("it's order1")
        for v, k in sorted(((v, k) for k, v in inventory.items())):
            print(str(v).rjust(4) + "      " + str(k).rjust(max(map(len, inventory))))
            items += v
            continue
    for i in range(max(map(len, inventory)) + 10):
        print("-", end='')
    print()
    print("Total number of items: " + str(items))


# Imports new inventory items from a file
# The filename comes as an argument, but by default it's 
# "import_inventory.csv". The import automatically merges items by name.
# The file format is plain text with comma separated values (CSV).
def import_inventory(inventory, filename="import_inventory.csv"):
    with open(filename, "r") as csvfile:
        new = csvfile.read().split(",")
        return add_to_inventory(inventory, new)

#POLECENIE


# Exports the inventory into a .csv file.
# if the filename argument is None it creates and overwrites a file
# called "export_inventory.csv". The file format is the same plain text 
# with comma separated values (CSV).

#1 sposób

def export_inventory(inventory, filename="export_inventory.csv"):
    with open(filename, "w") as csvfile:
        new = csv.writer(csvfile, quoting=csv.QUOTE_MINIMAL)
        new.writerow(sorted((k for k, v in inventory.items() for _ in range(v))))

#2 sposób
# def export_inventory(inventory, filename="export_inventory.csv"):
#     with open(filename, "w") as csvfile:
#         new = csv.writer(csvfile, quoting=csv.QUOTE_MINIMAL)
#         for key, value in inventory.items():
#             new.writerow([key for _ in range(value)])
#
# #3 sposób
# def export_inventory(inventory, filename="export_inventory.csv"):
#     with open(filename, "w") as csvfile:
#         new = csv.writer(csvfile, quoting=csv.QUOTE_MINIMAL)
#         new.writerow((k for k, v in inventory.items() for _ in range(v)))