from flask import Blueprint, request
import json
from app.helpers.database.database import get_all_homes

home_routes = Blueprint('home', __name__, url_prefix='')

@home_routes.route('/homes', methods=['GET'])
def get_homes():
    return json.dumps(get_all_homes())