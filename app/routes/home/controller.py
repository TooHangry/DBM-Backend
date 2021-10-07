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