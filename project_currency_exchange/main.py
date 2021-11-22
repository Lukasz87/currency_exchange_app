
from flask import Blueprint, render_template, request
from . import db
from . models import User

main = Blueprint('main', __name__)


@main.route('/')
def index():
    return render_template('index.html')


@main.route('/profile')
def profile():
    return render_template('profile.html')


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