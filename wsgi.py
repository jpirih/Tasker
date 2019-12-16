from tasker import create_app
from tasker import db
from tasker.models import User, Post


app = create_app()


@app.shell_context_processor
def make_shell_context() -> dict:
    return {'db': db, 'User': User, 'Post': Post}


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
