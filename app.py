from flask import Flask, request, render_template, flash
import flask_login
from flask_sqlalchemy import SQLAlchemy
from config import Config
login_manager = flask_login.LoginManager()
# from models import User


app = Flask(__name__)
app.config.from_object(Config)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
login_manager.init_app(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=True, nullable=False)        # todo hide password
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password


def form(name):
    return request.form[name]


@app.route("/signup", methods=['POST', 'GET'])
def create_user():
    if request.method == 'GET':
        return render_template('signup.html')

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

@app.route('/')
def hello():
    return "Hello World!"


# @app.route('/<name>')
# def hello_name(name):
#     return "Hello {}!".format(name)


if __name__ == '__main__':
    db.create_all()
    app.run()
