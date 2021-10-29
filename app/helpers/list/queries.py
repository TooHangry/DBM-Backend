from os import abort
from app.helpers.list import serializers
from flask import abort
import uuid

def get_all_lists(db):
    db.execute('''
                SELECT *
                FROM shopping_list
                ''')
    return serializers.serialize_lists(db.fetchall())

def get_user_lists(db, user_id):
    db.execute('''
                SELECT *
                FROM shopping_list
                WHERE tasked_to = ?
                ''', (user_id, ))
    shopping_lists = serializers.serialize_lists(db.fetchall())
    return shopping_lists[0] if len(shopping_lists) > 0 else abort(404)

def get_home_lists(db, home_id):
    db.execute('''
                SELECT *
                FROM shopping_list
                WHERE home_tasked = ?
                ''', (home_id, ))
    shopping_lists = serializers.serialize_lists(db.fetchall())
    return shopping_lists[0] if len(shopping_lists) > 0 else abort(404)

def create_list(db, connection, tasked_to, home_tasked, ):
    db.execute('''
                INSERT INTO shopping_list (tasked_to, home_tasked)
                VALUES (?, ?, ?)
                ''', (tasked_to, home_tasked))
    connection.commit()

def remove_list(db, connection, list_id, ):
    db.execute('''
                DELETE FROM shopping_list
                WHERE id = ?
                ''', (list_id, ))
    connection.commit()

def add_item_to_list(db, connection, list_id, item_id, quantity):
    db.execute('''
                INSERT INTO list_items (list_id, item_id, quantity, is_complete)
                VALUES (?, ?, ?, ?)
                ''', (list_id, item_id, quantity, 'F'))
    connection.commit()

def assign_list(db, connection, list_id, user_id, ):
    db.execute('''
                UPDATE shopping_list
                SET tasked_to = ?
                WHERE id = ?
                ''', (user_id, list_id, ))
    connection.commit()