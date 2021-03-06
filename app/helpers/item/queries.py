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


def update_item(db, connection, item_id, name, quantity, threshold, category_id, home_id):
    db.execute('''
                UPDATE home_items
                SET home = ?, quantity = ?, item_name = ?, category = ?, alert_threshold = ?
                WHERE id = ?
                ''', (home_id, quantity, name, category_id, threshold, item_id))
    connection.commit()

def update_item_in_list(db, connection, id, quantity):
    db.execute('''
                UPDATE home_items
                SET quantity = ?
                WHERE id = ?
                ''', (quantity, id, ))
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

def get_items_in_list(db, list):
    db.execute('''
                SELECT *
                FROM home_items
                WHERE list_id = ?
                ''', (list, ))
    return serializers.serialize_items(db.fetchall())

def reset_list_status(db, connection, list_id):
    db.execute('''
                UPDATE home_items
                SET list_id = 0, needed = 0
                WHERE list_id = ?
                ''', (list_id, ))
    connection.commit()

def add_item_to_list(db, connection, list_id, item_id, needed_count):
    db.execute('''
                UPDATE home_items
                SET list_id = ?, needed = ?
                WHERE id = ?
                ''', (list_id, needed_count, item_id, ))
    connection.commit()

def remove_item_from_list(db, connection, id, items_to_remove):
    item_tuple =  tuple(','.join(items_to_remove).split(','))
    questionmarks = '?' * len(item_tuple)
    query = '''
                UPDATE home_items
                SET list_id = NULL
                WHERE id IN ({})
                '''.format(','.join(questionmarks))

    db.execute(query, item_tuple)
    connection.commit()

def get_item(db, id):
    db.execute('''
                SELECT *
                FROM home_items
                WHERE id = ?
                ''', (id, ))
    items = serializers.serialize_items(db.fetchall())
    return items[0] if len(items) > 0 else abort(404)


def delete_item(db, connection, item_id):
    item_to_return = get_item(db, item_id)
    if item_to_return:
        db.execute('''
                    DELETE FROM home_items
                    WHERE id = ? 
                    ''', (item_id, ))
        connection.commit()
        return item_to_return
    abort(404)


def get_home_items(db, home_id, category_id):
    db.execute('''
                SELECT home_items.id, home_items.item_name, home_items.quantity, categories.category, home_items.alert_threshold, home_items.list_id, needed
                FROM home_items
                JOIN categories ON categories.id = home_items.category
                WHERE home_items.home = ? AND categories.category = ?
                ''', (home_id, category_id,))
    return serializers.serialize_home_items(db.fetchall())
