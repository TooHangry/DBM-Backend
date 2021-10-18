from flask import Blueprint, request
import json
from app.helpers.database import database

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

    print(name, invite_list)

    return json.dumps(database.create_new_home(name, admin, invite_list))