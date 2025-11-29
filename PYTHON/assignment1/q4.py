import re
import json

books = []            # list of all books
book_ids = set()      # to prevent duplicate IDs
FILE = "library_records.json"


# ------------------ Load Records From File ------------------
def load_records():
    try:
        with open(FILE, "r") as f:
            data = json.load(f)
            books.extend(data)
            for b in data:
                book_ids.add(b["id"])
    except FileNotFoundError:
        pass


# ------------------ Save Records to File ------------------
def save_records():
    with open(FILE, "w") as f:
        json.dump(books, f, indent=4)


# ------------------ Add New Book ------------------
def add_book():
    try:
        book_id = input("Enter Book ID: ")

        if book_id in book_ids:
            print("❌ Duplicate ID! Book not added.\n")
            return

        name = input("Enter Book Name: ")
        author = input("Enter Author Name: ")
        category = input("Enter Category: ")

        book = {
            "id": book_id,
            "name": name,
            "author": author,
            "category": category
        }

        books.append(book)
        book_ids.add(book_id)
        save_records()

        print("✔ Book Added Successfully!\n")

    except Exception as e:
        print("Error:", e)


# ------------------ Search Book (Using Regex) ------------------
def search_book():
    pattern = input("Enter keyword (regex): ")
    print("\n--- Search Results ---")

    found = False
    for b in books:
        if (re.search(pattern, b["name"], re.IGNORECASE) or
            re.search(pattern, b["author"], re.IGNORECASE) or
            re.search(pattern, b["category"], re.IGNORECASE)):
            print(b)
            found = True

    if not found:
        print("No matching book found.\n")


# ------------------ Update Book ------------------
def update_book():
    id_to_update = input("Enter Book ID to update: ")

    for b in books:
        if b["id"] == id_to_update:
            print("Leave blank to keep old value.")

            new_name = input("New Name: ")
            new_author = input("New Author: ")
            new_category = input("New Category: ")

            if new_name:
                b["name"] = new_name
            if new_author:
                b["author"] = new_author
            if new_category:
                b["category"] = new_category

            save_records()
            print("✔ Book Updated Successfully!\n")
            return

    print("❌ Book ID not found.\n")


# ------------------ Delete Book ------------------
def delete_book():
    id_to_delete = input("Enter Book ID to delete: ")

    for b in books:
        if b["id"] == id_to_delete:
            books.remove(b)
            book_ids.remove(id_to_delete)
            save_records()
            print("✔ Book Deleted Successfully!\n")
            return

    print("❌ Book ID not found.\n")


# ------------------ Display All Books ------------------
def display_books():
    print("\n--- All Book Records ---")
    for b in books:
        print(b)
    print()


# ------------------ Main Menu ------------------
load_records()

while True:
    print("1. Add Book")
    print("2. Search Book (Regex)")
    print("3. Update Book")
    print("4. Delete Book")
    print("5. Display All Books")
    print("6. Exit")

    choice = input("Enter choice: ")

    if choice == '1':
        add_book()
    elif choice == '2':
        search_book()
    elif choice == '3':
        update_book()
    elif choice == '4':
        delete_book()
    elif choice == '5':
        display_books()
    elif choice == '6':
        print("Exiting...")
        break
    else:
        print("Invalid choice! Try again.\n")
