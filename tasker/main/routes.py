from typing import List
import os

from flask import render_template, url_for
from tasker.models import Post
from flask_classful import FlaskView


class MainView(FlaskView):
    route_base = '/'

    def index(self) -> str:
        """Main page view controller"""
        title: str = 'Home'
        posts = Post.get_latest_posts()
        about_app: List = []
        f = open(os.path.abspath('tasker/static/files/about.txt'), 'r')
        for row in f:
            about_app.append(row)

        return render_template('main/index.html', about=about_app, posts=posts, title=title)
