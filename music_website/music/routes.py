from flask import Blueprint, render_template, redirect, url_for, flash
from flask_login import current_user, login_required

from music_website.auth.models import User
from music_website.database import session_scope
from music_website.music.forms import AddSampleForm, SearchByTagForm
from music_website.music.models import Sample, Tag
from music_website.music.repositories import SampleRepository, TagRepository

music_routes = Blueprint('music', __name__, 'templates/')


@music_routes.route('/dashboard', methods=['GET', 'POST'])
# @login_required
def dashboard():
    search_form = SearchByTagForm()
    if search_form.validate_on_submit():
        searched_tag = search_form.search.data
        return redirect(url_for('music.search', tag=searched_tag))
    sample_list = Sample.query.all()[:10]
    return render_template('dashboard.html',  sample_list=sample_list, search_form=search_form)


@music_routes.route('/upload', methods=['GET', 'POST'])
@login_required
def add_sample():

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

@music_routes.route('/search/<tag>')
# @login_required
def search(tag):
    tag_obj =Tag.query.filter(Tag.name ==tag).first()
    if not tag_obj:
        flash(f"No samples found under the tag: {tag}")
        return redirect(url_for('music.dashboard'))
    sample_list = tag_obj.samples
    return render_template('search.html', tag=tag, sample_list=sample_list)


@music_routes.route('/sample/<sample_id>')
# @login_required
def sample_page(sample_id):
    sample = Sample.query.filter_by(id=sample_id).first()
    if not sample:
        flash(f"No sample with the id: {sample_id}")
        return redirect(url_for('music.dashboard'))
    owner = User.query.filter_by(id=sample.user_id).first()
    comment_tuples = [(User.query.filter_by(id=c.author_id).one().username, c.text)
                      for c in sample.comments]
    return render_template('sample_page.html',
                           sample=sample,
                           owner=owner,
                           comment_tuples = comment_tuples)