from app.helpers.item import serializers

def get_all_items(db):
    db.execute('''
            SELECT *
            FROM home_items
            ''')
    return serializers.serialize_items(db.fetchall())

def get_home_items(db, home_id, category_id):
    db.execute('''
            SELECT home_items.item_name, home_items.quantity, categories.category, home_items.alert_threshold
            FROM home_items
            JOIN categories ON categories.id = home_items.category
            WHERE home_items.home = {} AND home_items.category = {}
            '''.format(home_id, category_id))
    return serializers.serialize_home_items(db.fetchall())