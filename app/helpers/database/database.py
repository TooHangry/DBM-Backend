import sqlite3

# Running on a single thread
connection = sqlite3.connect('db.sqlite3', timeout=10, check_same_thread=False)
db = connection.cursor()




from app.helpers.user import queries as user_queries
from app.helpers.home import queries as home_queries
from app.helpers.item import queries as item_queries
from app.helpers.database import tables

################
# USER QUERIES #
################
def login_current_user(email, password):
    return user_queries.login_current_user(db, email, password)

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

################
# ITEM QUERIES #
################
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