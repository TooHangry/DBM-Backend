from app.helpers.lists import serializers


def get_all_lists(db):
    db.execute('''
                SELECT *
                FROM lists
                ''')
    return serializers.serialize_lists(db.fetchall())

def remove_list(db, connection, id):
    db.execute('''
            DELETE FROM lists
            WHERE id = ?
            ''', (id, ))
    connection.commit()

def get_lists_from_home(db, home):
    db.execute('''
                SELECT *
                FROM lists
                WHERE home = ?
                ''', (home, ))
    return serializers.serialize_lists(db.fetchall())

def get_user_lists(db, id):
    db.execute('''
                SELECT *
                FROM lists
                WHERE tasked_user = ?
                ''', (id, ))
    return serializers.serialize_lists(db.fetchall())


def get_list_by_id(db, id):
    db.execute('''
                SELECT *
                FROM lists
                WHERE id = ?
                ''', (id, ))
    lists = serializers.serialize_lists(db.fetchall())
    return lists[0] if len(lists) > 0 else []


def create_list(db, connection, title, tasked_user_id, home_id, date_due, is_complete):
    db.execute('''
                INSERT INTO lists (title, tasked_user, home, date_due, is_complete)
                VALUES (?, ?, ?, ?, ?)
                ''', (title, tasked_user_id, home_id, date_due, is_complete, ))
    connection.commit()

    db.execute('''
                SELECT *
                FROM lists
                WHERE id = ?;
                ''', (db.lastrowid, ))
    lists = serializers.serialize_lists(db.fetchall())
    return lists[0] if len(lists) > 0 else []

def update_user_and_title(db, connection, id, user, title, is_complete):
    db.execute('''
                UPDATE lists 
                SET tasked_user = ?, title = ?, is_complete = ?
                WHERE id = ?;
                ''', (user, title, is_complete, id ))
    connection.commit()

def get_list_by_id(db, list):
    db.execute('''
                SELECT *
                FROM lists
                WHERE id = ?
                ''', (list, ))
    lists = serializers.serialize_lists(db.fetchall())
    return lists[0] if len(lists) > 0 else []
