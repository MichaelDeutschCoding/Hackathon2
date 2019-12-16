import hashlib

from music_website import db
from music_website.auth.models import User

class UserRepository:
    def register(self,
                 username,
                 email,
                 password,
                 first_name,
                 last_name,
                 ):
        # noinspection PyArgumentList
        user = User(username=username,
                    email=email,
                    password_hashed=hashlib.sha256(password.encode('utf-8')).digest(),
                    first_name=first_name,
                    last_name=last_name,
                    )
        db.session.add(user)
        db.session.commit()