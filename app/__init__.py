from flask import Flask, request
from flask_cors import CORS
from app.helpers.database import database

# Creates a flask instance with cross-origin resource sharing
app = Flask(__name__)
app.config.from_object('config')
cors = CORS(app, resources={r'/*': {"origins": '*'}})

# Initializes the SQLalchemy database



# Import modules and routes
from app.routes.default.controller import default_routes as default_module
from app.routes.user.controller import user_routes as user_module
from app.routes.home.controller import home_routes as home_module
from app.routes.item.controller import item_routes as item_module
app.register_blueprint(default_module)
app.register_blueprint(user_module)
app.register_blueprint(home_module)
app.register_blueprint(item_module)

database.initialize_database()


###################
# EXAMPLE QUERIES #
###################

# THIS ONE MERGES USERS -> USER_TO_HOMES -> HOMES
# This allows us to grab all of a user's homes

# SELECT *
# FROM users
# INNER JOIN (SELECT *
#             FROM user_to_homes
#             INNER JOIN homes
#             ON user_to_homes.home = homes.id) merged_homes
# ON users.id = merged_homes.home