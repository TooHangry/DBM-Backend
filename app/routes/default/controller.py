from flask import Blueprint
from app.helpers.database import database

default_routes = Blueprint('default', __name__, url_prefix='')

@default_routes.route('/', methods=['GET'])
def get_default():
    return 'Hello, World!'


@default_routes.route('/stats', methods=['GET'])
def get_stats():
    all_users = database.get_all_users()
    all_items = database.get_all_items()
    all_homes = database.get_all_homes()
    all_lists = database.get_all_lists()

    return {
        'User Count': len(all_users),
        'Item Count': len(all_items),
        'Home Count': len(all_homes),
        'List Count': len(all_lists)
    }
