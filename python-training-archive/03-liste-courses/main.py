import sys

# Global shopping list
shopping_list = []

def add_item():
    # Ask the user for an item and add it to the list
    item = input("Add an item to the list: ")
    shopping_list.append(item)

def remove_item():
    # Ask the user for an item to remove
    item_to_remove = input("Remove an item from the list: ")
    if item_to_remove in shopping_list:
        shopping_list.remove(item_to_remove)
    else:
        print("Item not found in the list.")

def display_list():
    # Display all items in the list
    print(shopping_list)

def clear_list():
    # Remove all items from the list
    shopping_list.clear()

# Main menu loop
while True:
    print("1. Add an item")
    print("2. Remove an item")
    print("3. Display the list")
    print("4. Clear the list")
    print("5. Quit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_item()
    elif choice == "2":
        remove_item()
    elif choice == "3":
        display_list()
    elif choice == "4":
        clear_list()
    elif choice == "5":
        sys.exit()
    else:
        print("Please enter a valid number.")