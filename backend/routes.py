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

@bp.route('/post', methods=['POST'])
def add_book():
    data = request.get_json()
    new_book = Book(title=data['title'], author_id=data['author_id'])
    db.session.add(new_book)
    db.session.commit()
    return jsonify({'id': new_book.id, 'title': new_book.title}), 201

@bp.route('/books/<int:id>', methods=['GET'])
def get_book(id):
    book = Book.query.get_or_404(id)
    return jsonify({
        'id': book.id,
        'title': book.title,
        'author_id': book.author_id,
        'member_id': book.member_id
    })

@bp.route('/books/<int:id>', methods=['PUT'])
def update_book(id):
    data = request.get_json()
    book = Book.query.get_or_404(id)
    book.title = data['title']
    book.author_id = data['author_id']
    db.session.commit()
    return jsonify({
        'id': book.id,
        'title': book.title,
        'author_id': book.author_id
    })

@bp.route('/books/<int:id>', methods=['DELETE'])
def delete_book(id):
    book = Book.query.get_or_404(id)
    db.session.delete(book)
    db.session.commit()
    return '', 204

# Member Routes
@bp.route('/members', methods=['GET'])
def get_members():
    members = Member.query.all()
    return jsonify([{'id': member.id, 'name': member.name} for member in members])

@bp.route('/members', methods=['POST'])
def add_member():
    data = request.get_json()
    new_member = Member(name=data['name'])
    db.session.add(new_member)
    db.session.commit()
    return jsonify({'id': new_member.id, 'name': new_member.name}), 201

# Loan Routes
@bp.route('/loans', methods=['POST'])
def create_loan():
    data = request.get_json()
    new_loan = Loan(
        book_id=data['book_id'],
        member_id=data['member_id'],
        loan_date=data['loan_date']
    )
    db.session.add(new_loan)
    db.session.commit()
    return jsonify({'id': new_loan.id}), 201

@bp.route('/loans/<int:id>', methods=['PUT'])
def return_loan(id):
    data = request.get_json()
    loan = Loan.query.get_or_404(id)
    loan.return_date = data['return_date']
    db.session.commit()
    return jsonify({'id': loan.id, 'return_date': loan.return_date})
