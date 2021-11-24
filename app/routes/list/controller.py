from flask import Blueprint, request
from app.helpers.database import database
import datetime
import json

list_routes = Blueprint('list', __name__, url_prefix='')

@list_routes.route('/lists', methods=['GET'])
def get_default_lists():
    return json.dumps(database.get_lists())

@list_routes.route('/lists/remove/<id>', methods=['DELETE'])
def remove_list(id):
    list_value = database.get_list_by_id(id)
    database.remove_list(id)
    return json.dumps(database.get_lists_in_home(list_value['homeID']))

@list_routes.route('/lists/home/<id>', methods=['GET'])
def get_lists_from_home(id):
    return json.dumps(database.get_lists_in_home(id))

@list_routes.route('/lists/create', methods=['POST'])
def create_list():
    data = data = request.form
    format = "%m/%d/%Y" 
    title = data['title']
    tasked_user = data['taskedUserID']
    home = data['home']
    is_complete = True if data['isComplete'] == 'true' else False
    end_date = datetime.datetime.strptime(data['dateDue'], format)
    
    return database.create_list(title, tasked_user, home, is_complete, end_date)

@list_routes.route('lists/updateitems/<id>', methods=['PUT'])
def update_list(id):
    data = request.form
    items = json.loads(data['items'])
    user = int(json.loads(data['user']))
    title = data['title']

    database.update_list(id, items, user, title)
    return json.dumps(database.get_list_by_id(id))

@list_routes.route('lists/mine/<id>', methods=['GET'])
def get_user_lists(id):
    return json.dumps(database.get_user_lists(id))
