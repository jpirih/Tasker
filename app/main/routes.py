from app.main import bp
from flask import render_template


@bp.route('/')
def home():
    """Main page view controller"""
    title:str = 'Home'
    return render_template('main/index.html', title=title)
