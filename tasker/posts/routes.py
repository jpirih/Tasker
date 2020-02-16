from flask import render_template, redirect, url_for
from flask_login import login_required, current_user

from tasker.models import Post
from flask_classful import FlaskView, route
from tasker.posts.forms import NewPostForm


class PostsView(FlaskView):
    route_base = '/posts'

    @route('/', methods=['GET', 'POST'])
    @login_required
    def index(self):
        """Posts list view controller"""
        title: str = 'Post List'
        form = NewPostForm()
        posts = Post.get_posts()

        if form.validate_on_submit():
            Post.save(body=form.body.data, user_id=current_user.id)
            return redirect(url_for('MainView:index'))

        return render_template('posts/posts.html', form=form, title=title, posts=posts)
