from app.helpers.home.serializers import serialize_categories
from app.helpers.item import serializers
from flask import abort

def add_item(db, connection, home, name, quantity, threshold, category_id):
    db.execute('''
                INSERT INTO home_items (home, quantity, item_name, category, alert_threshold)
                VALUES
                ({}, {}, '{}', {}, {})
                '''.format(home, quantity, name.replace("'", "''"), category_id, threshold))
    connection.commit()

def get_category(db, category):
    db.execute('''
                SELECT *
                FROM categories
                WHERE category = '{}'
                '''.format(category))
    return serialize_categories(db.fetchall())

def get_all_categories(db):
    db.execute('''
                SELECT category
                FROM categories
                ''')
    return serialize_categories(db.fetchall())

def get_all_items(db):
    db.execute('''
                SELECT *
                FROM home_items
                ''')
    return serializers.serialize_items(db.fetchall())

def get_item(db, id):
    db.execute('''
                SELECT *
                FROM home_items
                WHERE id = ?
                ''', (id, ))
    items = serializers.serialize_items(db.fetchall())
    return items[0] if len(items) > 0 else abort(404)

def get_home_items(db, home_id, category_id):
    db.execute('''
                SELECT home_items.id, home_items.item_name, home_items.quantity, categories.category, home_items.alert_threshold
                FROM home_items
                JOIN categories ON categories.id = home_items.category
                WHERE home_items.home = ? AND categories.category = ?
                ''', (home_id, category_id,))
    return serializers.serialize_home_items(db.fetchall())