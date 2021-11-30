from os import abort
from sqlite3 import dbapi2
from app.helpers.database import tables
from app.helpers.item import queries as item_queries
from app.helpers.home import queries as home_queries
from app.helpers.user import queries as user_queries
from app.helpers.invite import queries as invite_queries
from app.helpers.email import email as email_helper
from app.helpers.lists import queries as list_queries
import sqlite3
import itertools

# Running on a single thread
connection = sqlite3.connect('db.sqlite3', timeout=10, check_same_thread=False)
db = connection.cursor()


################
# USER QUERIES #
################

def create_user(email, fname, lname, hashed_password, token):
    try:
        user_queries.create_user(
            db, connection, email, fname, lname, hashed_password, token)
        user = user_queries.get_user_by_email(db, email)

        if user:
            invites = get_invites_for_user(email)
            for invite in invites:
                home = home_queries.get_home(db, invite['home'])
                admin = user_queries.get_home_admin(db, invite['home'])
                remove_invite(invite['home'], invite['email'])
                home_queries.create_new_user_to_home(
                    db, connection, user, home, admin)
    except:
        print("User could not be created")


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
    return user_queries.get_all_users(db)


def get_home_users(home_id):
    return user_queries.get_home_users(db, home_id)


def get_users_by_email(emails):
    return user_queries.get_users_by_email(db, emails)


def remove_user(user_id, home_id):
    return user_queries.remove_user(db, connection, user_id, home_id)


def add_user(email, home_id):
    user = user_queries.get_user_by_email(db, email)
    admin = user_queries.get_home_admin(db, home_id)
    home = home_queries.get_home(db, home_id)

    if user:
        try:
            home_queries.create_new_user_to_home(
                db, connection, user, home, admin)
            return 200
        except:
            return 400
    else:
        admin = user_queries.get_home_admin(db, home_id)
        email_helper.send_invites([email], home, admin)
        # for non-members, create an invite
        try:
            create_invite(email, home_id)
            return 201
        except:
            return 400


def get_user_by_email(email):
    return user_queries.get_user_by_email(db, email)

def get_member_by_email(email):
    return user_queries.get_member_by_email(db, email)

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

    # NEED TO GET HOME USERS AND INVITES
    home['users'] = get_home_users(home_id)
    home['invites'] = get_home_invites(home_id)
    home['admin'] = user_queries.get_home_admin(db, home_id)['email']

    return home


def create_new_home(name, admin_id, invite_list):
    admin = get_user_by_id(admin_id)

    if admin['email'] not in invite_list:
        invite_list.append(admin['email'])

    if admin:
        users = get_users_by_email(invite_list)
        user_id = users[0]['id']
        home = home_queries.create_new_home(db, connection, name)

        non_members = invite_list
        members = []
        for user in users:
            # SEND INVITE EMAILS HERE
            non_members.remove(user['email'])
            members.append(user['email'])
            home_queries.create_new_user_to_home(
                db, connection, user, home, admin)
            if user['id'] != admin['id']:
                email_helper.send_collab_notice(user, home, admin)

        # Sends the invite email
        email_helper.send_invites(non_members, home, admin)

        # for non-members, create an invite
        for email in non_members:
            create_invite(email, home['id'])

        return get_user_home(user_id, home['id'])

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


def remove_item(item_id):
    return item_queries.delete_item(db, connection, item_id)


def add_item(home, name, quantity, threshold, category_name):
    category_id = get_category_id(category_name)
    category_id = 1 if len(category_id) < 1 else int(category_id[0])
    item_queries.add_item(db, connection, home, name,
                          quantity, threshold, category_id)
    return


def update_item(item_id, name, quantity, threshold, category_name, home_id):
    category_id = get_category_id(category_name)
    category_id = 1 if len(category_id) < 1 else int(category_id[0])
    item_queries.update_item(db, connection, item_id,
                             name, quantity, threshold, category_id, home_id)


def get_all_items():
    return item_queries.get_all_items(db)


