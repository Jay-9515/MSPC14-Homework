# Book Class
class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.checked_out = False

    def check_out(self):
        if not self.checked_out:
            self.checked_out = True
            print(f"'{self.title}' checked out successfully.")
        else:
            print(f"'{self.title}' is already checked out.")

    def check_in(self):
        if self.checked_out:
            self.checked_out = False
            print(f"'{self.title}' returned successfully.")
        else:
            print(f"'{self.title}' was not checked out.")

    def display_info(self):
        status = "Checked Out" if self.checked_out else "Available"
        print(f"{self.title} by {self.author} [ISBN: {self.isbn}] - {status}")


# Customer Class
class Customer:
    def __init__(self, name, customer_id):
        self.name = name
        self.customer_id = customer_id
        self.checked_out_books = []

    def check_out_book(self, book):
        if not book.checked_out:
            book.check_out()
            self.checked_out_books.append(book)
        else:
            print(f"{book.title} is already checked out by someone else.")

    def check_in_book(self, book):
        if book in self.checked_out_books:
            book.check_in()
            self.checked_out_books.remove(book)
        else:
            print(f"{book.title} is not checked out by {self.name}.")

    def display_info(self):
        print(f"Customer: {self.name} (ID: {self.customer_id})")
        if self.checked_out_books:
            print("  Checked-out Books:")
            for book in self.checked_out_books:
                print(f"    - {book.title}")
        else:
            print("  No books currently checked out.")


# Library Class
class Library:
    def __init__(self):
        self.books = []
        self.customers = []

    def add_book(self, book):
        self.books.append(book)

    def add_customer(self, customer):
        self.customers.append(customer)
