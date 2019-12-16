from flask import Blueprint, render_template, redirect, url_for
from flask_login import login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from music_website.auth.forms import LoginForm, RegisterForm
from music_website import db
from music_website.auth import login_manager
from music_website.auth.models import User
from music_website.auth.repositories import UserRepository

auth_routes = Blueprint('auth', __name__, 'templates/')

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


@auth_routes.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user:
            if check_password_hash(user.password, form.password.data):
                login_user(user, remember=form.remember.data)
                return redirect(url_for('dashboard'))

        return '<h1>Invalid username or password</h1>'

    return render_template('login.html', form=form)


@auth_routes.route('/register', methods=['GET', 'POST'])
def signup():
    form = RegisterForm()

    if form.validate_on_submit():
        repo = UserRepository()
        repo.register(form.username.data,
                      form.email.data,
                      form.password.data,
                      form.first_name.data,
                      form.last_name.data)
        # should redirect to dashboard
        return '<h1>New user has been created!</h1>'

    return render_template('register.html', register_form=form)


@auth_routes.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html')


@auth_routes.route('/logout')
# @login_required
def logout():
    logout_user()
    return redirect(url_for('index'))
