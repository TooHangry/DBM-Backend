from flask import Flask, request
from flask_cors import CORS
from app.helpers.database import database

# Creates a flask instance with cross-origin resource sharing
app = Flask(__name__)
app.config.from_object('config')
cors = CORS(app, resources={r'/*': {"origins": '*'}})

# Import modules and routes
from app.routes.default.controller import default_routes as default_module
from app.routes.user.controller import user_routes as user_module
from app.routes.home.controller import home_routes as home_module
from app.routes.item.controller import item_routes as item_module
from app.routes.list.controller import list_routes as list_module
app.register_blueprint(default_module)
app.register_blueprint(user_module)
app.register_blueprint(home_module)
app.register_blueprint(item_module)
app.register_blueprint(list_module)

database.initialize_database()