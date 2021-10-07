from os import abort
from app.helpers.home import serializers
from flask import abort

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
            ''', (id))
    homes = serializers.serialize_homes(db.fetchall())
    return homes[0] if len(homes) > 0 else abort(404)

def get_home_categories(db, id):
    db.execute('''
                Select categories.category
                FROM categories
                where categories.id in (SELECT DISTINCT home_items.category
                                        From homes
                                        join home_items on home_items.home = homes.id
                                        WHERE homes.id = ?)
                ''', (id))
    return serializers.serialize_categories(db.fetchall())