
books = [
    {
        'name': 'Ashan Perera',
                'price': 250
    },
    {
        'name': 'Ashan Pereraf',
                'price': 250
    },
    {
        'name': 'Ashan Pereraas',
                'price': 250
    },
    {
        'name': 'Ashan Pereraa',
                'price': 250
    }
]


class BookRepository:
    def __init__(self):
        pass

    def get_all_books(self):
        return books

    def get_book(self, book_name):
        return_value = {}
        for book in books:
            if(book["name"] == book_name):
                return_value = book
        return return_value

    def add_book(self, book):
        return books.append(book)

    #  this is for test purpose.
    def update_book(self, book):
        return book
