from data.book_repository import BookRepository

book_repository = BookRepository()


class Book:

    def __init__(self):
        pass

    def get_all_books(self):
        return book_repository.get_all_books()

    def get_book(self, book_name):
        return book_repository.get_book(book_name)

    def add_book(self, book):
        return book_repository.add_book(book)

    def update_book(self, book):
        return book_repository.update_book(book)
