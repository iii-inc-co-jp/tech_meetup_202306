from flask import Blueprint
from service import Service

api = Blueprint('api', __name__, url_prefix='/api')

service = Service()

@api.route('/users', methods=['GET'])
def list_user():
    return service.get_users()


@api.route('/users/<string:user_id>', methods=['GET'])
def get_user(user_id=None):
    return service.get_user(user_id)

