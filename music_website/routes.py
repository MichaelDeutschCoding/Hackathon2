from flask import Blueprint, render_template, redirect, url_for
from music_website.auth import login_manager
from flask_bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app)

main_routes = Blueprint('main', __name__, 'templates/')
login_manager.login_view = 'login'

@main_routes.route('/index')
def index():
    return render_template('index.html')


@main_routes.route('/testplayback')
def test_playback():
    return render_template('playback.html')