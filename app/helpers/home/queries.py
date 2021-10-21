from os import abort
from app.helpers.home import serializers
from flask import abort
import uuid

def get_all_homes(db):
    db.execute('''
                SELECT *
                FROM homes
                ''')
    return serializers.serialize_homes(db.fetchall())

def get_home(db, id):
    db.execute('''
            SELECT *
            FROM homes
            WHERE id = ?;
            ''', (id, ))
    homes = serializers.serialize_homes(db.fetchall())
    return homes[0] if len(homes) > 0 else abort(404)

def get_home_categories(db, id):
    db.execute('''
                SELECT categories.category
                FROM categories
                WHERE categories.id in (SELECT DISTINCT home_items.category
                                        From homes
                                        JOIN home_items ON home_items.home = homes.id
                                        WHERE homes.id = ?)
                ''', (id,))
    return serializers.serialize_categories(db.fetchall())

def create_new_home(db, connection, name):
    guid = uuid.uuid1()
    db.execute('''
                INSERT INTO homes (nickname, GUID)
                VALUES (?, ?)''', (name, str(guid)))
    connection.commit()

    db.execute('''
                SELECT *
                FROM homes
                WHERE nickname = ? AND GUID = ?''', (name, str(guid),))
    homes = serializers.serialize_homes(db.fetchall())
    return homes[0] if len(homes) > 0 else abort(404)

def create_new_user_to_home(db, connection, user, home, admin):
    db.execute('''
                INSERT INTO user_to_homes (user, home, is_admin)
                VALUES (?, ?, ?)
                ''', (user['id'], home['id'], 'T' if admin['id'] == user['id'] else 'F'))
    connection.commit()

    db.execute('''
                SELECT * 
                FROM user_to_homes
                WHERE user = ? AND home = ?''', (user['id'], home['id'],))