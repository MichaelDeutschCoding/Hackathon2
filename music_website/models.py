from flask_login import UserMixin
from music_website import db


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(16), unique=True, nullable=False)
    email = db.Column(db.String(50), unique=True, nullable=False)
    password_hashed = db.Column(db.String(80), nullable=False)
    first_name = db.Column(db.String(32))
    last_name = db.Column(db.String(32))


class Music(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    path = db.Column(db.String(256))


class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    music_id = db.Column(db.Integer, db.ForeignKey('music.id'))
    author_id = db.Column(db.Integer, db.ForeignKey('user.id'))
#
# class Tag(db.Model):
#     pass
#
# project = db.Table(
#
# )