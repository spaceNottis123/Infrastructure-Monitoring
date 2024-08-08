from flask import Blueprint, jsonify, request
from app import db
from models import Author, Book


bp = Blueprint('main', __name__)

#Author Routes
@bp.route('/authors', methods=['GET'])
def get_authors():
    authors = Author.query.all()
    return jsonify([{'id': author.id, 'name': author.name} for author in authors])

@bp.route('/authors', methods=['POST'])
def add_author():
    data = request.get_json()
    new_author = Author(name=data['name'])
    db.session.add(new_author)
    db.session.commit()
    return jsonify({'id': new_author.id, 'name': new_author}), 201

#Book routes
@bp.route('/books', methods=['GET'])
def get_books():
    books = Book.query.all()
    return jsonify([{
        'id': book.id,
        'title': book.title,
        'author_id': book.author_id,
        'member_id': book.member_id
    } for book in books])
