from tasker.errors import bp
from flask import render_template


@bp.app_errorhandler(404)
def page_not_found(e):
    """Page not found controller"""
    return render_template('errors/404.html', error=e), 404
