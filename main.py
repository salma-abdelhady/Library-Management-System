from admin import Admin

def main():
    admin = Admin()

    while True:
        print("\n===== Library Options=====")
        print("1. Add Book")
        print("2. Print Library Books")
        print("3. Find Book by Name")
        print("4. Add User")
        print("5. Borrow Book")
        print("6. Return Book")
        print("7. Print Users Who Borrowed Books")
        print("8. Print All Users")
        print("0. Exit")

        choice = input("Enter your choice from 1 to 8: ")

        if choice == "1":
            id = int(input("Please Enter the book id: "))
            name = input("Please Enter the book name: ")
            quantity = int(input("Please Enter the book quantity: "))
            admin.add_book(id, name, quantity)

        elif choice == "2":
            admin.print_all_books()

        elif choice == "3":
            name = input("Enter book name to search: ")
            admin.find_book(name)

        elif choice == "4":
            id = int(input("Enter user ID: "))
            name = input("Enter user name: ")
            admin.add_user(id, name)

        elif choice == "5":
            user_name = input("Enter your name: ")
            book_name = input("Enter book name to borrow: ")
            admin.borrow_book(user_name, book_name)

        elif choice == "6":
            book_name = input("Enter book name to return: ")
            admin.return_book(book_name)

        elif choice == "7":
            admin.print_users_who_borrowed_books()
            
        elif choice == "8":
            admin.print_users()

        elif choice == "0":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Try again.")

main()