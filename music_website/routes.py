from flask import Blueprint, render_template, redirect, url_for
from flask_login import login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from music_website.forms import LoginForm, RegisterForm
from music_website.models import User
from music_website import db
from music_website import login_manager

main_routes = Blueprint('main', __name__, 'templates/')
login_manager.login_view = 'login'


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


@main_routes.route('/')
def index():
    return render_template('index.html')


@main_routes.route('/login', methods=['GET', 'POST'])
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


@main_routes.route('/sign-up', methods=['GET', 'POST'])
def signup():
    form = RegisterForm()

    if form.validate_on_submit():
        hashed_password = generate_password_hash(form.password.data, method='sha256')
        # noinspection PyArgumentList
        new_user = User(username=form.username.data,
                        email=form.email.data,
                        password=hashed_password,
                        first_name=form.first_name.data,
                        last_name=form.last_name.data
                        )
        db.session.add(new_user)
        db.session.commit()

        return '<h1>New user has been created!</h1>'

    return render_template('signup.html', form=form)


@main_routes.route('/dashboard')
@login_required
def dashboard():
    return render_template('register.html', name=current_user.username)


@main_routes.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))
