from . import db
from flask_login import UserMixin


# class User(UserMixin, db.Model):
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(200), unique=True, nullable=False)        # todo hide password
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password
