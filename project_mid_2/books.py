class Book:
    def __init__(self, title, author, genre, ISBN):
        self.__title = title
        self.__author = author
        self.__genre = genre
        self.__ISBN = ISBN
        self.__availability = True  # By default, the book is available

    def get_book_info(self):
        return f"Title: {self.__title}\nAuthor: {self.__author}\nGenre: {self.__genre}\nISBN: {self.__ISBN}"

    def check_availability(self):
        return "Available" if self.__availability else "Not Available"

    def borrow_book(self):
        if self.__availability:
            self.__availability = False
            return f"You have successfully borrowed {self.__title}."
        else:
            return f"{self.__title} is currently not available."

    def return_book(self):
        self.__availability = True
        return f"You have successfully returned {self.__title}."
    
