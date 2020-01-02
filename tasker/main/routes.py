from typing import List

from flask import render_template
from tasker.main import bp
from tasker.models import Post


@bp.route('/')
def home() -> str:
    """Main page view controller"""
    title: str = 'Home'
    posts = Post.get_latest_posts()
    about_app: List = []
    f = open('tasker/static/files/about.txt', 'r')
    for row in f:
        about_app.append(row)

    return render_template('main/index.html', about=about_app, posts=posts, title=title)
