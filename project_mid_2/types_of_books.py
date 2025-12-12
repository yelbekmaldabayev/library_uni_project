from books import Book

class AcademicBook(Book):
    def __init__(self, title, author, genre, ISBN, course_name):
        super().__init__(title, author, genre, ISBN)
        self.__course_name = course_name

    def get_course_name(self):
        return f"This book is recommended for the course: {self.__course_name}"

    def get_book_info(self):
        info = super().get_book_info()
        return f"{info}\nCourse Name: {self.__course_name}"


class FictionBook(Book):
    def __init__(self, title, author, genre, ISBN, sub_genre):
        super().__init__(title, author, genre, ISBN)
        self.__sub_genre = sub_genre

    def get_sub_genre(self):
        return f"This fiction book belongs to the sub-genre: {self.__sub_genre}"

    def get_book_info(self):
        info = super().get_book_info()
        return f"{info}\nSub-Genre: {self.__sub_genre}"


class ReferenceBook(Book):
    def __init__(self, title, author, genre, ISBN, subject_area):
        super().__init__(title, author, genre, ISBN)
        self.__subject_area = subject_area

    def get_subject_area(self):
        return f"This reference book is focused on: {self.__subject_area}"

    def get_book_info(self):
        info = super().get_book_info()
        return f"{info}\nSubject Area: {self.__subject_area}"
