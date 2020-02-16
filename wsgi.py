from tasker import app
from tasker import db
from tasker.models import User, Post
from tasker.data_seeder import PostsSeeder

posts_seeder = PostsSeeder()


@app.shell_context_processor
def make_shell_context() -> dict:
    return {'db': db, 'User': User, 'Post': Post}


@app.cli.command(help='Saves sample posts to db.')
def seed_posts():
    posts_seeder.seed_sample_posts()


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
