from app import db
from .models.book import Book
from flask import request, Blueprint, make_response
from flask import jsonify


books_bp = Blueprint("books", __name__, url_prefix="/books")

def is_int(value):
    try:
        return int(value)
    except ValueError:
        return False

@books_bp.route("/<book_id>", methods=["GET"], strict_slashes=False)
def get_single_book(book_id):
    # Try to find the book with the given id
    if not is_int(book_id):
        return make_response("", 404)
        # return {
        #     "message": f"ID {book_id} must be an integer",
        #     "success" : False
        # }, 404
    book = Book.query.get(book_id)

    if book:
        return book.to_json(), 200

    return make_response("", 404)
    # return {
    #     "message": f"Book with id {book_id} was not found",
    #     "success" : False
    # }, 404

# @books_bp.route("", methods=["GET"], strict_slashes=False)  
# def get_book_title():
    
#     title_query = request.args.get("title")
#     book = Book.query.filter_by(title=title_query)

#     if book:
#         # return book.to_json(), 200
#         return {
#             "id": book.id,
#             "title": book.title,
#             "description": book.description
#         }, 200

#     return make_response("", 404)


@books_bp.route("", methods=["GET"], strict_slashes=False)
def books_index():
    # title_query = request.args.get("title")
    # if title_query:
    #     books = Book.query.filter_by(title-title_query)
    # else:
    #     books = Book.query.all()

    books = Book.query.all()
    books_response = []
    for book in books:
        books_response.append(book.to_json())
    return jsonify(books_response), 200


@books_bp.route("", methods=["POST"], strict_slashes=False)
def handle_books():
    request_body = request.get_json()
    new_book = Book(title=request_body["title"],
                    description=request_body["description"])

    db.session.add(new_book)
    db.session.commit()

    return new_book.to_json(), 201
    # return {
    #     "success": True,
    #     "message": f"Book {new_book.title} has been created"
    # }, 201


@books_bp.route("<book_id>", methods=["PUT"], strict_slashes=False)
def update_book(book_id):
    if not is_int(book_id):
        return make_response("", 404)

    book = Book.query.get(book_id)
    if book is None:
        return make_response("", 404)

    request_body = request.get_json()

    book.title = request_body["title"]
    book.description = request_body["description"]

    db.session.commit()

    return jsonify({
        "success": True,
        "message": f"Book {book_id} successfully updated"
    }), 200


@books_bp.route("<book_id>", methods=["DELETE"], strict_slashes=False)
def delete_book(book_id):

    book = Book.query.get(book_id)
    if book is None:
        return make_response("", 404)

    db.session.delete(book)
    db.session.commit()

    return {
        "success": True,
        "message": f"Book {book_id} successfully deleted"
    }, 200





# @books_bp.route("", methods=["GET", "POST"], strict_slashes=False)
# def handle_books():
#     if request.method == "GET":
#         books = Book.query.all()
#         books_response = []
#         for book in books:
#             books_response.append({
#                 "id": book.id,
#                 "title": book.title,
#                 "description": book.description
#             })
#         return jsonify(books_response), 200

#     elif request.method == "POST":
#         request_body = request.get_json()

#         new_book = Book(title=request_body["title"],
#                         description=request_body["description"])

#         db.session.add(new_book)
#         db.session.commit()

#         return make_response(f"Book {new_book.title} successfully created", 201)

    # return {
    #       "success": True,
    #       "message": f"Book {new_book.title} has been create"
    #   }, 201




# hello_world_bp = Blueprint("hello_world", __name__)

# @hello_world_bp.route("/hello-world", methods=["GET"])
# def get_hello_world():
#     my_response = "Hello, World!"
#     return my_response


# @hello_world_bp.route("/hello/JSON", methods=["GET"])
# def hello_world_json():
#     return {
#         "name": "Ada Lovelace",
#         "message": "Hello!",
#         "hobbies": ["Fishing", "Swimming", "Watching Reality Shows"]
#     }

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