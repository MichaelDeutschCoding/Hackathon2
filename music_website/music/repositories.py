from music_website.music.models import Sample, Tag, Comment
from music_website import db


class SampleRepository:
    def __init__(self, session):
        self.session = session

    def add_new(self, title, path, description, tags, current_user):
        sample = Sample(
            title=title,
            path=path,
            description=description,
            tags=tags,
            user_id=current_user.id
        )
        self.session.add(sample)


class TagRepository:
    def __init__(self, session):
        self.session = session

    def add_tags(self, tags):
        tags = set(tags)
        existing_tag_objs = list(Tag.query.filter(Tag.name.in_(tags)))
        existing_tags = {tag.name for tag in existing_tag_objs}
        missing_tags = [Tag(name=name) for name in tags - existing_tags]
        for tag in missing_tags:
            self.session.add(tag)

        return missing_tags + existing_tag_objs

class CommentRepository:
    def add_comment(self, sample_id, current_user, text):
        comment = Comment(
            sample_id=sample_id,
            author_id=current_user.id,
            text=text
        )

        db.session.add(comment)
        db.session.commit()
