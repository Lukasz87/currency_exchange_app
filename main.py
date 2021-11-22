from exchange_rates_connector import FreeCurrencyApi
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

# Define the WSGI application object
app = Flask(__name__)

# Configurations
app.config.from_object('config')
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///app_exchange_rate'

# database
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    rates = FreeCurrencyApi()
    get_rates = rates.get_rates('USD')
    print(get_rates)