def get_home_category_items(home_id, category_id):
    return item_queries.get_home_items(db, home_id, category_id)


##################
# INVITE QUERIES #
##################

def get_home_invites(home_id):
    return invite_queries.get_home_invites(db, home_id)


def create_invite(email, home_id):
    return invite_queries.create_invite(db, connection, email, home_id)


def remove_invite(home, user):
    return invite_queries.remove_invite(db, connection, home, user)


def get_invites_for_user(email):
    return invite_queries.get_invites_for_user(db, email)


def get_invite(email, home_id):
    return invite_queries.get_invite(db, email, home_id)

################
# LIST QUERIES #
################
def get_lists():
    return list_queries.get_all_lists(db)

def get_lists_in_home(home):
    lists = list_queries.get_lists_from_home(db, home)
    for l in lists:
        l['items'] = item_queries.get_items_in_list(db, l['id'])
        l['taskedUserEmail'] = user_queries.get_user_by_id(db, l['taskedUser'])['email']
        l['homeName'] = home_queries.get_home(db, l['homeID'])['nickname']
    return lists

def get_list_by_id(id):
    lists = list_queries.get_list_by_id(db, id)
    lists['items'] = item_queries.get_items_in_list(db, lists['id'])
    lists['taskedUserEmail'] = user_queries.get_user_by_id(db, lists['taskedUser'])['email']
    lists['homeName'] = home_queries.get_home(db, lists['homeID'])['nickname']
    return lists

def get_user_lists(id):
    lists = list_queries.get_user_lists(db, id)
    for l in lists:
        l['items'] = item_queries.get_items_in_list(db, l['id'])
        l['taskedUserEmail'] = user_queries.get_user_by_id(db, l['taskedUser'])['email']
        l['homeName'] = home_queries.get_home(db, l['homeID'])['nickname']
    return lists

def create_list(title, tasked_user, home, is_complete, end_date):
    user = get_user_by_id(tasked_user)
    if user:
        lists = list_queries.create_list(db, connection, title, tasked_user, home, end_date, is_complete)
        lists['items'] = item_queries.get_items_in_list(db, lists['id'])
        lists['taskedUserEmail'] = user['email']
        lists['homeName'] = home_queries.get_home(db, lists['homeID'])['nickname']
        h = get_home(home)
        email_helper.send_list_notice(user, h, title, end_date)
        return lists

    abort(404)

def remove_list(id):
    list = get_list_by_id(id)
    item_queries.reset_list_status(db, connection, id)
    list_queries.remove_list(db, connection, id)
    return get_lists_in_home(list['homeID'])

def update_list(id, items, user, title):
    current_list = list_queries.get_list_by_id(db, id)
    if (current_list):
        items_in_list = item_queries.get_items_in_list(db, id)

        new_item_ids = list(map(lambda item: str(item['id']), items))
        list_item_ids = list(map(lambda item: str(item['id']), items_in_list))
       
        items_to_remove = []
        for item in list_item_ids:
            if item not in new_item_ids:
                items_to_remove.append(item)

        item_queries.remove_item_from_list(db, connection, id, items_to_remove)

        for item_id in new_item_ids:
            item_needed_count = [item for item in items if int(item['id']) == int(item_id)]
            if len(item_needed_count) > 0:
                item_queries.add_item_to_list(db, connection, id, item_id, item_needed_count[0]['needed'])
        
        is_complete = True
        for item in items:
            if int(item['needed'] if item['needed'] else 0) > int(item['quantity'] if item['quantity'] else 0):
                is_complete = False
        list_queries.update_user_and_title(db, connection, id, user, title, 'T' if is_complete else 'F')
    return

def update_list_items(id, items):
    current_list = list_queries.get_list_by_id(db, id)
    if (current_list):
        for item in items:
            item_queries.update_item_in_list(db, connection, item['id'], item['quantity'])
        

###########################
# DATABASE INITIALIZATION #
###########################


def initialize_database():
    tables.create_tables(db)
    tables.populate_tables(db, connection)
