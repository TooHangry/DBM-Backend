from flask import Blueprint

default_routes = Blueprint('default', __name__, url_prefix='')

@default_routes.route('/', methods=['GET'])
def get_default():
    return 'Hello, World!'