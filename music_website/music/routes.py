from flask import Blueprint, render_template, redirect, url_for
from flask_login import current_user, login_user

from music_website.auth.models import User
from music_website.database import session_scope
from music_website.music.forms import AddSampleForm
from music_website.music.models import Sample
from music_website.music.repositories import SampleRepository, TagRepository

music_routes = Blueprint('music', __name__, 'templates/')


@music_routes.route('/dashboard')
# @login_required
def dashboard():
    sample_list = Sample.query.all()[:10]
    return render_template('dashboard.html',  sample_list=sample_list)


@music_routes.route('/upload', methods=['GET', 'POST'])
# @login_required
def add_sample():
    user = User.query.filter_by(id=1).first()
    login_user(user)

    form = AddSampleForm()
    if form.validate_on_submit():
        with session_scope() as session:
            tag_repo = TagRepository(session)
            tags = tag_repo.add_tags(form.tags.data)

            sample_repo = SampleRepository(session)
            sample_repo.add_new(
                form.title.data,
                form.path.data,
                form.description.data,
                tags,
                current_user
            )

        return redirect(url_for('music.dashboard'))

    return render_template('upload.html', form=form)