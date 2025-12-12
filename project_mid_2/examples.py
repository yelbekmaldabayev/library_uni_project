from types_of_books import AcademicBook, FictionBook, ReferenceBook
from patron import Patron
from library import Library


# Create some book objects
book1 = AcademicBook("Introduction to Python", "John Doe", "Computer Science", "12345", "CS101")
book2 = FictionBook("The Great Gatsby", "F. Scott Fitzgerald", "Fiction", "67890", "Classic")
book3 = ReferenceBook("Encyclopedia of Science", "Various Authors", "Reference", "11223", True)

# Create some patron objects
patron1 = Patron("Alice", "P001")
patron2 = Patron("Bob", "P002")

# Create a library object
library = Library()
library.add_book(book1)
library.add_book(book2)
library.add_book(book3)

# Add patrons to the library
library.add_patron(patron1)
library.add_patron(patron2)

print()

print("Patron borrows and returns books")
print(patron1.borrow_book(book1))  # Alice borrows "Introduction to Python"
print(patron1.return_book(book1))  # Alice returns the book

print()


# Show book info
print(book1.get_book_info())
print(book2.get_book_info())
print(book3.get_book_info())

# Show patron info
# print(f"Patron: {patron1.name()}, ID: {patron1.get_id()}")
# print(f"Patron: {patron2.name()}, ID: {patron2.get_id()}")

print(patron1.get_patron_info())

# Show library contents (assuming Library has methods to list books/patrons)
print("Books in library:")
library.list_books()

for p in library.list_patrons():
    print(p.get_patron_info())
