from .db import db
from flask_login import UserMixin


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(200), unique=True, nullable=False)        # todo hide password
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password


class Wallet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    currency_code = db.Column(db.String(3), unique=True, nullable=False)
    qty = db.Column(db.Numeric, default=0)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)


class Currency(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    country = db.Column(db.String(100), unique=False, nullable=False)
    name = db.Column(db.String(100), unique=False, nullable=False)
    code = db.Column(db.String(3), unique=False, nullable=False)
    minor_unit = db.Column(db.Integer, nullable=False)
    symbol = db.Column(db.String(100), unique=False, nullable=True)


class CurrencyRates(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_currency = db.Column(db.Integer, db.ForeignKey('currency.id'), nullable=False)
    second_currency = db.Column(db.Integer, db.ForeignKey('currency.id'), nullable=False)
    rate = db.Column(db.Numeric)

    def __init__(self, first_currency, second_currency, rate):
        self.first_currency = first_currency
        self.second_currency = second_currency
        self.rate = rate


