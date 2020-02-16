from tasker.models import User, UsersSchema
from flask import jsonify
from flask_classful import FlaskView


class UsersApiView(FlaskView):
    route_prefix = '/api/'
    route_base = '/users/'

    def index(self):
        users = User.query.all()
        users_schema = UsersSchema(exclude=['password_hash'], many=True)
        output = users_schema.dump(users)
        return jsonify({'uses': output})
