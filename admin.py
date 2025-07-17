from book import *
from user import *

class Admin():
    def __init__(self):
        self.books = []
        self.users = []
        
    def add_book(self, id, name, quantity):
        for book in self.books:
            if book.id == id:
                print("Book already exist. ")
                return 
            
        book = Book(id, name, quantity) 
        self.books.append(book)
        print("Book added successfully. ")
    
    def print_all_books(self):
        if not self.books:
            print("There is no books avaliable. ")
            return
        
        for book in self.books:
            print(f"Book id: {book.id}, Name: {book.name}, Quantity: {book.quantity}")
        
    def find_book(self,name):
        if not self.books:
            print("There is no books avaliable. ")
            return 
        
        for book in self.books:
            if book.name.lower() == name.lower():
                print(f"Book {book.name} exist. ")
    
    def add_user(self, id, name):
        for user in self.users:
            if user.id == id:
                print("User already exist. ")
                return 
            
        user = User(id, name) 
        self.users.append(user)
        print("User added successfully. ")
    
    def borrow_book(self,user_name,book_name):
        user = None
        for u in self.users:
            if u.name == user_name:
                user = u
                break
        
        if user is None:
            print("User not found.")
            return
        
        if not self.books:
            print("There is no books avaliable for Borrow. ")
            return
        
        for book in self.books:
            if book.name.lower() == book_name.lower():
                if book.quantity > 0:
                    print(f"Here is your book, have a happy time reading {book.name}")
                    user.borrowed_books.append(book.name)
                    book.quantity -= 1
                else:
                    print("Sorry, the book is out of stock.")
                return
            else:
                print("The book isn't available in the library.")
                
    
    def return_book(self,user_name, book_name):
        user = None
        for u in self.users:
            if u.name == user_name:
                user = u
                break
        
        if user is None:
            print("User not found.")
            return
        
        if book_name in user.borrowed_books:
            user.borrowed_books.remove(book_name)
            for book in self.books:
                if book.name == book_name:
                    book.quantity += 1
                    print(f"Thanks for returning {book.name}")
                    return
        else:
            print("This book was not borrowed by the user.")
    
                
    def print_users_who_borrowed_books(self):
        if not self.users:
            return
        for user in self.users:
            if user.borrowed_books:
                print(f"User Id: {user.id}, Name: {user.name}")
                print("Borrowed books: ")
                for book in user.borrowed_books:
                    print(book)    
            else:
                print("There is no borrowed books. ")
        
    
    def print_users(self):
        if not self.users:
            print("There is no users avaliable. ")
            return 
        for user in self.users:
            print(f"User Id: {user.id}, Name: {user.name}")
        
        
                