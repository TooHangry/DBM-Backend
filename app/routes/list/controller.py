from flask import Blueprint

list_routes = Blueprint('list', __name__, url_prefix='')

@list_routes.route('/lists', methods=['GET'])
def get_default():
    return {
        'lists': []
    }

# /lists/mine/id
# /lists/home/id
# /lists/add
# /lists/remove/id
# /lists/update/id