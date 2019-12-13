from flask_login import UserMixin
from music_website import db


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(15), unique=True)
    email = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(80))
    first_name = db.Column(db.String(32))
    last_name = db.Column(db.String(32))



class Music(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey(user.id))


class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    music_id = Column(db.Integer, ForeignKey('music.id'))
    author_id = Column(db.Integer, ForeignKey('user.id'))