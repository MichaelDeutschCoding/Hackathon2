from music_website import db

sample_tags = db.Table('sample_tags',
                       db.Column('sample_id', db.Integer, db.ForeignKey('sample.id'), primary_key=True),
                       db.Column('tag_name', db.String, db.ForeignKey('tag.name'), primary_key=True)
                       )


class Sample(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(64), nullable=False)
    path = db.Column(db.String(256), nullable=False)
    description = db.Column(db.String(512))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    tags = db.relationship('Tag',
                           secondary=sample_tags,
                           lazy='subquery',
                           backref=db.backref('samples', lazy=True))
    comments = db.relationship('Comment', backref='sample', lazy=True)


class Tag(db.Model):
    name = db.Column(db.String(32), primary_key=True)

class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    sample_id = db.Column(db.Integer, db.ForeignKey('sample.id'))
    author_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    text = db.Column(db.String(256), nullable=False)
