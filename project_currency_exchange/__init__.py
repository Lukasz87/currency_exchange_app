from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .auth import auth as auth_blueprint
from flask_login import LoginManager
from .main import main as main_blueprint
from .models import User

# init SQLAlchemy so we can use it later in our models
db = SQLAlchemy()


class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = False
    SECRET_KEY = 'kopytko'
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:postgres@localhost/app_exchange_rate'


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    # login_manager = LoginManager()
    # login_manager.login_view = 'auth.login'
    # login_manager.init_app(app)
    #
    # @login_manager.user_loader
    # def load_user(user_id):
    #     # since the user_id is just the primary key of our user table, use it in the query for the user
    #     return User.query.get(int(user_id))

    # blueprint for auth routes in our app
    app.register_blueprint(auth_blueprint)
    # blueprint for non-auth parts of app
    app.register_blueprint(main_blueprint)

    return app


