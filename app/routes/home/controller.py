from flask import Blueprint, request
import json
from app.helpers.database import database
from app.helpers.user.queries import get_user_by_email

home_routes = Blueprint('home', __name__, url_prefix='')

@home_routes.route('/homes', methods=['GET'])
def get_homes():
    return json.dumps(database.get_all_homes())

@home_routes.route('/home/<id>', methods=['GET'])
def get_home_info(id):
    return json.dumps(database.get_home_info(id))

@home_routes.route('/home/add', methods=['POST'])
def create_home():
    data = request.form

    name = data['name']
    invite_list = json.loads(data['invites'])
    admin = data['admin']

    return json.dumps(database.create_new_home(name, admin, invite_list))

@home_routes.route('/home/adduser', methods=['POST'])
def add_user():
    data = request.form
    res = database.add_user(data['user'], int(data['homeID']))
    user = database.get_user_by_email(data['user'])
    print(user)
    if user:
        return json.dumps(user)
    return {
        'success': 400
    }