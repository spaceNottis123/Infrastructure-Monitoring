from app import db

class Author(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    books = db.relationship('Book', backref='author', lazy=True)

    def __repr__(self):
        return f'<Author {self.name}>'
    
class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    author_id = db.Column(db.Integer, db.ForeignKey('author.id'), nullable=False)
    member_id = db.Column(db.Integer, db.ForeignKey('member.id'), nullable=True)
    author = db.relationship('Author', backref='books')
    member = db.relationship('Member', backref='books', lazy=True)

    def __repr__(self):
        return f'<Book {self.title}>'

class Member(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    loans = db.relationship('Loan', backref='member', lazy=True)
    books = db.relationship('Book', backref='borrowed_by', lazy=True)

    def __repr__(self):
        return f'<Member {self.name}>'

class Loan(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    book_id = db.Column(db.Integer, db.ForeignKey('book.id'), nullable=False)
    member_id = db.Column(db.Integer, db.ForeignKey('member.id'), nullable=False)
    loan_date = db.Column(db.Date, nullable=False)
    return_date = db.Column(db.Date, nullable=True)
    book = db.relationship('Book', backref='loans')
    member = db.relationship('Member', backref='loans')

    def __repr__(self):
        return f'<Loan Book ID {self.book_id} Member ID {self.member_id}>'