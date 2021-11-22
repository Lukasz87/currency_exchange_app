from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_user, login_required, logout_user
from werkzeug.security import generate_password_hash, check_password_hash
from .models import User
from .db import db

auth = Blueprint('auth', __name__)


def form(val):
    return request.form.get(val)


@auth.route('/login', methods=['POST', 'GET'])
def login():
    remember = True if request.form.get('remember') else False
    if request.method == 'GET':
        return render_template('login.html')
    email = form('email')
    password = form('password')
    user = User.query.filter_by(email=email).first()
    if not user or not check_password_hash(user.password, password):
        flash('Please check your login details and try again.')
        return redirect(url_for('auth.login'))
    login_user(user, remember=remember)
    return redirect(url_for('main.profile'))


@auth.route('/signup', methods=['POST', 'GET'])
def signup():
    if request.method == 'GET':
        return render_template('signup.html')
    username = form('username')
    email = form('email')
    password = form('password')
    user = User.query.filter_by(email=email).first()
    if user:
        flash('Email address already exists')
        return redirect(url_for('auth.signup'))
    new_user = User(username, email, password=generate_password_hash(password, method='sha256'))  # todo orm to method
    db.session.add(new_user)
    db.session.commit()
    return redirect(url_for('auth.login'))


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.index'))
