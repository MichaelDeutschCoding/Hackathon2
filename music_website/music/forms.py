from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import InputRequired, Length


class TagsField(StringField):
    def _value(self):
        if self.data:
            return u', '.join(self.data)
        else:
            return u''

    def process_formdata(self, valuelist):
        if not valuelist:
            self.data = []
        self.data = [t.strip() for t in valuelist[0].split(',')]


class AddSampleForm(FlaskForm):
    title = StringField('Title', validators=[InputRequired(), Length(max=64)])
    path = StringField('Path', validators=[InputRequired(), Length(max=256)])
    description = StringField('Description')
    tags = TagsField('Add Tags separated by a comma')


class WriteCommentForm(FlaskForm):
    text = StringField('Add a comment', validators=[InputRequired(), Length(max=256)])
