import datetime
from Udacity_Item_catalog import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120), unique=True)
    created_at = db.Column(db.DateTime, nullable=False)

    def __init__(self, username, email):
        self.username = username
        self.email = email
        self.created_at = datetime.datetime.utcnow()

