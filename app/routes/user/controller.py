from flask import Blueprint, request
import json
from app.helpers.database.database import get_all_users, get_user_by_id, get_user_homes, login_current_user

user_routes = Blueprint('user', __name__, url_prefix='')


@user_routes.route('/users/login', methods=['POST'])
def login():
    email = request.form['username']
    password = request.form['password']

    if email and password:
        user = login_current_user(email, password)
        return json.dumps(user)
    return {}


@user_routes.route('/all', methods=['GET'])
def get_users():
    return json.dumps(get_all_users())


@user_routes.route('/user/<id>', methods=['GET'])
def get_current_user(id):
    u = get_user_by_id(id)

    return json.dumps(u)


@user_routes.route('/user/<id>/homes', methods=['GET'])
def get_current_user_homes(id):
    u = get_user_homes(id)

    return json.dumps(u)
