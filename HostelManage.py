# Hostel Inventory Manager

def display_menu():
    print("\n--- Hostel Inventory Manager ---")
    print("1. View Inventory")
    print("2. Add Item")
    print("3. Remove Item")
    print("4. Search Item")
    print("5. Check Shortages")
    print("6. Exit")

def view_inventory(inventory):
    print("\nCurrent Inventory:")
    if not inventory:
        print("Inventory is empty.")
    else:
        for item, qty in inventory.items():
            print(f"{item}: {qty}")

def add_item(inventory):
    item = input("Enter item name to add: ").strip().lower()
    qty = int(input("Enter quantity: "))
    if item in inventory:
        inventory[item] += qty
    else:
        inventory[item] = qty
    print(f"{qty} {item}(s) added.")

def remove_item(inventory):
    item = input("Enter item name to remove: ").strip().lower()
    if item in inventory:
        qty = int(input("Enter quantity to remove: "))
        if qty >= inventory[item]:
            del inventory[item]
            print(f"All {item}(s) removed from inventory.")
        else:
            inventory[item] -= qty
            print(f"{qty} {item}(s) removed.")
    else:
        print(f"{item} not found in inventory.")

def search_item(inventory):
    item = input("Enter item name to search: ").strip().lower()
    if item in inventory:
        print(f"{item} found with quantity: {inventory[item]}")
    else:
        print(f"{item} not found.")

def check_shortages(inventory):
    print("\nItems with quantity less than 5 (shortages):")
    found = False
    for item, qty in inventory.items():
        if qty < 5:
            print(f"{item}: {qty}")
            found = True
    if not found:
        print("No shortages currently.")

def main():
    inventory = {}
    while True:
        display_menu()
        choice = input("Enter your choice (1-6): ")
        if choice == '1':
            view_inventory(inventory)
        elif choice == '2':
            add_item(inventory)
        elif choice == '3':
            remove_item(inventory)
        elif choice == '4':
            search_item(inventory)
        elif choice == '5':
            check_shortages(inventory)
        elif choice == '6':
            print("Exiting Hostel Inventory Manager.")
            break
        else:
            print("Invalid choice. Please select between 1-6.")

if __name__ == "__main__":
    main()