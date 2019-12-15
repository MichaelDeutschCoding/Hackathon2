import random
from flask import Flask
from flask_bootstrap import Bootstrap
from music_website.auth import login_manager
from music_website.database import db, migrate


app = Flask(__name__)

app.config['SECRET_KEY'] = random._urandom(56)
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = "postgres://postgres@localhost/mixmusic"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

Bootstrap(app)

login_manager.init_app(app)
db.init_app(app)
migrate.init_app(app, db)


from music_website import routes
from music_website.auth import routes as auth_routes
from music_website.music import routes as music_routes
app.register_blueprint(routes.main_routes)
app.register_blueprint(auth_routes.auth_routes)
app.register_blueprint(music_routes.music_routes)