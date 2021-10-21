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

def get_user_home(user, home):
    return user_queries.get_user_home(db, user, home)

def get_user_by_id(id):
    return user_queries.get_user_by_id(db, id)

def get_all_users():
    return user_queries.get_user_by_id(db)

def get_users_by_email(emails):
    return user_queries.get_users_by_email(db, emails)

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

def create_new_home(name, admin_id, invite_list):
    admin = get_user_by_id(admin_id)

    if admin['email'] not in invite_list:
        invite_list.append(admin['email'])

    if admin:
        users = get_users_by_email(invite_list)
        home = home_queries.create_new_home(db, connection, name)

        non_members = invite_list
        members = []
        for user in users:
            # SEND INVITE EMAILS HERE
            non_members.remove(user['email'])
            members.append(user['email'])
            user_to_home = home_queries.create_new_user_to_home(db, connection, user, home, admin)

        return get_user_home(user['id'], home['id'])
    
    return {}


def get_category_id(category_name):
    return item_queries.get_category(db, category_name)

################
# ITEM QUERIES #
################

def get_all_categories():
    return item_queries.get_all_categories(db)

def get_item(id):
    return item_queries.get_item(db, id)

def add_item(home, name, quantity, threshold, category_name):
    category_id = get_category_id(category_name)
    category_id = 1 if len(category_id) < 1 else int(category_id[0])
    item_queries.add_item(db, connection, home, name,
                          quantity, threshold, category_id)
    return

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
