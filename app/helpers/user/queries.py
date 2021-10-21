from flask import abort
from app.helpers.user import serializers
from app.models.user import User
from app.helpers.item import queries as item_queries


def create_user(db, connection, email, fname, lname, hashed_password, token):
    db.execute('''
                INSERT INTO users (first_name, last_name, email, password, UUID_token)
                VALUES
                (?, ?, ?, ?, ?)
                ''', (fname, lname, email, hashed_password, token, ))
    connection.commit()


def login_current_user(db, email, password):
    db.execute('''
                SELECT id, first_name, last_name, email, date_joined, UUID_token
                FROM users
                WHERE email = ? AND password = ?;
                ''', (email, password, ))
    
    users = serializers.serialize_users(db.fetchall())
    user: dict = users[0] if len(users) > 0 else abort(404)
    if user:
        homes = get_user_homes(db, user['id'])
        user['homes'] = homes
        categories = item_queries.get_all_categories(db)
        user['categories'] = categories
        return user
    abort(404)

def login_from_token(db, token):
    db.execute('''
                SELECT id, first_name, last_name, email, date_joined, UUID_token
                FROM users
                WHERE UUID_token = '{}';
                '''.format(token))
    users = serializers.serialize_users(db.fetchall())
    user: dict = users[0] if len(users) > 0 else abort(404)
    if user:
        homes = get_user_homes(db, user['id'])
        user['homes'] = homes
        categories = item_queries.get_all_categories(db)
        user['categories'] = categories
        return user
    abort(404)

def get_user_homes(db, id):
    db.execute('''
                SELECT home, is_admin, nickname, users.id
                FROM users
                INNER JOIN (SELECT *
                            FROM user_to_homes
                            INNER JOIN homes
                            ON user_to_homes.home = homes.id) merged_homes
                ON users.id = merged_homes.user
                WHERE users.id = ?
                ''', (id, ))
    return serializers.serialize_homes(db.fetchall())

def get_user_home(db, user, home):
    db.execute('''
                SELECT home, is_admin, nickname, users.id
                FROM users
                INNER JOIN (SELECT *
                            FROM user_to_homes
                            INNER JOIN homes
                            ON user_to_homes.home = homes.id AND homes.id = ?) merged_homes
                ON users.id = merged_homes.user
                WHERE users.id = ?;
                '''(home, user, ))
    homes = serializers.serialize_homes(db.fetchall())
    return homes[0] if len(homes) > 0 else abort(404)

def get_user_by_id(db, id):
    db.execute('''
                SELECT * 
                FROM users
                WHERE id = ?
                ''', (id, ))
    users = serializers.serialize_users(db.fetchall())
    return users[0] if len(users) > 0 else {}


def get_all_users(db):
    db.execute('''
                SELECT * 
                FROM users
                ''')
    users = serializers.serialize_users(db.fetchall())
    return users

def get_users_by_email(db, emails):
    email_tuple = tuple(','.join(emails).split (','))
    questionmarks = '?' * len(email_tuple)
    query = '''
                SELECT *
                FROM users
                WHERE email IN ({})
                '''.format(','.join(questionmarks))

    db.execute(query, email_tuple)
    users = serializers.serialize_users(db.fetchall())
    return users