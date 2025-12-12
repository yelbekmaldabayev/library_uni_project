class Library:
    def __init__(self):
        self.__books = []
        self.__patrons = []

    def add_book(self, book):
        self.__books.append(book)

    def remove_book(self, book):
        if book in self.__books:
            self.__books.remove(book)
        else:
            return "Book not found."

    def add_patron(self, patron):
        self.__patrons.append(patron)

    def list_books(self):
        for book in self.__books:
            print(book.get_book_info())

    def list_patrons(self):
        return self.__patrons