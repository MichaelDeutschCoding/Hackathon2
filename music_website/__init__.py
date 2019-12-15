import random
from flask import Flask
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate


app = Flask(__name__)

app.config['SECRET_KEY'] = random._urandom(56)
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = "postgres://postgres@localhost/mixmusic"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

Bootstrap(app)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

login_manager = LoginManager()
login_manager.init_app(app)


from music_website import models, routes

app.register_blueprint(routes.main_routes)