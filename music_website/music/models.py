from music_website import db


class Sample(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    path = db.Column(db.String(256))


class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    music_id = db.Column(db.Integer, db.ForeignKey('music.id'))
    author_id = db.Column(db.Integer, db.ForeignKey('user.id'))



# class Tag(db.Model):
#     pass
#
# project = db.Table(
#
# )