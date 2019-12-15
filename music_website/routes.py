from flask import Blueprint, render_template, redirect, url_for
from music_website.auth import login_manager

main_routes = Blueprint('main', __name__, 'templates/')
login_manager.login_view = 'login'

@main_routes.route('/')
def index():
    return render_template('index.html')
