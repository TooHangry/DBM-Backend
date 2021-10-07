from flask import Blueprint, config, request, abort
import json
from secrets import token_urlsafe
from app.helpers.database import database
from app.helpers.user import helpers
user_routes = Blueprint('user', __name__, url_prefix='')

@user_routes.route('/login', methods=['POST'])
def login():
    email = request.form['email']
    password = request.form['password']

    if email and password:
        hashed_password = helpers.get_hashed_password(password)
        return json.dumps(database.login_current_user(email, hashed_password))
    abort(404)

@user_routes.route('/login/token', methods=['POST'])
def login_token():
    token = request.form['token']
    if token:
        return json.dumps(database.login_from_token(token))
    abort(404)

@user_routes.route('/signup', methods=['POST'])
def signup():
    email = request.form['email']
    password = request.form['password']
    fname = request.form['fname']
    lname = request.form['lname']
    merged = lname + fname

    if email and password and fname and lname:
        hashed_password = helpers.get_hashed_password(password)
        token = token_urlsafe(len(merged)) + merged
        database.create_user(email, fname, lname, hashed_password, token)
        return json.dumps(database.login_current_user(email, hashed_password))
    abort(404)

@user_routes.route('/all', methods=['GET'])
def get_users():
    return json.dumps(database.get_all_users())

@user_routes.route('/user/<id>', methods=['GET'])
def get_current_user(id):
    return json.dumps(database.get_user_by_id(id))

@user_routes.route('/user/<id>/homes', methods=['GET'])
def get_current_user_homes(id):
    return json.dumps(database.get_user_homes(id))