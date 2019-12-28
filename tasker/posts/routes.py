from flask import render_template,redirect, url_for
from flask_login import login_required, current_user

from tasker.models import Post
from tasker.posts import bp
from tasker.posts.forms import NewPostForm


@bp.route('/posts', methods=['GET', 'POST'])
@login_required
def posts():
    """Posts list view controller"""
    title: str = 'Post List'
    form = NewPostForm()
    posts = Post.get_posts()

    if form.validate_on_submit():
        Post.save(body=form.body.data,user_id=current_user.id)
        return redirect(url_for('main.home'))

    return render_template('posts/posts.html', form=form, title=title, posts=posts)
