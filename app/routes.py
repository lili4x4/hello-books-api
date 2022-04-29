from app import db
from app.models.book import Book
from flask import Blueprint, jsonify, make_response, request

books_bp = Blueprint("books", __name__, url_prefix="/books")

@books_bp.route("", methods=["GET"])
def read_all_books():
    books = Book.query.all()
    books_response = []
    
    for book in books:
        books_response.append({
            "id": book.id,
            "title": book.title,
            "description": book.description
        })
    
    return jsonify(books_response)

@books_bp.route("", methods=["POST"])
def create_book():
    request_body = request.get_json()
    new_book = Book(
        title=request_body["title"],
        description=request_body["description"]
    )
    db.session.add(new_book)
    db.session.commit()

    return f"Book {new_book.title} created", 201




# class Book:
#     def __init__(self, id, title, description):
#         self.id = id
#         self.title = title
#         self.description = description

#     def to_dict(self):
#         return dict(
#             id=self.id,
#             title=self.title,
#             description=self.description
#         )

# books = [
#     Book(1, "The Name of the Wind", "The first book in the Kingkiller Chronicles fantasy trilogy."),
#     Book(2, "The Wise Man's Fear", "The first book in the Kingkiller Chronicles fantasy trilogy."),
#     Book(3, "The Doors of Stone", "The supposed third book in the Kingkiller Chronicles trilogy, which apparently will never be released.")
# ]

# hello_world_bp = Blueprint("hello_world", __name__)

# def validate_book(book_id):
#     try:
#         book_id = int(book_id)
#     except:
#         abort(make_response({"message": f"Book {book_id} not found"}, 400))

#     for book in books:
#         if book.id == book_id:
#             return book
#     abort(make_response({"message": f"Book {book_id} invalid"}, 404))


# @hello_world_bp.route("/hello-world", methods=["GET"])
# def say_hello_world():
#     response_body = "Hello, World!"
#     return response_body

# @hello_world_bp.route("/hello/JSON", methods=["GET"])
# def say_hello_json():
#     return {
#         "name": "Ada Lovelace",
#         "message": "Hello!",
#         "hobbies": ["Fishing", "Swimming", "Watching Reality Shows"]
#         }
    
# @hello_world_bp.route("/broken-endpoint-with-broken-server-code")
# def broken_endpoint():
#     response_body = {
#         "name": "Ada Lovelace",
#         "message": "Hello!",
#         "hobbies": ["Fishing", "Swimming", "Watching Reality Shows"]
#     }
#     new_hobby = "Surfing"
#     response_body["hobbies"].append(new_hobby)
#     return response_body

@books_bp.route("/<book_id>", methods=["GET"])
def handle_book(book_id):

    book = validate_book(book_id)

    # return {
    #         "id": book.id,
    #         "title": book.title,
    #         "description": book.description
    #         }

    return jsonify(book.to_dict())
