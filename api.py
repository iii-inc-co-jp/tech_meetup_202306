from flask import Blueprint
from service import Service

api = Blueprint('api', __name__, url_prefix='/api')


@api.route('/users', methods=['GET'])
def list_user():
    return Service.get_users


@api.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id=None):
    return Service.get_user(user_id)

