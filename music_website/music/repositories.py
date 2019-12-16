from flask import session

from music_website.music.models import Sample, Tag
from sqlalchemy.dialects.postgresql import insert


class SampleRepository:
    def __init__(self, session):
        self.session = session

    def add_new(self, title, path, description, tags, current_user):
        current_user = current_user
        sample = Sample(
            title=title,
            path=path,
            description=description,
            tags=tags,
            user_id=current_user
        )
        self.session.add(sample)


class TagRepository:
    def __init__(self, session):
        self.session = session

    def add_tags(self, tags):
        stmt = insert('tag').values(tags)
        stmt = stmt.on_conflict_do_nothing()
        self.session.execute(stmt)
