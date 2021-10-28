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

