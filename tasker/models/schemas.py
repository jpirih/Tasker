from tasker import ma
from tasker.models import User, Post


class UsersSchema(ma.ModelSchema):
    class Meta:
        model = User


class PostsSchema(ma.ModelSchema):
    class Meta:
        model = Post
