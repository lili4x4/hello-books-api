from flask import Blueprint, jsonify, abort, make_response

class Book:
    def __init__(self, id, title, description):
        self.id = id
        self.title = title
        self.description = description

books = [
    Book(1, "The Name of the Wind", "The first book in the Kingkiller Chronicles fantasy trilogy."),
    Book(2, "The Wise Man's Fear", "The first book in the Kingkiller Chronicles fantasy trilogy."),
    Book(3, "The Doors of Stone", "The supposed third book in the Kingkiller Chronicles trilogy, which apparently will never be released.")
]

hello_world_bp = Blueprint("hello_world", __name__)

books_bp = Blueprint("books", __name__, url_prefix="/books")

def validate_book(book_id):
    try:
        book_id = int(book_id)
    except:
        abort(make_response({"message": f"Book {book_id} not found"}, 400))
    
    for book in books:
        if book.id == book_id:
            return book
    abort(make_response({"message": f"Book {book_id} invalid"}, 404))


@hello_world_bp.route("/hello-world", methods=["GET"])
def say_hello_world():
    response_body = "Hello, World!"
    return response_body

@hello_world_bp.route("/hello/JSON", methods=["GET"])
def say_hello_json():
    return {
        "name": "Ada Lovelace",
        "message": "Hello!",
        "hobbies": ["Fishing", "Swimming", "Watching Reality Shows"]
        }
    
@hello_world_bp.route("/broken-endpoint-with-broken-server-code")
def broken_endpoint():
    response_body = {
        "name": "Ada Lovelace",
        "message": "Hello!",
        "hobbies": ["Fishing", "Swimming", "Watching Reality Shows"]
    }
    new_hobby = "Surfing"
    response_body["hobbies"].append(new_hobby)
    return response_body

@books_bp.route("", methods=["GET"])
def handle_books():
    books_response = []
    for book in books:
        books_response.append({
            "id": book.id,
            "title": book.title,
            "description": book.description
        })
    return jsonify(books_response)

@books_bp.route("/<book_id>", methods=["GET"])
def handle_book(book_id):

    book = validate_book(book_id)

    return {
            "id": book.id,
            "title": book.title,
            "description": book.description
            }
