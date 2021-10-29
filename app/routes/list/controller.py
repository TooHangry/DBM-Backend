from flask import Blueprint, request
import json
from app.helpers.database import database

list_routes = Blueprint('list', __name__, url_prefix='')

@list_routes.route('/lists', methods=['GET'])
def get_default():
    return {
        'lists': []
    }

# /lists/mine/id
#   Gets user lists (pass userID as query param)
@list_routes.route('/lists/mine/<id>', methods=['GET'])
def get_user_lists(id):
    return json.dumps(database.get_user_lists(id))  #can view with 127.0.0.1:5000

# /lists/home/id
#   Gets lists in a home (pass in homeIDas query param)
@list_routes.route('/lists/home/<id>', methods=['GET'])
def get_home_lists(id):
    return json.dumps(database.get_home_lists(id))

# /lists/add
#   Create a new list (pass in formdata with name, homeID, adminID, etc.)
@list_routes.route('/lists/add', methods=['POST'])
def create_list():
    data = request.form

    tasked_to = data['taskedTo']
    home_tasked = data['homeTasked']

    return json.dumps(database.create_list(tasked_to, home_tasked))

# /lists/remove/id
#   Delete home with id from query param
@list_routes.route('/lists/remove/<id>', methods=['GET'])
def remove_list(id):
    return json.dumps(database.remove_list(id))

# /lists/update/id
#   Update the list at 'id' with passed-in form data