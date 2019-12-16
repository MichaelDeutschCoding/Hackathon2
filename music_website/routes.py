from flask import Blueprint, render_template, Flask
from flask_bootstrap import Bootstrap
from music_website.auth import login_manager

app = Flask(__name__)
Bootstrap(app)

main_routes = Blueprint('main', __name__, 'templates/')
login_manager.login_view = 'login'

@main_routes.route('/')
def index():
    return render_template('index.html')


@main_routes.route('/testplayback')
def test_playback():
    return render_template('playback.html')