from flask import Blueprint, request
import json
from app.helpers.database import database

item_routes = Blueprint('item', __name__, url_prefix='')

@item_routes.route('/items', methods=['GET'])
def get_items():
    return json.dumps(database.get_all_items())

@item_routes.route('/items/<home>', methods=['POST'])
def add_item(home):
    name = request.form['name']
    quantity = request.form['quantity']
    threshold = request.form['threshold']
    category_name = request.form['category']
    database.add_item(home, name, quantity, threshold, category_name)
    return json.dumps(database.get_home_info(home))

@item_routes.route('/categories', methods=['GET'])
def get_categories():
    return json.dumps(database.get_all_categories())