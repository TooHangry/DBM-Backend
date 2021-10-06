from flask import Blueprint, request
import json
from app.helpers.database import database

item_routes = Blueprint('item', __name__, url_prefix='')

@item_routes.route('/items', methods=['GET'])
def get_items():
    return json.dumps(database.get_all_items())

@item_routes.route('/items/<home>/<category>', methods=['GET'])
def get_home_category_items(home, category):
    return json.dumps(database.get_home_category_items(home, category))