from flask import render_template
from tasker.main import bp
from tasker.models import  Post


@bp.route('/')
def home() -> str:
    """Main page view controller"""
    title: str = 'Home'
    posts = Post.get_latest_posts()
    return render_template('main/index.html', posts=posts, title=title)
