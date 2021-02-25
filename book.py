from flask import Flask, jsonify, request
from business.book_manager import Book


app = Flask(__name__)

print(__name__)

bookRef = Book()

# Sample GET


@app.route('/api/books')
def get_books():
    books = bookRef.get_all_books()
    return jsonify(books)

# Sample GET by id


@app.route('/api/book/<string:name>')
def get_book(name):
    book = bookRef.get_book(name)
    return jsonify(book)

# Sample POST


@app.route('/api/books', methods=['POST'])
def add_book():
    book = request.get_json()
    savedVal = bookRef.add_book(book)
    return jsonify(savedVal)


app.run(port=5000)
