from flask import render_template
from tasker.main import bp


@bp.route('/')
def home():
    """Main page view controller"""
    title: str = 'Home'
    return render_template('main/index.html', title=title)
