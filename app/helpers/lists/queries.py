from app.helpers.lists import serializers

def get_all_lists(db):
    db.execute('''
                SELECT *
                FROM lists
                ''')
    return serializers.serialize_lists(db.fetchall())

def get_lists_from_home(db, home):
    db.execute('''
                SELECT *
                FROM lists
                WHERE home = ?
                ''', (home, ))
    return serializers.serialize_lists(db.fetchall())

def create_list(db, connection, title, tasked_user_id, home_id, date_tasked, date_due, is_complete):
    db.execute('''
                INSERT INTO lists (title, tasked_user, home, date_tasked, date_due, is_complete)
                VALUES (?, ?, ?, ?, ?, ?)
                ''', (title, tasked_user_id, home_id, date_tasked, date_due, is_complete, ))
    connection.commit()

    db.execute('''
                SELECT *
                FROM lists
                WHERE id = ?;
                ''', (db.lastrowid, ))
    lists = serializers.serialize_lists(db.fetchall())
    return lists[0] if len(lists) > 0 else []