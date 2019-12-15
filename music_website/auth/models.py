from flask_login import UserMixin
from music_website import db


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(16), unique=True, nullable=False)
    email = db.Column(db.String(50), unique=True, nullable=False)
    password_hashed = db.Column(db.String(80), nullable=False)
    first_name = db.Column(db.String(32))
    last_name = db.Column(db.String(32))

