from app.helpers.database import tables
from app.helpers.item import queries as item_queries
from app.helpers.home import queries as home_queries
from app.helpers.user import queries as user_queries
import sqlite3
import itertools
# Running on a single thread
connection = sqlite3.connect('db.sqlite3', timeout=10, check_same_thread=False)
db = connection.cursor()


################
# USER QUERIES #
################

def create_user(email, fname, lname, hashed_password, token):
    return user_queries.create_user(db, connection, email, fname, lname, hashed_password, token)


def login_current_user(email, password):
    return user_queries.login_current_user(db, email, password)


def login_from_token(token):
    return user_queries.login_from_token(db, token)


def get_user_homes(id):
    return user_queries.get_user_homes(db, id)


def get_user_by_id(id):
    return user_queries.get_user_by_id(db, id)


def get_all_users():
    return user_queries.get_user_by_id(db)


################
# HOME QUERIES #
################
def get_all_homes():
    return home_queries.get_all_homes(db)


def get_home(id):
    return home_queries.get_home(db, id)


def get_home_info(home_id):
    home = get_home(home_id)
    categories = home_queries.get_home_categories(db, home_id)
    home['categories'] = categories if len(categories) > 0 else []
    items = [get_home_category_items(home_id, cat) for cat in categories]
    flattened_items = list(itertools.chain(*items))
    home['items'] = flattened_items if len(flattened_items) > 0 else []
    return home


def get_category_id(category_name):
    return item_queries.get_category(db, category_name)

################
# ITEM QUERIES #
################

def get_all_categories():
    return item_queries.get_all_categories(db)
    
def add_item(home, name, quantity, threshold, category_name):
    category_id = get_category_id(category_name)
    category_id = 1 if len(category_id) < 1 else int(category_id[0])
    item_queries.add_item(db, connection, home, name,
                          quantity, threshold, category_id)

def get_all_items():
    return item_queries.get_all_items(db)

def get_home_category_items(home_id, category_id):
    return item_queries.get_home_items(db, home_id, category_id)

###########################
# DATABASE INITIALIZATION #
###########################


def initialize_database():
    tables.create_tables(db)
    tables.populate_tables(db, connection)
