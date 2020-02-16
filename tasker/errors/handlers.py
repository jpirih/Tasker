from flask import render_template


class ErrorsHandler:
    @staticmethod
    def page_not_found(e) -> str:
        """Page not found controller"""
        return render_template('errors/404.html', error=e), 404
