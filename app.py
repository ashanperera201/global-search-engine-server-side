from flask import Flask, jsonify, request
from business.book_manager import Book


app = Flask(__name__)
APP_KEY = 'xQvVXrVcaZh4diC8wQ5s'

# print(__name__)
# mysql connection
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root'
app.config['MYSQL_DB'] = 'test_db'

mysql = MySQL(app)

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

@app.route('/api/register', methods=['POST'])
def register_api():
    application_key = request.headers['Application-Key'];

    if application_key is not None and application_key == APP_KEY:
        if request.method == 'POST':
            

    # book = request.get_json()
    # savedVal = bookRef.add_book(book)
    # return jsonify(savedVal)

def validate_access_key():

app.run(port=5000)
