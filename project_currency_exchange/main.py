
from flask import Blueprint, render_template, request
from .db import db
from . models import User, Wallet, Currency
from flask_login import login_required, current_user
from .exchange_rates_connector import FreeCurrencyApi

main = Blueprint('main', __name__)


@main.route('/')
def index():
    return render_template('index.html')


@main.route('/profile')
@login_required
def profile():
    return render_template('profile.html', user=current_user)


def form(name):
    return request.form[name]


@main.route("/signup", methods=['POST', 'GET'])
def create_user():
    if request.method == 'GET':
        return render_template('old_signup.html')

    else:
        try:
            username = form('username')
            email = form('email')
            password = form('password')
            new_user = User(username, email, password) # todo orm to method
            db.session.add(new_user)
            db.session.commit()
        except:
            return 'Error in create user'       # todo refactor

        return f"User {username} created"


@main.route("/wallet", methods=['POST', 'GET'])
@login_required
def wallet():
    wallet_recs = Wallet.query.filter_by(user_id=current_user.id).all()
    currency_recs = Currency.query.all()
    return render_template('wallet.html', wallet=wallet_recs, currency=currency_recs )


