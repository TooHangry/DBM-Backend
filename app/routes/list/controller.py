from flask import Blueprint, request
from app.helpers.database import database
import datetime
import json

list_routes = Blueprint('list', __name__, url_prefix='')

@list_routes.route('/lists', methods=['GET'])
def get_default_lists():
    return json.dumps(database.get_lists())

@list_routes.route('/lists/home/<id>', methods=['GET'])
def get_lists_from_home(id):
    return json.dumps(database.get_lists_in_home(id))

@list_routes.route('/lists/create', methods=['POST'])
def create_list():
    data = data = request.form
    print(data)
    format = "%m/%d/%Y" 
    title = data['title']
    tasked_user = data['taskedUserID']
    home = data['home']
    is_complete = True if data['isComplete'] == 'true' else False
    start_date = datetime.datetime.strptime(data['dateTasked'], format)
    end_date = datetime.datetime.strptime(data['dateDue'], format)
    
    return database.create_list(title, tasked_user, home, is_complete, start_date, end_date)

@list_routes.route('lists/updateitems/<id>', methods=['PUT'])
def update_list(id):
    data = request.form
    items = json.loads(data['items'])
    
    database.update_list(id, items)
    return json.dumps(database.get_list_by_id(id))
# /lists/mine/id
#   Gets user lists (pass userID as query param)

# /lists/home/id
#   Gets lists in a home (pass in homeIDas query param)

# /lists/add
#   Create a new list (pass in formdata with name, homeID, adminID, etc.)

# /lists/remove/id
#   Delete home with id from query param

# /lists/update/id
#   Update the list at 'id' with passed-in form data