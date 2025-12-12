class Patron:
    def __init__(self, name, patron_id):
        self.__name = name
        self.__patron_id = patron_id
        self.__borrowed_books = {}

    def get_patron_info(self):
        return f"Patron Name: {self.__name}\nPatron ID: {self.__patron_id}"

    def borrow_book(self, book):
        if book.check_availability() == "Available":
            self.__borrowed_books[book] = book.borrow_book()
            return self.__borrowed_books[book]
        else:
            return f"Sorry, the book '{book.get_book_info()}' is not available."

    def return_book(self, book):
        if book in self.__borrowed_books:
            self.__borrowed_books[book] = book.return_book()
            return self.__borrowed_books[book]
        else:
            return "You haven't borrowed this book."