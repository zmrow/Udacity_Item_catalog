import datetime
from controller import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120), unique=True)
    created_at = db.Column(db.DateTime, nullable=False)

    categories = db.relationship('Category', backref='user', lazy='dynamic')
    items = db.relationship('Item', backref='user', lazy='dynamic')

    def __init__(self, username, email):
        self.username = username
        self.email = email
        self.created_at = datetime.datetime.utcnow()


class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True)
    created_at = db.Column(db.DateTime, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    items = db.relationship('Item', backref='category', lazy='dynamic')

    def __init__(self, username, email):
        self.name = name
        self.created_at = datetime.datetime.utcnow()


class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True)
    description = db.Column(db.Text, unique=True)
    created_at = db.Column(db.DateTime, nullable=False)

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'))

    def __init__(self, username, email):
        self.name = name
        self.description = description
        self.created_at = datetime.datetime.utcnow()
