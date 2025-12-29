import getpass
import pickle

def save_library(library, filename="library_data.pkl"):
    with open(filename, 'wb') as f:
        pickle.dump(library, f)

def load_library(filename="library_data.pkl"):
    try:
        with open(filename, 'rb') as f:
            return pickle.load(f)
    except FileNotFoundError:
        # Initial library data if file not found
        return {
            101: ("The Alchemist", "Paulo Coelho", 4),
            102: ("1984", "George Orwell", 2),
            103: ("To Kill a Mockingbird", "Harper Lee", 3)
        }

def list_books(library):
    print("\nCurrent Books in Library:")
    for book_id, (title, author, qty) in library.items():
        print(f"ID: {book_id}, Title: {title}, Author: {author}, Quantity: {qty}")

def search_book(library):
    book_id = int(input("Enter Book ID to search: "))
    if book_id in library:
        title, author, qty = library[book_id]
        print(f"Book Found - Title: {title}, Author: {author}, Quantity: {qty}")
    else:
        print("Book not found.")

def add_book(library):
    book_id = int(input("Enter new Book ID: "))
    title = input("Enter Book Title: ")
    author = input("Enter Author: ")
    quantity = int(input("Enter Quantity: "))
    if book_id in library:
        print("Book ID already exists, updating quantity.")
        current_qty = library[book_id][2]
        library[book_id] = (title, author, current_qty + quantity)
    else:
        library[book_id] = (title, author, quantity)
    print("Book added/updated successfully.")

def borrow_book(library):
    book_id = int(input("Enter Book ID to borrow: "))
    if book_id in library:
        title, author, qty = library[book_id]
        if qty > 0:
            library[book_id] = (title, author, qty - 1)
            print(f"You have borrowed '{title}'.")
        else:
            print("Sorry, this book is currently not available.")
    else:
        print("Book ID not found in the library.")

def return_book(library):
    book_id = int(input("Enter Book ID to return: "))
    if book_id in library:
        title, author, qty = library[book_id]
        library[book_id] = (title, author, qty + 1)
        print(f"Thank you for returning '{title}'.")
    else:
        print("Book ID not recognized.")

def login():
    print("Welcome to the Library Management System")
    while True:
        choice = input("Enter 'login' to log in or 'exit' to quit: ").strip().lower()
        if choice == 'exit':
            print("Exiting the system....\nGoodbye!")
            return False
        elif choice == 'login':
            username = input("Enter username: ")
            password = getpass.getpass("Enter password: ")  # Secure password entry
            # Add authentication logic here if desired
            print(f"Login successful. Welcome, {username}!")
            return True
        else:
            print("Invalid choice. Please enter 'login' or 'exit'.")

def main():
    if not login():
        return

    library = load_library()

    while True:
        print("\nLibrary Management System")
        print("1. List Books")
        print("2. Search Book")
        print("3. Add Book")
        print("4. Borrow Book")
        print("5. Return Book")
        print("6. Exit")
        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            list_books(library)
        elif choice == '2':
            search_book(library)
        elif choice == '3':
            add_book(library)
            save_library(library)
        elif choice == '4':
            borrow_book(library)
            save_library(library)
        elif choice == '5':
            return_book(library)
            save_library(library)
        elif choice == '6':
            print("Exiting the system....\nGoodbye!")
            save_library(library)
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    main()
